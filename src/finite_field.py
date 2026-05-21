def add(a: int, b: int, p: int) -> int:
    return (a + b) % p


def sub(a: int, b: int, p: int) -> int:
    return (a - b) % p


def mul(a: int, b: int, p: int) -> int:
    return (a * b) % p


def inv(a: int, p: int) -> int:
    return pow(a, -1, p)


def div(a: int, b: int, p: int) -> int:
    return mul(a, inv(b, p)) % p


def is_prime(p: int) -> bool:
    pass


def normalize(a: int, p: int) -> int:
    return a % p
