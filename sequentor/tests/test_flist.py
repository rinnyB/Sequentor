# ignore E731
import pytest
from sequentor.flist import FList
from sequentor.flist_errors import MapError

"""
Test that FList is initialized successfully
for different input types: a single list
and a various arguments list
"""


class Test_FlistInit:
    def test_FList_init_list(self):
        data = [1, 2, 3, 4, 5]
        assert FList(data) == data

    def test_FList_init_args(self):
        data = [1, 2, 3, 4, 5]
        assert FList(*data) == data

    def test_FList_init_list_tuples(self):
        data = [(1, 2), (3, 4), (5, 6)]
        assert FList(data) == data

    def test_FList_init_tuple(self):
        data = (1, 2, 3, 4, 5)
        assert(FList(data) == list(data))

    def test_FList_init_from_map(self):
        data = [1, 2, 3, 4, 5]
        awaited = [2, 3, 4, 5, 6]
        func = lambda x: x + 1
        assert(FList(map(func, data)) == awaited)

    def test_FList_init_from_filter(self):
        data = [1, 2, 3, 4, 5]
        awaited = [1, 2]
        func = lambda x: x < 3
        assert(FList(filter(func, data)) == awaited)


class Test_FListMap:
    def test_FList_map(self):
        data = [1, 2, 3, 4, 5]
        awaited = [0.5, 1, 1.5, 2, 2.5]
        func = lambda x: x / 2
        assert (FList(data).map(func) == awaited)

    def test_FList_map_raise_exception(self):
        data = [1, 2, 3, 4, 5]
        # use inappropriate function
        func = lambda x: x.lower()
        with pytest.raises(MapError):
            FList(data).map(func)
