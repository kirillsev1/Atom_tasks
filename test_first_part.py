import pytest
from typing import Callable
from third import count_tags, count_tags_attrs
from second import square, create_handlers
from fifth import comparison

test_third_list = [
    ('https://www.google.com/', 163, 265),
    ('https://testometrika.com/tests/', 407, 734)
]

test_fifth_list = [
    ('1.01.', '2.1', -1),
    ('10.', '0.1', 1),
    ('1.1.', '1.1.0', 0),
    ('1.', '1.0.0.0', 0),
    ('0.1', '0.0.1', 1)
]

test_add_one = [(1, 1), (-1, 1), (10, 100), (5, 25)]
test_create_handlers = [
    ([0, 1, 4, 9, 16], True), ([1, 0, 1, 4, 9], False), ([4, 9, 16, 25], False), ([25, 36, 49, 64], False)
]


@pytest.mark.parametrize("number, result", test_add_one)
def test_check_add_one(number: int, result: int) -> None:
    """Test square function.

    Args:
        number: int - input data.
        result: int - the result of the function.
    """
    assert square(number) == result


@pytest.mark.parametrize("result, expect", test_create_handlers)
def test_check_create_handlers(result: list, expect: bool) -> None:
    """Test for create handlers.

    Args:
        result: list - the result after executing.
        expect: bool - what we expect.
    """
    temp_list = [function() for function in create_handlers(square)] == result
    assert temp_list == expect


@pytest.mark.parametrize('url, first_func_res, second_func_res', test_third_list)
def test_third_file(url: str, first_func_res: int, second_func_res: int) -> None:
    """Test find tags function and find attrs of tags function.

    Args:
        url: str - url on html page.
        first_func_res: Callable - function which finds number of tags.
        second_func_res: Callable - function which finds number of attrs in tags even if it is None.
    """
    assert count_tags(url) == first_func_res
    assert count_tags_attrs(url) == second_func_res


@pytest.mark.parametrize('version_1, version_2, result', test_fifth_list)
def test_fifth_file(version_1: str, version_2: str, result: int) -> None:
    """Test checking version function.

    Args:
        version_1: str - comparable version.
        version_2: str - needful version.
        result: int - if version is equal: 0, if version_a older: -1, if version_b older: 1.
    """
    assert comparison(version_1, version_2) == result
