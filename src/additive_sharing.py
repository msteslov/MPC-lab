import random


def split_secret(secret: int, n: int, p: int) -> list[int]:  # n - число участников, соответственно и число долей,
    # secret принадлежит группе Z_p(аддитивная абелева группа вычетов по модулю p)
    secrets_parts = [random.randint(0, p - 1) for _ in range(n - 1)]
    secrets_parts += [(secret - sum(secrets_parts)) % p]

    return secrets_parts


def reconstruct_secret(shares: list[int], p: int) -> int:
    reconstructed_secret = sum(shares) % p
    return reconstructed_secret


def add_shares(shares_a: list[int], shares_b: list[int], p: int) -> list[int]:
    if len(shares_a) != len(shares_b):
        raise ValueError("shares must have the same length")
    res = []
    for i in range(len(shares_a)):
        res.append((shares_a[i] + shares_b[i]) % p)

    return res
