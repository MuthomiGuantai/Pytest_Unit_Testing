import math_func
import pytest
from math_func import StudentDB


@pytest.mark.number
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7


@pytest.mark.skip(reason="do not run number")
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

@pytest.mark.parametrize('num1, num2, result',[
    (7, 3, 10),
    ('Hello', 'World', 'HelloWorld'),
    (10.5, 25.5, 36)
])
def test_add_All(num1, num2, result):
    assert math_func.add(num1, num2) == result

@pytest.fixture(scope='module')
def db():
    print('----------setup----------------')
    db = StudentDB()
    db.connect('data.json')
    yield db
    print('----------teardown----------------')
    db.close()

def test_scott_data(db):
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'

def test_mark_data(db):
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'
  