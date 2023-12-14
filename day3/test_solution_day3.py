import pytest

from day3.solution_day3 import (
    find_adjacent_other_line,
    find_adjacent_same_line,
    find_adjacent_two_asterisks,
    find_asterisk_indeces,
    find_numbers,
    find_symbols_indeces,
    sum_adjacent_numbers,
)


@pytest.mark.parametrize(
    "test_case,symbol_indices",
    [
        ("467..114..", []),
        ("=..*......", [0, 3]),
        ("@.35..633.", [0]),
        ("......#...", [6]),
        ("617*......", [3]),
        ("%....+.58.", [0, 5]),
        ("&.592.....", [0]),
        ("-.....755.", [0]),
        ("#..$.*....", [0, 3, 5]),
        (".664.598/.", [8]),
    ],
)
def test_find_symbols_indeces(test_case, symbol_indices):
    assert find_symbols_indeces(test_case) == symbol_indices


@pytest.mark.parametrize(
    "test_case,output",
    [
        ("467..114..", [467, 114]),
        ("...*......", []),
        ("..35..633.", [35, 633]),
        ("......#...", []),
        ("617*......", [617]),
        (".....+.58.", [58]),
        ("..592.....", [592]),
        ("......755.", [755]),
        ("...$.*....", []),
        (".664.598..", [664, 598]),
        (
            "................*...........*.............$.........*.......205......*135.......................%.....286..............418.............$....",
            [205, 135, 286, 418],
        ),
    ],
)
def test_find_numbers(test_case, output):
    for _match in find_numbers(test_case):
        assert int(_match.group) in output


test_case = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]
expected_result = [467, 35, 633, 617, 592, 755, 664, 598]


def test_find_adjacent_same_line():
    result = find_adjacent_same_line(
        find_numbers(test_case[4]), find_symbols_indeces(test_case[4])
    )
    assert 617 in result

    ex = "................*...........*.............$.........*.......205......*135.......................%.....286..............418.............$...."

    assert 135 in find_adjacent_same_line(
        find_numbers(ex),
        find_symbols_indeces(ex),
    )


def test_find_upper_adjacent():
    result = find_adjacent_other_line(
        find_numbers(test_case[0]), find_symbols_indeces(test_case[1])
    )
    assert 467 in result

    numbers_7 = find_numbers(test_case[7])
    symbols_8 = find_symbols_indeces(test_case[8])

    result = find_adjacent_other_line(numbers_7, symbols_8)
    assert 755 in result


def test_find_lower_adjacent():
    result = find_adjacent_other_line(
        find_numbers(test_case[2]), find_symbols_indeces(test_case[1])
    )
    assert 35 in result


def test_sum_adjacent_numbers():
    assert sum_adjacent_numbers(test_case) == 4361


def test_find_asterisk_indeces():
    assert 3 in find_asterisk_indeces("...*.....")


def test_adjacent_two_asterisks():
    assert find_adjacent_two_asterisks(test_case) == 467835
