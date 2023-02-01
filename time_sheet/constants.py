import os

TIMESHEET_TITLE = '{}|  Timesheet for {} to {}  |{}'
PAY_TITLE =       '{}|     Pay for {} to {}     |{}'
BORDER = '\n--------------------------------------------\n'
REPORT_COLUMNS = ['DAY', 'TIME', 'HOURS', 'DESCRIPTION']
PATH = os.path.dirname(os.path.realpath(__file__))
DATE_MARKER = 'DT:' # Marks a line as the start of a new day
DATE_LENGTH = 3 # Date must always have three values or we have a problem
RATE = 70
TAX_RATE = 0.25
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