import pytest

from main import get_footer


@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected_footer",
    [
        (4, 5, 1, 0, "1 ... 4 5"),
        (4, 10, 2, 2, "1 2 3 4 5 6 ... 9 10"),
        (5, 10, 2, 0, "1 2 ... 5 ... 9 10"),
    ],
)
def test_should_return_footer_with_three_points(
    current_page, total_pages, boundaries, around, expected_footer
):
    footer = get_footer(current_page, total_pages, boundaries, around)

    assert footer == expected_footer


@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected_footer",
    [
        (1, 5, 1, 0, "1 ... 5"),
        (10, 10, 1, 0, "1 ... 10"),
        (10, 10, 1, 2, "1 ... 8 9 10"),
        (1, 10, 2, 0, "1 2 ... 9 10"),
    ],
)
def test_should_return_footer_with_first_and_last_values(
    current_page, total_pages, boundaries, around, expected_footer
):
    footer = get_footer(current_page, total_pages, boundaries, around)

    assert footer == expected_footer


@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected_footer",
    [
        (1, 5, 5, 0, "1 2 3 4 5"),
        (3, 5, 1, 4, "1 2 3 4 5"),
        (1, 11, 6, 0, "1 2 3 4 5 6 7 8 9 10 11"),
        (6, 11, 5, 0, "1 2 3 4 5 6 7 8 9 10 11"),
    ],
)
def test_should_return_footer_with_all_values(
    current_page, total_pages, boundaries, around, expected_footer
):
    footer = get_footer(current_page, total_pages, boundaries, around)

    assert footer == expected_footer


@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, error_message",
    [
        (0, 5, 1, 0, "Current page number should not be less then 1"),
        (4, 0, 1, 0, "Total pages number should not be less then 1"),
        (4, 5, 0, 0, "Boundaries number should not be less then 1"),
        (4, 5, 1, -1, "Around number should not be less then 0"),
        (6, 5, 1, 0, "Current page is bigger then the total pages number."),
    ],
)
def test_should_raise_error(
    current_page, total_pages, boundaries, around, error_message
):

    with pytest.raises(AssertionError) as exc_info:
        get_footer(current_page, total_pages, boundaries, around)

    assert str(exc_info.value) == error_message
