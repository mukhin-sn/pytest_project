import pytest

from utils import arrs


@pytest.fixture
def kit():
    return [1, 2, 3, 4, 5]


def test_get(kit):
    assert arrs.get(kit, 1, "test") == 2
    assert arrs.get(kit, 10, "test") == "test"
    assert arrs.get([], 0, "test") == "test"


def test_slice(kit):
    assert arrs.my_slice(kit, 1, 3) == [2, 3]
    assert arrs.my_slice(kit, 1) == [2, 3, 4, 5]
    assert arrs.my_slice(kit, end=3) == [1, 2, 3]
    assert arrs.my_slice(kit) == [1, 2, 3, 4, 5]
    assert arrs.my_slice(kit, 2, 10) == [3, 4, 5]
    assert arrs.my_slice([]) == []


def test_slice_type_error():
    with pytest.raises(TypeError):
        arrs.my_slice(1259, 2, 3)
