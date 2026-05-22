import pytest

from additive_sharing import reconstruct_secret, split_secret
from beaver import generate_triple, multiply_shared


P = 2089


def test_generate_triple() -> None:
    a, b, c = generate_triple(P)

    assert 0 <= a < P
    assert 0 <= b < P
    assert c == (a * b) % P


def test_multiply_shared_reconstructs_product() -> None:
    n = 5
    x = 123
    y = 456
    a, b, c = generate_triple(P)

    x_shares = split_secret(x, n, P)
    y_shares = split_secret(y, n, P)
    a_shares = split_secret(a, n, P)
    b_shares = split_secret(b, n, P)
    c_shares = split_secret(c, n, P)

    product_shares = multiply_shared(
        x_shares,
        y_shares,
        a_shares,
        b_shares,
        c_shares,
        P,
    )

    assert reconstruct_secret(product_shares, P) == (x * y) % P


def test_multiply_shared_rejects_different_lengths() -> None:
    with pytest.raises(ValueError):
        multiply_shared([1, 2], [1], [1, 2], [1, 2], [1, 2], P)
