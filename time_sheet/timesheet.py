"""Main Timesheet Logic"""
from datetime import datetime, timedelta
import argparse
import calendar
from db import TimesheetDB
import constants as Const


def manage_timesheet(args):
    """
    Handle command line args and do what they say
    """
    timesheet_db = TimesheetDB()
    timesheet_db.init_db()
    response = None
    start = None
    end = None

    # IMPORTING DATA
    if hasattr(args, 'file'):
        entries, errors = import_entries(args, timesheet_db.valid_categories)
        if errors:
            for error in errors:
                print(error)
        if entries:
            timesheet_db.insert_bulk_entries(entries)
        print(f'Imported {len(entries)} entries.')

    # REPORTING DATA
    elif hasattr(args, 'start'):
        if args.start and args.end:
            # a specific start and end was provided
            start, end = args.start, args.end
            response = timesheet_db.get_report_between(_format_date(start), _format_date(end))
        elif args.all:
            # you just want everything ever entered in the timesheet
            response = timesheet_db.get_report_all()
            start, end = 'beginning', 'end'
        elif args.current:
            # whatever the current pay period is
            start, end = _get_current_start_end()
            response = timesheet_db.get_report_between(start, end)
        elif args.month:
            # report for a chosen month
            start, end = _get_month_start_end(args.month, args.year)
            response = timesheet_db.get_report_between(start, end)
        report, hours_by_day = generate_activity_report(start, end, response)

        if args.pay:
            # because somethings you just want to see some extra numbers
            pay = generate_pay_report(start, end, hours_by_day)
            report = report + pay

        if args.fileout:
            # send to output file
            report_filename = f'{Const.PATH}\\report.txt'
            with open(report_filename, 'w', encoding='utf-8') as report_file:
                for line in report:
                    report_file.write(line + '\n')
                print(f'Output sent to {report_filename}')
        else:
            # or just print it to the console
            for line in report:
                print(line)
    # print(json.dumps(hours_by_day))
    
def get_current_report():
    timesheet_db = TimesheetDB()
    timesheet_db.init_db()
    response = None
    start = None
    end = None
    start, end = _get_current_start_end()
    response = timesheet_db.get_report_between(start, end)
    report, hours_by_day = generate_activity_report(start, end, response)
    # print(hours_by_day)
    report_filename = f'{Const.PATH}\\report.txt'
    with open(report_filename, 'w', encoding='utf-8') as report_file:
        for line in report:
            report_file.write(line + '\n')
        print(f'Output sent to {report_filename}')
    # return "Got current report"

def import_entries(args, valid_categories):
    """
    Using an imput file, import, one line at a time, all new entries.
    Args:
        args: command line args
    """
    ts_file_path = f'{Const.PATH}\\input\\timesheet.txt'
    timesheet_file = open(ts_file_path, encoding='utf-8')
    lines = timesheet_file.readlines()
    date_str = ''
    new_entry = {}
    entry_list = []
    response = []
    for line in lines:
        clean_line = line.strip()
        # 1. If it's a date, then we are at the start of a day. Save the value
        #    and append any previous entry to the list.
        if clean_line.startswith('DT:'):
            date_str = _format_date(clean_line[3:])
            if new_entry:
                new_entry['added'] = True
                entry_list.append(new_entry['values'])
        # 2. If it's a DOC then we should have an entry ready for insert.
        #    Add the DOC to that entry.
        elif clean_line.startswith('DOC:'):
            if new_entry:
                vals_list = list(new_entry['values'])
                vals_list[-1] = clean_line[4:]
                new_entry['values'] = tuple(vals_list)
            else:
                response.append("ERROR: We have a DOC with no entry!")
                return [], response
        # 3. If it's not a DOC or a date, then it's either a new entry, comment,
        #    or garbage. Prep for insert if it's an entry, otherwise, ignore it.
        else:
            entry_array = clean_line.split(Const.ENTRY_DELIMITER)
            if len(entry_array) != Const.ENTRY_LENGTH or clean_line.startswith('#'):
                # this is a comment or garbage
                continue
            if not date_str:
                response.append("ERROR: No date string for this entry!")
                return [], response
            if new_entry and not new_entry['added']:
                # if a previous entry exists, append it to the list now
                new_entry['added'] = True
                entry_list.append(new_entry['values'])
            # check if the category is valid
            if entry_array[0] not in valid_categories:
                entry_array[0] = 'NONE'
            new_entry = {
                'values': (date_str, entry_array[0], entry_array[1], _convert_time(entry_array[2], False), _to_minutes(entry_array[3]), ''),
                'added': False
            }
    if new_entry and not new_entry['added']:
        entry_list.append(new_entry['values'])

    timesheet_file.close()

    # now clear the timesheet and add a timestamp for the last time it was imported
    with open(ts_file_path, 'w', encoding='utf-8') as timesheet_file:
        timesheet_file.write(Const.DT_STR)
        timesheet_file.write(Const.ENTRY_STR)
        timesheet_file.write(Const.CATEGORIES.format(', '.join(valid_categories)))
        timesheet_file.write(Const.DOC_STR)
        timesheet_file.write(Const.LAST_IMPORT.format(datetime.now().strftime(Const.LAST_IMPORT_FORMAT)))
    return entry_list, response

def _format_date(date_string):
    date_array = date_string.split('-')
    # assume month, day, year (likely mm-dd-yyyy)
    # convert to yyyy-mm-dd to allow easy search
    return f'{date_array[2]}-{date_array[0]}-{date_array[1]}'

def _get_current_start_end():
    """
    Figure out how far we are into the current month. If we are at or before the
    first Tuesday, then return the start and end dates for the previous month. 
    Otherwise return start and end dates for current month.

    Returns:
        tuple: The start and end date strings
    """
    today = datetime.now()
    first_day = datetime(today.year, today.month, 1)
    first_tuesday = _get_first_tuesday(first_day)
    if today <= first_tuesday and today >= first_day:
        # in this case, we need to get the first and last day of last month
        prev_month = first_day - timedelta(days=1)
        start, end = _get_month_start_end(prev_month.month, None)
    else:
        # otherwise, we are after the furst tuesday so pass back values for this month
        start, end = _get_month_start_end(today.month, None)

    return start, end

def _get_first_tuesday(first_day_of_the_month):
    """
    Does exactly as it sounds. Give it any first day of the month and it will
    pass pack the furst Tuesday of that month.

    Args:
        first_day_of_the_month (datetime): First day of the month

    Returns:
        datetime: first tuesday of the month
    """
    # This should give us the closest Tuesday before the current day
    offset = 1 - first_day_of_the_month.weekday()
    if offset < 0:
        # if it's negative, the closest previous Tuesday was last month
        # add 7 days and you got the first Tuesday
        offset += 7
    # return the first day of the month plus whatever offset we found
    return first_day_of_the_month + timedelta(offset)

def _get_month_start_end(month, year=None):
    """
    For a given month, and an optional year, return a string representation of
    the first day of that month and last day of that month in year-month-day
    formatting.

    Args:
        month (int): month where we need to find the first and last day
        year (int): optional value if you want to specify the year

    Returns:
        tuple: start and end date strings with year-month-day formatting
    """
    if not year:
        today = datetime.now()
        if today.month < month:
            # We will just assume it's January and we want
            # December of last year. I know it's not super smart
            # but I don't care for now.
            year = today.year - 1
        else:
            year = today.year
    # to get the first weekday of the month and the max number of days
    # we don't actually care about the first value
    first_last = calendar.monthrange(year, month)
    first = datetime(year, month, 1)
    last = datetime(year, month, first_last[1])
    return first.strftime(Const.DATE_FORMAT), last.strftime(Const.DATE_FORMAT)

def generate_activity_report(start, end, data):
    """
    Here we are just trying to generate a human readable report of whatever timesheet
    data was queried.

    Args:
        start (str): start date in year-month-day format
        end (str): end date in year-month-day format
        data (list): data queried from the data base using start and end dates
    """
    total_minutes = 0
    output_str = []
    # 1. Print the TITLE
    output_str.append(Const.TIMESHEET_TITLE.format(Const.BORDER, start, end, Const.BORDER))
    # 2. Print the column names across the top
    cols_str = ''
    for col in Const.REPORT_COLUMNS:
        if col.upper() == 'DAY':
            cols_str += col.ljust(Const.LONG_JUSTIFICATION)
        elif col.upper() == 'DESCRIPTION':
            cols_str += col
        else:
            cols_str += col.ljust(Const.SHORT_JUSTIFICATION)
    output_str.append(cols_str)
    # 3. Print a line for each entry
    hours_by_day = {}
    for entry in data:
        day = entry[Const.DAY_INDEX].ljust(Const.LONG_JUSTIFICATION)
        desc = entry[Const.DESC_INDEX]
        time = _convert_time(entry[Const.TIME_INDEX]).ljust(Const.SHORT_JUSTIFICATION)
        total_minutes += entry[Const.DUR_INDEX]
        curr_hours = entry[Const.DUR_INDEX] / Const.MINUTES_PER_HOUR
        hours = str(f'{curr_hours:.2f}').ljust(Const.SHORT_JUSTIFICATION) # make sure hours is only 2 decimal places
        output_str.append(f'{day}{time}{hours}{desc}')
        if entry[Const.DAY_INDEX] not in hours_by_day:
            hours_by_day[entry[Const.DAY_INDEX]] = curr_hours
        else:
            hours_by_day[entry[Const.DAY_INDEX]] += curr_hours
    #4. Print the sumary
    hours = total_minutes / Const.MINUTES_PER_HOUR
    output_str.append(f'\nTotal hours: {hours:.2f}\n')
    return output_str, hours_by_day

def generate_pay_report(start, end, hours_by_day):
    # pylint: disable=R0914
    # I'm okay with too many variables on this one
    """
    A more informative set of calculations based on the accumulated hours across
    a date range.

    Args:
        start (str): start date in year-month-day format
        end (str): end date in year-month-day format
        hours_by_day (dict): sum of hours by day
    """
    output_str = []
    output_str.append(Const.PAY_TITLE.format(Const.BORDER, start, end, Const.BORDER))
    day_count = len(hours_by_day)
    hours = sum(hours_by_day.values())
    gross_pay = hours * Const.RATE
    if Const.HSA_CONTRIBUTION:
        before_tax_cont = Const.HSA_CONTRIBUTION
    else:
        before_tax_cont = 0
    pay_minus_btc = gross_pay - before_tax_cont
    taxes = pay_minus_btc * Const.TAX_RATE
    net_pay = pay_minus_btc - taxes
    if day_count > 0:
        hrs_per_day = hours / day_count
    else:
        hrs_per_day = 0

    output_str.append(f'{"Days Worked: ":>17}{day_count}')
    output_str.append(f'{"Hrs per day: ":>17}{hrs_per_day:.2f}')
    output_str.append(f'{"Total hours: ":>17}{hours:,.2f}')
    output_str.append(f'{"Tax Rate: ":>17}{Const.TAX_RATE:.1%}')
    output_str.append(f'{"Gross Pay: $":>18}{gross_pay:,.2f}')
    output_str.append(f'{"Before Tax Cont: $":>18}{before_tax_cont:,.2f}')
    output_str.append(f'{"Net Pay: $":>18}{net_pay:,.2f}')
    output_str.append(f'{"Save for taxes: $":>18}{taxes:,.2f}\n')

    return output_str

converted_minutes = 0
def _to_minutes(duration):
    """
    Converts an hours:minutes input into just minutes. I could enter it as traight minutes
    but it feels easier to do it in hours and minutes on the fly.    
    """
    hours_minutes = duration.split(Const.TIME_DELIMITER)
    if len(hours_minutes) == 2:
        # If the split gives us two things then it's in hours and minutes
        curr_min = ((int(hours_minutes[0]) * Const.MINUTES_PER_HOUR) + int(hours_minutes[1]))
    else:
        # If there is only one value then it will be minutes
        curr_min = int(hours_minutes[0])
    global converted_minutes
    converted_minutes = curr_min
    return curr_min

def _convert_time(time, to_twelve_hour=True):
    """
    Just a simple method to convert a time string back and forth. The database stores time in
    military format to allow for easy sort order. But when we display time in a report, it's
    in a nice twelve hour format for human eye consumption.

    Args:
        time (str): a string representation of time in hours:minutes (am/pm if not military) format
        to_twelve_hour (bool, optional): Set to False if you want military. Defaults to True.

    Returns:
        str: time as a string in either twelve hour or military
    """
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
        converted_time = f'{hours_str}:{mins_str} {am_pm}'
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
        converted_time = f'{hours_str}:{mins_str}'
    return converted_time

def run():
    """
    Setup all the potential arguments that can be fed to this tool
    and provide good help strings for usage.
    """
    desc = "Timesheet importer tool."
    final_note = "Don't forget to clear your times sheet after each use!"
    parser = argparse.ArgumentParser(description=desc, epilog=final_note)
    timesheet_file = f'{Const.PATH}\\input\\timesheet.txt'

    subs = parser.add_subparsers(title='commands')

    # Import new data
    arg_consume_file = subs.add_parser('import', help='Import timesheet entries from a file.')
    arg_consume_file.add_argument('-file', help='Filename of the plain text file to import.', default=timesheet_file)

    # Generate reports
    arg_report_timesheet = subs.add_parser('report', help='Generate a timesheet report for management.')
    arg_report_timesheet.add_argument('--all', '-a', action='store_true', help='Report on the entire stored timesheet database.')
    arg_report_timesheet.add_argument('--fileout', '-f', action='store_true', help='Turn this on if you want the output sent to report.txt')
    arg_report_timesheet.add_argument('--current', '-c', action='store_true', help='Report based on current pay period.')
    arg_report_timesheet.add_argument('--pay', '-p', action='store_true', help='Report hours with expected pay.')
    arg_report_timesheet.add_argument('--start', '-s', help='Start date.')
    arg_report_timesheet.add_argument('--end', '-e', help='End date')
    arg_report_timesheet.add_argument('--month', '-m', type=int, help='To request a specific month in the current year.')
    arg_report_timesheet.add_argument('--year', '-y', type=int, help='Optional if you want to specify a year with the month.')

    args = parser.parse_args()
    manage_timesheet(args)

if __name__ == "__main__" or __name__ == "<module>" or __name__ == "time_sheet.timesheet":
    run()
else:
    print(f'No match for __name__ as {__name__}')
    