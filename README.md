# diffsquare-py

A Python implementation of **Fermat's Difference of Squares Factorization**.
This is the Python counterpart to the Rust crate [`diffsquare`](https://crates.io/crates/diffsquare).

## Features

* Factors integers efficiently using Fermat's method.
* Supports large integers up to \~64 bits practically.
* Optional verbose output showing approximate factors in scientific notation.
* Configurable precision and iteration print interval for verbose output.
* Suppress verbose output with `--quiet`.

## Installation

Clone the repository:

```bash
git clone https://github.com/Abhrankan-Chakrabarti/diffsquare-py.git
cd diffsquare-py
```

Requires Python 3 and [`gmpy2`](https://pypi.org/project/gmpy2/):

```bash
pip install gmpy2
```

## Usage

Factor a number via stdin:

```bash
echo 5959 | python factor.py
```

Or using the `-n` argument:

```bash
python factor.py -n 5959
```

Suppress verbose progress:

```bash
python factor.py -n 5959 --quiet
```

Set scientific notation precision (default is 30):

```bash
python factor.py -n 5959 -p 6
```

Set iteration print interval (default is 1,000,000):

```bash
python factor.py -n 5959 -i 100000
```
