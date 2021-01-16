"""National Register Number generator, CLI version.

Usage:
    nrn_cli.py --be <YEAR> <MONTH> <DAY> <GENDER>
    nrn_cli.py [-h | --help]
    nrn_cli.py [--version]

Options:
    -h --help   Show this screen
    --version   Show Version
    --be        Belgium

Arguments:
    YEAR        Year of birth, e.g. 1980
    MONTH       Month of birth, e.g. 01
    DAY         Day of birth, e.g. 20
    GENDER      Gender, Male or Female
"""

import sys
from docopt import docopt
from app.nrn_generators import *


def main():
    args = docopt(__doc__, version='0.0.1')
    gen = NrnBelgiumGenerateFromDate(args['<YEAR>'], args['<MONTH>'], args['<DAY>'], args['<GENDER>'])
    print(gen.nrn)


if __name__ == '__main__':
    main()

