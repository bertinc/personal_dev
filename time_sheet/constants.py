import os

# Because I am very much against magic numbers that cannot be changed in one place and
# so I can reuse constant values.

TIMESHEET_TITLE = '{}|  Timesheet for {} to {}  |{}'
PAY_TITLE =       '{}|     Pay for {} to {}     |{}'
BORDER = '\n--------------------------------------------\n'
REPORT_COLUMNS = ['DAY', 'TIME', 'HOURS', 'DESCRIPTION']
PATH = os.path.dirname(os.path.realpath(__file__))
DATE_MARKER = 'DT:' # Marks a line as the start of a new day
DATE_LENGTH = 3 # Date must always have three values or we have a problem
RATE = 70
TAX_RATE = 0.20
DAY_INDEX = 0
DESC_INDEX = 1
TIME_INDEX = 2
DUR_INDEX = -2
ENTRY_DELIMITER = ';'
TIME_DELIMITER = ':'
DATE_DELIMITER = '-'
ENTRY_LENGTH = 3
INPUT_DATE_FORMAT = '%m-%d-%Y'
DATE_FORMAT = '%Y-%m-%d'
LONG_JUSTIFICATION = 13
SHORT_JUSTIFICATION = 10
PAY_JUSTIFICATION = 18
MINUTES_PER_HOUR = 60

# This is the default stuff we put at the top of the timesheet file after import
DT_STR = '# Date - DT:mm-dd-yyyy\n'
ENTRY_STR = '# Any number of log entries after a Date - some desctiption;h:m{am/pm};h:m or just m\n'
DOC_STR = '# DOC: comes imediately after a log entry to link notes to an entry\n'
LAST_IMPORT = '# Last import on {}\n'
LAST_IMPORT_FORMAT = '%m-%d-%Y at %I:%M %p'