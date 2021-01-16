"""National Register Number generator, CLI version.

Usage:
    nrn_cli.py --be --generate (<YEAR> <MONTH> <DAY> <GENDER>)
    nrn_cli.py --be --isvalid <NUMBER>
    nrn_cli.py [-h | --help]
    nrn_cli.py [--version]

Options:
    -h --help   Show this screen
    --version   Show Version
    --be        Belgium
    --generate  Generate a new number
    --isvalid   Validate a number

Arguments:
    YEAR        Year of birth, e.g. 1980
    MONTH       Month of birth, e.g. 01
    DAY         Day of birth, e.g. 20
    GENDER      Gender, Male or Female
    NUMBER      National number, for validation
"""

import sys
from docopt import docopt
from app.nrn_generators import *


def main():
    args = docopt(__doc__, version='0.0.1')

    if args['--be'] and args['--generate']:
        gen = NrnBelgiumGenerateFromDate(args['<YEAR>'], args['<MONTH>'], args['<DAY>'], args['<GENDER>'])
        print(gen.nrn)

    if args['--be'] and args['--isvalid']:
        validator = NrnBelgiumValidator(args['<NUMBER>'])
        print(validator.isValid)


if __name__ == '__main__':
    main()

