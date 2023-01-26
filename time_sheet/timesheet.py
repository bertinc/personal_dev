import db
import argparse

def manage_timesheet(args):
    if args.file:
        print(args.file)

def run():
    desc = "Timesheet importer tool."
    final_note = "Don't forget to clear your times sheet after each use!"
    parser = argparse.ArgumentParser(description=desc, epilog=final_note)

    subs = parser.add_subparsers(title='commands')

    arg_consume_file = subs.add_parser('import', help='Import timesheet entries from a file.')
    arg_consume_file.add_argument('file', help='Filename of the plain text file to import.')

    arg_report_timesheet = subs.add_parser('report', help='Generate a timesheet report for management.')
    arg_report_timesheet.add_argument('--all', help='Report on the entire stored timesheet database.')
    arg_report_timesheet.add_argument('-start', '-s', help='Start date.')
    arg_report_timesheet.add_argument('-end', '-e', help='End date')

    args = parser.parse_args()
    manage_timesheet(args)

if __name__ == "__main__":
    run()