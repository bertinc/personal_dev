import os

TITLE = "\n-------------------\n|  Timesheet 0.1.0  |\n-------------------\n"
PATH = os.path.dirname(os.path.realpath(__file__))
DATE_MARKER = 'DT:' # Marks a line as the start of a new day
DATE_LENGTH = 3 # Date must always have three values or we have a problem
ENTRY_DELIMITER = ';'
ENTRY_LENGTH = 3