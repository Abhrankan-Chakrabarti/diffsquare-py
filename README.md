# diffsquare-py

Python implementation of Fermat's Difference of Squares factorization algorithm. This is the Python equivalent of the Rust `diffsquare` crate.

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/Abhrankan-Chakrabarti/diffsquare-py.git
cd diffsquare-py
pip install -r requirements.txt
```

Dependencies:

* `gmpy2`

## Usage

Factor an RSA modulus:

```bash
echo 10546581863473198687 | python factor.py
```

Or specify with `-n`:

```bash
python factor.py -n 10546581863473198687
```

### Options

* `-n, --mod`   Modulus to factor (decimal or hex with 0x)
* `-q, --quiet` Suppress progress output
* `-p, --prec`  Digits to show for approximate factors (default=30)
* `-i, --interval` Print interval for progress (default=1e6)

## Examples

### Example 1: Default precision (`--prec=30`)

```bash
$ echo 10546581863473198687 | python factor.py
Iteration: 86000000 p ≈ 2581237283 q ≈ 4085862983

✅ Factors of 10546581863473198687:
p = 2578536577
q = 4090142431
Iterations = 86789371
⏱️  Execution time: 103.220617 seconds
```

Since both `p` and `q` are under 30 digits, they are shown in full decimal form.

---

### Example 2: Reduced precision (`--prec=6`)

```bash
$ echo 10546581863473198687 | python factor.py -p 6
Iteration: 86000000 p ≈ 2.581237e+09 q ≈ 4.085863e+09

✅ Factors of 10546581863473198687:
p = 2578536577
q = 4090142431
Iterations = 86789371
⏱️  Execution time: 103.220617 seconds
```

With precision limited to 6 digits, the intermediate approximations are shown in scientific notation.

---

## License

MIT
