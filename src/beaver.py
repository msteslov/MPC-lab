import random

from additive_sharing import reconstruct_secret


def generate_triple(p: int) -> tuple[int, int, int]:
    a = random.randint(0, p - 1)
    b = random.randint(0, p - 1)
    c = (a * b) % p

    return a, b, c


def multiply_shared(
    x_shares: list[int],
    y_shares: list[int],
    a_shares: list[int],
    b_shares: list[int],
    c_shares: list[int],
    p: int,
) -> list[int]:
    n = len(x_shares)
    if not (
        len(y_shares)
        == len(a_shares)
        == len(b_shares)
        == len(c_shares)
        == n
    ):
        raise ValueError("all share lists must have the same length")

    d_shares = []
    e_shares = []
    for i in range(n):
        d_shares.append((x_shares[i] - a_shares[i]) % p)
        e_shares.append((y_shares[i] - b_shares[i]) % p)

    d = reconstruct_secret(d_shares, p)
    e = reconstruct_secret(e_shares, p)

    z_shares = []
    for i in range(n):
        z_i = (c_shares[i] + d * b_shares[i] + e * a_shares[i]) % p
        z_shares.append(z_i)

    z_shares[0] = (z_shares[0] + d * e) % p

    return z_shares
