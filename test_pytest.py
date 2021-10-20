
from mars_rover_task2_class import MarsRover


def test__init__():
    mars_rover = MarsRover(plateau_width=5, plateau_height=5, x=1, y=2, direction='N')
    assert "N" == mars_rover.direction
    assert 1 == mars_rover.x
    assert 2 == mars_rover.y
    assert 5 == mars_rover.plateau_height


def test_method_check_print_final_output():
    mars_rover = MarsRover(plateau_width=5, plateau_height=5, x=5, y=2, direction='W')
    expected_result = "Rover final coordinates: 3 3 S"
    output = [[3, 3, "S"]]
    assert expected_result == mars_rover.print_final_output(output)


def test_rover_move_method_working_correct():
    mars_rover = MarsRover(plateau_width=5, plateau_height=5, x=1, y=2, direction='N')
    mars_rover.rover_move("M")
    expected_result = '1' + ' ' + '3'
    actual_result = f"{mars_rover.x} {mars_rover.y}"
    assert expected_result == actual_result


def test_rover_move_method_not_working_correct():
    mars_rover = MarsRover(plateau_width=5, plateau_height=5, x=1, y=2, direction='N')
    mars_rover.rover_move("F")
    expected_result = '1' + ' ' + '2'
    actual_result = f"{mars_rover.x} {mars_rover.y}"
    assert expected_result == actual_result


def test_input_with_invalid_direction():
    mars_rover = MarsRover(plateau_width=5, plateau_height=5, x=1, y=2, direction="G")
    expected_result = "Chosen direction: G not correct! Please chose from: N, E, W, S"
    actual_result = f"Chosen direction: {mars_rover.direction} not correct! Please chose from: N, E, W, S"
    assert expected_result == actual_result


def test_right_rotation_working_correct():
    mars_rover = MarsRover(plateau_width=5, plateau_height=5, x=1, y=2, direction='N')
    expected_result = "W"
    mars_rover.left_rotate()
    assert expected_result == mars_rover.direction


def test_left_rotation_working_correct():
    mars_rover = MarsRover(plateau_width=5, plateau_height=5, x=1, y=2, direction='N')
    expected_result = "E"
    mars_rover.right_rotate()
    assert expected_result == mars_rover.direction


def test_if_method_return_rover_to_previous_position_is_working_correct():
    mars_rover = MarsRover(plateau_width=5, plateau_height=5, x=2, y=2, direction='W')
    mars_rover.rover_move("M")
    mars_rover.return_rover_to_previous_position()
    expected_result = '2' + ' ' + '2'
    actual_result = f"{mars_rover.x} {mars_rover.y}"
    assert expected_result == actual_result
