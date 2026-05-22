# MPC-lab

MPC-lab is a small educational Python project that implements core building blocks of secure multi-party computation (MPC) from scratch.

The project focuses on the mechanics behind secret sharing and arithmetic over secret-shared values rather than production-grade cryptography. It is intended as a readable lab for understanding how private values can be split into shares, processed, and reconstructed only when the protocol allows it.

The implementation assumes a semi-honest setting and is intended for educational experiments only.

## Features

- Finite field arithmetic over a prime modulus `p`
- Additive secret sharing
- Shamir secret sharing with Lagrange interpolation
- Beaver triples for multiplication of additively shared values
- Secure aggregation demo for sum and average computation
- Unit tests for core primitives

## Project Structure

```text
mpc-lab/
  README.md
  src/
    finite_field.py
    additive_sharing.py
    shamir.py
    beaver.py
    secure_aggregation.py
  tests/
  examples/
    secure_sum_demo.py
```

## Implemented Primitives

### Finite Field Arithmetic

All arithmetic is performed modulo a prime number `p`. The module includes addition, subtraction, multiplication, modular inverse, division, primality checks, and normalization.

### Additive Secret Sharing

A secret `s` is split into `n` shares:

```text
s = share_1 + share_2 + ... + share_n mod p
```

This scheme is simple and useful for secure aggregation, where sums can be computed directly over shares.

### Shamir Secret Sharing

Shamir sharing uses a random polynomial where the secret is stored as the constant term:

```text
f(0) = secret
```

Shares are points on the polynomial. Any `t` shares can reconstruct the secret via Lagrange interpolation.

### Beaver Triples

Beaver triples enable multiplication of secret-shared values. Given a preprocessed triple:

```text
c = a * b mod p
```

the protocol can compute shares of `x * y` without opening `x` or `y`.

### Secure Aggregation

The aggregation module demonstrates how multiple private values can be summed or averaged using additive shares. Individual inputs are split into shares, aggregation is performed over shares, and only the final aggregate is reconstructed.

## Running the Demo

```bash
PYTHONPATH=src python3 examples/secure_sum_demo.py
```

## Running Tests

Install `pytest` if needed:

```bash
python3 -m pip install pytest
```

Run the test suite:

```bash
PYTHONPATH=src python3 -m pytest
```

## Notes

This repository is for learning and experimentation. It does not implement network communication, malicious-party security, authenticated shares, constant-time implementations, secure randomness, or production-ready parameter selection.
