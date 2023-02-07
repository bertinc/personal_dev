import db
import argparse
import constants as const
import calendar
from datetime import datetime, timedelta

def manage_timesheet(args):
    timesheet_db = db.DB()
    timesheet_db.init_db()
    response = None
    start = None
    end = None
    if hasattr(args, 'file'):
        entries = import_entries(args)
        timesheet_db.insert_bulk_entries(entries)
    elif hasattr(args, 'start'):
        if args.start and args.end:
            start, end = args.start, args.end
            response = timesheet_db.get_report_between(_format_date(start), _format_date(end))
        elif args.all:
            response = timesheet_db.get_report_all()
            start, end = 'beginning', 'end'
        elif args.current:
            start, end = _get_current_start_end()
            response = timesheet_db.get_report_between(start, end)
        elif args.month:
            start, end = _get_month_start_end(args.month)
            response = timesheet_db.get_report_between(start, end)
        generate_report(start, end, response)

        if args.pay:
            report_hours_with_pay(start, end, response)
            

def import_entries(args):
    """
    Using an imput file, import, one line at a time, all new entries.
    Args:
        args: command line args
    """
    timesheet_file = open(args.file)
    lines = timesheet_file.readlines()
    date_str = ''
    new_entry = {}
    entry_list = []
    for line in lines:
        clean_line = line.strip()
        # 1. If it's a date, then we are at the start of a day. Save the value
        #    and append any previous entry to the list.
        if clean_line.startswith('DT:'):
            date_str = _format_date(clean_line[3:])
            if new_entry:
                new_entry['added'] = True
                entry_list.append(new_entry['values'])
            # date = datetime.strptime(date_str,'%m-%d-%Y')
            # timestamp = int(datetime.timestamp(date) * 1000)
            # print(timestamp)
        # 2. If it's a DOC then we should have an entry ready for insert.
        #    Add the DOC to that entry.
        elif clean_line.startswith('DOC:'):
            if new_entry:
                vals_list = list(new_entry['values'])
                vals_list[-1] = clean_line[4:]
                new_entry['values'] = tuple(vals_list)
            else:
                print("ERROR: We have a DOC with no entry!")
                return
        # 3. If it's not a DOC or a date, then it's either a new entry, comment,
        #    or garbage. Prep for insert if it's an entry, otherwise, ignore it.
        else:
            entry_array = clean_line.split(const.ENTRY_DELIMITER)
            if len(entry_array) != const.ENTRY_LENGTH or clean_line.startswith('#'):
                # this is a comment or garbage
                continue
            if not date_str:
                print("ERROR: No date string for this entry!")
                return
            if new_entry and not new_entry['added']:
                # if a previous entry exists, append it to the list now
                new_entry['added'] = True
                entry_list.append(new_entry['values'])
            new_entry = {
                'values': (date_str, entry_array[0], _convert_time(entry_array[1], False), entry_array[2], ''),
                'added': False
            }
    if new_entry and not new_entry['added']:
        entry_list.append(new_entry['values'])

    timesheet_file.close()

    return entry_list

def _format_date(date_string):
    date_array = date_string.split('-')
    # assume month, day, year (likely mm-dd-yyyy)
    # convert to yyyy-mm-dd to allow easy search
    return f'{date_array[2]}-{date_array[0]}-{date_array[1]}'

def _get_current_start_end(today=None):
    if not today:
        today = datetime.now()
    start = today.strftime(const.DATE_FORMAT)
    end = today.strftime(const.DATE_FORMAT)
    first_day = datetime(today.year, today.month, 1)
    first_tuesday = _get_first_tuesday(first_day)
    if today < first_tuesday:
        # in this case, we need to get the first tuesday of last month
        prev_month = first_day - timedelta(days=1)
        first_day_prev_month = datetime(prev_month.year, prev_month.month, 1)
        first_tuesday_prev_month = _get_first_tuesday(first_day_prev_month)
        # we actually want the day before the first Tuesday, which could technically
        # take us to the previous month
        first_monday = first_tuesday - timedelta(days=1)
        start = first_tuesday_prev_month.strftime(const.DATE_FORMAT)
        end = first_monday.strftime(const.DATE_FORMAT)
    else:
        # otherwise, today is still in the same month of the start
        start = first_tuesday.strftime(const.DATE_FORMAT)

    return start, end

def _get_first_tuesday(first_day_of_the_month):
    offset = 1 - first_day_of_the_month.weekday()
    if offset < 0:
        offset += 7
    return first_day_of_the_month + timedelta(offset)

def _get_month_start_end(month):
    today = datetime.now()
    first_last = calendar.monthrange(today.year, month)
    first = datetime(today.year, month, first_last[0])
    last = datetime(today.year, month, first_last[1])
    return first.strftime(const.DATE_FORMAT), last.strftime(const.DATE_FORMAT)

def generate_report(start, end, data):
    total_minutes = 0
    just_long = const.LONG_JUSTIFICATION
    just_short = const.SHORT_JUSTIFICATION
    print(const.TIMESHEET_TITLE.format(const.BORDER, start, end, const.BORDER))
    cols = const.REPORT_COLUMNS
    cols_str = ''
    for col in cols:
        if col.upper() == 'DAY':
            cols_str += col.ljust(just_long)
        elif col.upper() == 'DESCRIPTION':
            cols_str += col
        else:
            cols_str += col.ljust(just_short)
    print(cols_str)
    for entry in data:
        day = entry[const.DAY_INDEX].ljust(just_long)
        desc = entry[const.DESC_INDEX]
        time = _convert_time(entry[const.TIME_INDEX]).ljust(just_short)
        dur = entry[const.DUR_INDEX]
        hours_mins = dur.split(const.TIME_DELIMITER)
        curr_min = 0
        if len(hours_mins) == 2:
            # If the split gives us two things then it's in hours and minutes
            curr_min = ((int(hours_mins[0]) * const.MINUTES_PER_HOUR) + int(hours_mins[1]))
            total_minutes += curr_min
        else:
            # If there is only one value then it will be minutes
            curr_min = int(hours_mins[0])
            total_minutes += curr_min
        curr_hours = curr_min / const.MINUTES_PER_HOUR
        hours = str(curr_hours).ljust(just_short)
        print(f'{day}{time}{hours}{desc}')
    hours = total_minutes / const.MINUTES_PER_HOUR
    print(f'\nTotal hours: {hours}\n')

def report_hours_with_pay(start, end, data):
    total_minutes = 0
    print(const.PAY_TITLE.format(const.BORDER, start, end, const.BORDER))
    for entry in data:
        dur = entry[const.DUR_INDEX]
        hours_mins = dur.split(const.TIME_DELIMITER)
        if len(hours_mins) == 2:
            # If the split gives us two things then it's in hours and minutes
            curr_min = ((int(hours_mins[0]) * const.MINUTES_PER_HOUR) + int(hours_mins[1]))
            total_minutes += curr_min
        else:
            # If there is only one value then it will be minutes
            curr_min = int(hours_mins[0])
            total_minutes += curr_min
    hours = total_minutes / const.MINUTES_PER_HOUR
    gross_pay = hours * const.RATE
    taxes = gross_pay * const.TAX_RATE
    net_pay = gross_pay - taxes
    print(f'{"Total hours: ":>17}{hours:,.2f}')
    print(f'{"Tax Rate: ":>17}{const.TAX_RATE:.1%}')
    print(f'{"Gross Pay: $":>18}{gross_pay:,.2f}')
    print(f'{"Net Pay: $":>18}{net_pay:,.2f}')
    print(f'{"Save for taxes: $":>18}{taxes:,.2f}\n')

def _convert_time(time, to_twelve_hour=True):
    if to_twelve_hour:
        hours_mins = time.split(':')
        mins_str = str(hours_mins[1])
        hours = int(hours_mins[0])
        hours_str = str(hours)
        am_pm = 'AM'
        if hours >= 12:
            am_pm = 'PM'
            if hours > 12:
                hours_str = str(hours - 12)
        if hours == 0:
            hours_str = '12'
        return f'{hours_str}:{mins_str} {am_pm}'
    else:
        # need to return military time version
        hours_mins = time[:-2].split(':')
        hours = int(hours_mins[0])
        hours_str = str(hours)
        mins_str = str(hours_mins[1])
        am_pm = time[-2:]
        if am_pm.lower() == 'am' and hours < 10:
            hours_str = f'0{hours_str}'
        if am_pm.lower() == 'am' and hours == 12:
            hours_str = '00'
        if am_pm.lower() == 'pm' and hours < 12:
            hours_str = str(hours + 12)
        return f'{hours_str}:{mins_str}'

def run():
    desc = "Timesheet importer tool."
    final_note = "Don't forget to clear your times sheet after each use!"
    parser = argparse.ArgumentParser(description=desc, epilog=final_note)
    timesheet_file = f'{const.PATH}\\input\\timesheet.txt'

    subs = parser.add_subparsers(title='commands')

    arg_consume_file = subs.add_parser('import', help='Import timesheet entries from a file.')
    arg_consume_file.add_argument('-file', help='Filename of the plain text file to import.', default=timesheet_file)

    arg_report_timesheet = subs.add_parser('report', help='Generate a timesheet report for management.')
    arg_report_timesheet.add_argument('--all', '--a', action='store_true', help='Report on the entire stored timesheet database.')
    arg_report_timesheet.add_argument('--current', '--c', action='store_true', help='Report based on current pay period.')
    arg_report_timesheet.add_argument('--pay', '--p', action='store_true', help='Report hours with expected pay.')
    arg_report_timesheet.add_argument('-start', '-s', help='Start date.')
    arg_report_timesheet.add_argument('-end', '-e', help='End date')
    arg_report_timesheet.add_argument('-month', '-m', type=int, help='To request a specific month in the current year.')

    args = parser.parse_args()
    manage_timesheet(args)

if __name__ == "__main__":
    run()