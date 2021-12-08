
<div align="center">
  National Registry Number
  <br />
</div>



---

## About


> National Number Generator is a command line tool to help generate valid national numbers.
> Currently, this tool works for Belgian numbers only.
> The goal is to simplify the creation of test accounts for development purposes.

> Important: The national numbers are only valid from a purely mathematical standpoint and will pass a simple computation check.
> They are NOT valid from the national registry database standpoint, and will fail all legal checks obviously.

> Other countries may be added at a later date.

<details>
<summary>Screenshots</summary>
<br>

<img src="docs/images/nrn.png" title="Home Page" width="100%">

</details>

### Built With

> Python 3

## Getting Started

### Prerequisites

> docopt

### Installation

> git clone this project

> pip3 install docopt

## Usage

> Let's say you want to generate a national number for a female person born the 30th of January 1980:

> python3 nrn_cli.py --be --generate 1980 01 30 FEMALE

> Display help: 

> python3 nrn_cli.py -h


## License

This project is licensed under the **GNU General Public License v3**.

See [LICENSE](LICENSE) for more information.

