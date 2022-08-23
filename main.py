def get_footer(current_page, total_pages, boundaries, around):
    assert current_page > 0, "Current page number should not be less then 1"
    assert total_pages > 0, "Total pages number should not be less then 1"
    assert boundaries > 0, "Boundaries number should not be less then 1"
    assert around >= 0, "Around number should not be less then 0"

    if current_page > total_pages:
        raise AssertionError("Current page is bigger then the total pages number.")

    if boundaries >= total_pages / 2:
        footer = range(1, total_pages + 1)
        return serialize_footer_to_output(footer)

    footer_begin_limit_value = boundaries + 1
    footer_begin_values = list(range(1, footer_begin_limit_value))

    footer_end_first_value = total_pages - boundaries + 1
    footer_end_values = list(range(footer_end_first_value, total_pages + 1))

    footer_middle_first_value = (
        footer_begin_limit_value
        if current_page - around < footer_begin_limit_value
        else current_page - around
    )
    footer_middle_limit_value = (
        footer_end_first_value
        if current_page + around + 1 > footer_end_first_value
        else current_page + around + 1
    )
    footer_middle_values = list(
        range(footer_middle_first_value, footer_middle_limit_value)
    )

    footer = concat_footer_values(
        footer_begin_values, footer_middle_values, footer_end_values
    )

    return serialize_footer_to_output(footer)


def serialize_footer_to_output(footer_values):
    return " ".join([str(value) for value in footer_values])


def concat_footer_values(footer_begin_values, footer_middle_values, footer_end_values):
    if footer_middle_values:
        if footer_begin_values[-1] != footer_middle_values[0] - 1:
            footer_begin_values.append("...")

        if footer_middle_values[-1] != footer_end_values[0] - 1:
            footer_middle_values.append("...")
    else:
        if footer_begin_values[-1] != footer_end_values[0] - 1:
            footer_begin_values.append("...")

    footer_values = (
        list(footer_begin_values) + list(footer_middle_values) + list(footer_end_values)
    )

    return footer_values


if __name__ == "__main__":
    print(
        "Inform the current page, total pages, boundaries and around number respectively separated by a white space"
    )
    while True:
        try:
            a, b, c, d = [int(number) for number in input().split()]
            footer = get_footer(a, b, c, d)
        except ValueError:
            print("Invalid input!")
            continue
        except AssertionError as e:
            print(e)
            continue
        print(f"Footer: {footer}")
