import pytest

"""
def test_example():
    # 使用 assert
    assert True
    assert False

    # 使用 pytest.raises
    with pytest.raises(ZeroDivisionError):
        x = 1 / 0

    # 使用 pytest.approx
    assert 3.14159265359 == pytest.approx(3.14, abs=1e-2)

    # 使用 pytest.mark
    @pytest.mark.skip
    def test_skip():
        pass

    @pytest.mark.xfail
    def test_xfail():
        assert False

    @pytest.mark.xfail(reason="这个测试用例预期会失败")
    def test_xfail_with_reason():
        assert False
"""

from example01 import seq_search, bin_search


@pytest.fixture
def data1():
    return [35, 97, 12, 68, 55, 73, 81, 40]

@pytest.fixture
def data2():
    return [12, 35, 40, 55, 68, 73, 81, 97]

def test_seq_search(data1):
    """测试顺序查找"""
    assert seq_search(data1, 35) == 0
    assert seq_search(data1, 12) == 2
    assert seq_search(data1, 81) == 6
    assert seq_search(data1, 40) == 7
    assert seq_search(data1, 99) == -1
    assert seq_search(data1, 7) == -1

def test_bin_search(data2):
    """测试二分查找"""
    assert bin_search(data2, 35) == 1
    assert bin_search(data2, 12) == 0
    assert bin_search(data2, 81) == 6
    assert bin_search(data2, 40) == 2
    assert bin_search(data2, 97) == 7
    assert bin_search(data2, 7) == -1
    assert bin_search(data2, 99) == -1
