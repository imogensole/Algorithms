import pytest
from algorithms.binary_sort import binary_sort

@pytest.mark.parametrize("list, target, expected", [
    ([1, 2, 3, 4, 5], 3, 2),
    ([1, 2, 3, 4, 5], 6, None),
    ([1, 2, 3, 4, 5], 1, 0),
    ([1, 2, 3, 4, 5], 5, 4),
    ([1, 2, 3, 4, 5], 0, None),
    (["ant", "bat", "cat", "dog", "egg", "fly", "gnu", "hip", "igu", "jam"], "dog", 3),
    (["ant", "bat", "cat", "dog", "egg", "fly", "gnu", "hip", "igu", "jam"], "hip", 7),
    (["ant", "bat", "cat", "dog", "egg", "fly", "gnu", "hip", "igu", "jam"], "igu", 8),
    (["ant", "bat", "cat", "dog", "egg", "fly", "gnu", "hip", "igu", "jam"], "jam", 9),
    (["ant", "bat", "cat", "dog", "egg", "fly", "gnu", "hip", "igu", "jam"], "ant", 0),
    (["ant", "bat", "cat", "dog", "egg", "fly", "gnu", "hip", "igu", "jam"], "bat", 1),
    (["ant", "bat", "cat", "dog", "egg", "fly", "gnu", "hip", "igu", "jam"], "cat", 2),
])
def test_binary_sort(list, target, expected):
    assert binary_sort(list, target) == expected