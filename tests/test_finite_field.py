import pytest

from finite_field import add, div, inv, is_prime, mul, normalize, sub


P = 17


def test_basic_field_operations_are_modulo_p() -> None:
    assert add(14, 8, P) == 5
    assert sub(3, 8, P) == 12
    assert mul(5, 4, P) == 3
    assert normalize(-1, P) == 16


def test_inverse_and_division() -> None:
    assert inv(5, P) == 7
    assert mul(5, inv(5, P), P) == 1
    assert div(6, 3, P) == 2


def test_zero_has_no_inverse() -> None:
    with pytest.raises(ValueError):
        inv(0, P)


def test_is_prime() -> None:
    assert is_prime(2)
    assert is_prime(17)
    assert is_prime(2089)
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(21)
