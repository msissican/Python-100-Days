from example02 import select_sort, merge
import pytest


@pytest.fixture
def data1():
    return [35, 97, 12, 68, 55, 73, 81, 40]

@pytest.fixture
def items1():
    return [12, 35, 68, 97]

@pytest.fixture
def items2():
    return [40, 55, 73, 81]

def test_merge(items1, items2):
    items = merge(items1, items2)
    for i in range(len(items) - 1):
        assert items[i] <= items[i + 1]

def test_select_sort(data1):
    items = select_sort(data1)
    for i in range(len(items) - 1):
        assert items[i] <= items[i + 1]
