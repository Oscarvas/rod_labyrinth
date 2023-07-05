from src.main import can_rotate, exit_reached, is_valid_move, labyrinth_len

labyrinth = [
    [".",".","."],
    [".",".","."],
    [".",".","."]
]

def test_can_rotate_ok():
    assert can_rotate(labyrinth, 1, 1) == True

def test_can_rotate_ko():
    assert not can_rotate(labyrinth, 0, 1) == True

def test_exit_reached_horizontal():
    assert exit_reached(labyrinth, 2, 1, True) == True

def test_exit_reached_horizontal_ko():
    assert not exit_reached(labyrinth, 1, 1, True) == True

def test_exit_reached_vertical():
    assert exit_reached(labyrinth, 1, 2, False) == True

def test_exit_reached_vertical_ko():
    assert not exit_reached(labyrinth, 1, 1, False) == True

def test_labirynth_len_horizontal():
    labyrinth = [
        [".",".","."],
        [".",".","."],
        [".",".","."],
        [".",".","."]
    ]
    
    assert labyrinth_len(labyrinth, True) == 3

def test_labirynth_len_vertical():
    labyrinth = [
        [".",".","."],
        [".",".","."],
        [".",".","."],
        [".",".","."]
    ]
    
    assert labyrinth_len(labyrinth, False) == 4

def test_is_valid_move_horizontal_up():
    assert is_valid_move(labyrinth, 0, 1, True) == True

def test_is_valid_move_horizontal_down():
    assert is_valid_move(labyrinth, 2, 1, True) == True

def test_is_valid_move_horizontal_right_ko():
    assert not is_valid_move(labyrinth, 0, 2, True) == True

def test_is_valid_move_vertical_up():
    assert is_valid_move(labyrinth, 1, 1, True) == True

def test_is_valid_move_vertical_up_ko():
    assert not is_valid_move(labyrinth, 1, 0, True) == True