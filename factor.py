#!/usr/bin/env python3
import sys
import time
import argparse
from gmpy2 import mpz, isqrt, is_square

def to_sci(n, prec=30):
    """
    Convert integer n to scientific notation string with `prec` digits after decimal.
    Only converts if number has more digits than `prec`.
    Example: to_sci(123456789, prec=6) -> "1.234568e+08"
    """
    n = mpz(n)
    s = str(n)

    # If number fits within precision, return full string
    if len(s) <= prec:
        return s

    neg = n < 0
    if neg:
        n = -n
        s = str(n)

    exp = len(s) - 1
    sig_len = 1 + prec  # 1 digit before decimal + `prec` after

    extended = s if len(s) > sig_len else s + ("0" * (sig_len + 1 - len(s)))
    sig = extended[:sig_len]
    next_digit = extended[sig_len] if len(extended) > sig_len else "0"

    mant_int = int(sig)

    # Round if needed
    if next_digit >= "5":
        mant_int += 1
        if mant_int >= 10 ** sig_len:
            mant_int //= 10
            exp += 1

    mant_str = str(mant_int).rjust(sig_len, "0")
    mantissa = mant_str[0] + "." + mant_str[1:]  # prec digits after decimal
    exp_str = f"{exp:+02d}"
    sign = "-" if neg else ""
    return f"{sign}{mantissa}e{exp_str}"

def predict_factor(N, quiet=False, prec=30, print_interval=1000000):
    N = mpz(N)
    y0 = isqrt(N)
    if y0 * y0 < N:
        y0 += 1

    D = y0 * y0 - N
    k = 0
    while True:
        if is_square(D):
            x = isqrt(D)
            y = y0 + k
            p = y - x
            q = y + x
            if p * q == N:
                return p, q, k

        if not quiet and k % print_interval == 0 and k > 0:
            y = y0 + k
            approx_x = isqrt(D)
            approx_p = y - approx_x
            approx_q = y + approx_x
            print(
                f"Iteration: {k} p ≈ {to_sci(approx_p, prec)} q ≈ {to_sci(approx_q, prec)}",
                end="\r",
                flush=True,
            )

        k += 1
        D += 2 * y0 + 2 * k - 1

def main():
    parser = argparse.ArgumentParser(description="Fermat's Difference of Squares Factorization (Python)")
    parser.add_argument("-n", "--mod", type=str, help="Modulus to factor (decimal or hex with 0x)", required=False)
    parser.add_argument("-q", "--quiet", action="store_true", help="Suppress progress output")
    parser.add_argument("-p", "--prec", type=int, default=30, help="Digits to show for approximate factors (default=30)")
    parser.add_argument("-i", "--interval", type=int, default=1000000, help="Print interval for progress (default=1e6)")
    args = parser.parse_args()

    if args.mod:
        data = args.mod.strip()
    else:
        data = sys.stdin.read().strip()

    if not data:
        print("Usage: echo <modulus> | python factor.py OR python factor.py -n <modulus>")
        sys.exit(1)

    if data.startswith("0x") or data.startswith("0X"):
        N = mpz(int(data, 16))
    else:
        N = mpz(data)

    start = time.perf_counter()
    p, q, k = predict_factor(N, quiet=args.quiet, prec=args.prec, print_interval=args.interval)
    end = time.perf_counter()

    print(f"\n✅ Factors of {N}:")
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"Iterations = {k}")
    print(f"⏱️  Execution time: {end - start:.6f} seconds")

if __name__ == "__main__":
    main()
