import db
import argparse
import constants as const
from datetime import datetime

def manage_timesheet(args):
    timesheet_db = db.DB()
    timesheet_db.init_db()
    if hasattr(args, 'file'):
        entries = import_entries(args)
        timesheet_db.insert_bulk_entries(entries)
    elif hasattr(args, 'start'):
        print('Gen report')

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
            date_str = clean_line[3:]
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
                'values': (date_str, entry_array[0], entry_array[1], entry_array[2], ''),
                'added': False
            }
    if new_entry and not new_entry['added']:
        entry_list.append(new_entry['values'])

    timesheet_file.close()

    return entry_list

def run():
    desc = "Timesheet importer tool."
    final_note = "Don't forget to clear your times sheet after each use!"
    parser = argparse.ArgumentParser(description=desc, epilog=final_note)
    timesheet_file = f'{const.PATH}\\input\\timesheet.txt'

    subs = parser.add_subparsers(title='commands')

    arg_consume_file = subs.add_parser('import', help='Import timesheet entries from a file.')
    arg_consume_file.add_argument('-file', help='Filename of the plain text file to import.', default=timesheet_file)

    arg_report_timesheet = subs.add_parser('report', help='Generate a timesheet report for management.')
    arg_report_timesheet.add_argument('--all', action='store_true', help='Report on the entire stored timesheet database.')
    arg_report_timesheet.add_argument('-start', '-s', help='Start date.')
    arg_report_timesheet.add_argument('-end', '-e', help='End date')

    args = parser.parse_args()
    manage_timesheet(args)

if __name__ == "__main__":
    run()