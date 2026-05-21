from itertools import combinations

from shamir import evaluate_polynomial, reconstruct_secret, split_secret


P = 2089


def test_evaluate_polynomial() -> None:
    coefficients = [10, 3, 4]

    assert evaluate_polynomial(coefficients, x=0, p=17) == 10
    assert evaluate_polynomial(coefficients, x=2, p=17) == 15


def test_split_secret_returns_n_points_without_x_zero() -> None:
    shares = split_secret(secret=1234, t=3, n=5, p=P)

    assert len(shares) == 5
    assert [x for x, _ in shares] == [1, 2, 3, 4, 5]


def test_reconstruct_secret_from_any_threshold_shares() -> None:
    secret = 1234
    threshold = 3
    shares = split_secret(secret=secret, t=threshold, n=5, p=P)

    for subset in combinations(shares, threshold):
        assert reconstruct_secret(list(subset), P) == secret
