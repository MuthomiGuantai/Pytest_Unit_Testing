import math_func
import pytest


@pytest.mark.number
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7


@pytest.mark.number
def test_product():
    assert math_func.product(7, 2) == 14
    assert math_func.product(5) == 10
    assert math_func.product(4) == 8


@pytest.mark.string
def test_add_strings():
    result = math_func.add('Hello', 'world')
    assert result == 'Helloworld'
    assert type(result) is str
    assert 'Heldo' not in result


@pytest.mark.string
def test_product_strings():
    assert math_func.product('H ', 3) == 'H H H '
    result = math_func.product('H ')
    assert result == 'H H '
    assert type(result) is str
    assert 'H' in result
