import random


def evaluate_polynomial(coefficients: list[int], x: int, p: int) -> int:
    res = 0
    for i in range(len(coefficients)):
        res += coefficients[i] * (x ** i)

    return res % p


def split_secret(secret: int, t: int, n: int, p: int) -> list[tuple[int, int]]:
    coefficients = [secret] + [random.randint(0, p - 1) for _ in range(t - 1)]
    shares = [(0, 0)] * n
    for x in range(0, n):
        shares[x] = (x + 1, evaluate_polynomial(coefficients, x + 1, p))

    return shares


def reconstruct_secret(shares: list[tuple[int, int]], p: int) -> int:
    secret = 0
    for i in range(len(shares)):
        xi, yi = shares[i]
        numerator = 1
        denominator = 1

        for j in range(len(shares)):
            if i == j:
                continue
            xj, _ = shares[j]
            numerator = (numerator * (-xj)) % p
            denominator = (denominator * (xi - xj)) % p

        lagrange_basis = numerator * pow(denominator, -1, p)
        secret = (secret + yi * lagrange_basis) % p

    return secret
