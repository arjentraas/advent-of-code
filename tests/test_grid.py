from utils import Grid, Position


def test_move_position():
    g = Grid()
    g.empty_grid(col_count=7, row_count=7)

    new_pos = g.move_position(Position(2, 4), 2, -3)
    assert new_pos == Position(4, 1)


def test_move_position_with_teleport_from_up():
    g = Grid().empty_grid(col_count=7, row_count=7)
    new_pos = g.move_position(Position(4, 1), 2, -3, teleport=True)
    assert new_pos == Position(6, 5)


def test_move_position_with_teleport_left():
    g = Grid().empty_grid(col_count=11, row_count=7)
    new_pos = g.move_position(Position(10, 6), 2, -3, teleport=True)
    assert new_pos == Position(1, 3)


def test_move_position_with_teleport_down():
    g = Grid().empty_grid(col_count=11, row_count=7)
    new_pos = g.move_position(Position(10, 6), 2, 3, teleport=True)
    assert new_pos == Position(1, 2)
