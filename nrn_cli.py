"""
National Register Number generator, CLI version.

Usage:
nrn_cli.py (-h | --help)
nrn_cli.py --version

Options:
    -h --help   Show this screen
    --version   Show Version
"""

from docopt import docopt
from app.nrn_generators import *

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
