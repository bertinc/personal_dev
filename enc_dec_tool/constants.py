import os

# Because I am very much against magic numbers that cannot be changed in one place and
# so I can reuse constant values.

TITLE = '{}|  {}  |{}'
BORDER = '\n--------------------------------------------\n'
PATH = os.path.dirname(os.path.realpath(__file__))
DEC_FILE = f'{PATH}\\dec.txt'
ENC_FILE = f'{PATH}\\enc.txt'
LONG_JUSTIFICATION = 13
SHORT_JUSTIFICATION = 10
ENC_DEC_KEY = 'nbpPE9hgALVwKsCudlCCK19ojWyAzShpyqCPpQfWYIY='