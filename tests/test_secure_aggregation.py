import pytest

from secure_aggregation import secure_average, secure_sum


P = 2089


def test_secure_sum() -> None:
    values = [10, 20, 30, 40]

    assert secure_sum(values, P) == sum(values)


def test_secure_sum_is_modulo_p() -> None:
    values = [1000, 1200, 50]

    assert secure_sum(values, P) == sum(values) % P


def test_secure_sum_rejects_empty_values() -> None:
    with pytest.raises(ValueError):
        secure_sum([], P)


def test_secure_average() -> None:
    values = [10, 20, 30, 40]

    assert secure_average(values, P) == 25.0
