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
PASS = 'gAAAAABj_7HZ4n2HzXBiHLB0-0-FwK0fRel1TYqfjnh61J3NpE9ktMas4DVZmo-3Hr1zK28nRWzHJdAhtau4BztdqNw7VpMiRA=='