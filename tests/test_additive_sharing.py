import pytest

from additive_sharing import add_shares, reconstruct_secret, split_secret


P = 2089


def test_split_secret_returns_n_shares_and_reconstructs_secret() -> None:
    secret = 1234
    shares = split_secret(secret, n=5, p=P)

    assert len(shares) == 5
    assert reconstruct_secret(shares, P) == secret


def test_split_secret_normalizes_secret_mod_p() -> None:
    shares = split_secret(P + 42, n=4, p=P)

    assert reconstruct_secret(shares, P) == 42


def test_add_shares_adds_two_shared_values() -> None:
    secret_a = 500
    secret_b = 1700
    shares_a = split_secret(secret_a, n=5, p=P)
    shares_b = split_secret(secret_b, n=5, p=P)

    summed_shares = add_shares(shares_a, shares_b, P)

    assert reconstruct_secret(summed_shares, P) == (secret_a + secret_b) % P


def test_add_shares_rejects_different_lengths() -> None:
    with pytest.raises(ValueError):
        add_shares([1, 2], [1], P)
