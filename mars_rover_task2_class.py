from collections import deque


class MarsRover:
    RIGHT_ROTATION_DICT = {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N'
    }

    LEFT_ROTATION_DICT = {
        'N': 'W',
        'W': 'S',
        'S': 'E',
        'E': 'N'
    }

    POSSIBLE_DIRECTIONS = ["N", "E", "S", "W"]

    def __init__(self, plateau_width: int, plateau_height: int, x: int, y: int, direction: str):
        self.plateau_width = plateau_width + 1
        self.plateau_height = plateau_height + 1
        self.x = x
        self.y = y
        self.direction = direction
        self.move = ""

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value <= 0 or value > self.plateau_width:
            raise ValueError(f"X must be more than 0 and less then plateau width: {self.plateau_width}")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value <= 0 or value > self.plateau_height:
            raise ValueError(f"Y must be more than 0 and less than plateau height: {self.plateau_height}")
        self.__y = value

    def rover_move(self, move):
        if move == "M":
            if self.direction == "N":
                self.y += 1
            elif self.direction == "E":
                self.x += 1
            elif self.direction == "W":
                self.x -= 1
            elif self.direction == "S":
                self.y -= 1

    def return_rover_to_previous_position(self):
        if self.direction == "N":
            self.y -= 1
        elif self.direction == "S":
            self.y += 1
        elif self.direction == "E":
            self.x -= 1
        elif self.direction == "W":
            self.x += 1

    def left_rotate(self):
        self.direction = self.LEFT_ROTATION_DICT[self.direction]

    def right_rotate(self):
        self.direction = self.RIGHT_ROTATION_DICT[self.direction]

    @staticmethod
    def print_final_output(output):
        return f"Rover final coordinates: {output[0][0]} {output[0][1]} {output[0][2]}"


def main():
    def check_valid_coordinates(x, y, width, height):
        if (0 <= x < width) and (0 <= y < height):
            return True
        return False

    plateau_width = int(input("Please insert plateau width:"))
    plateau_height = int(input("Please insert plateau height:"))

    # TODO Please use only one of the moves lists/arrays provided at a time and put a comment on the others, while you are testing the code!

    '''
    Please use only one of the moves lists/arrays provided at a time and put a comment on the others, while you are testing the code!
    '''
    # moves = ["LMLMLMLMM", "MMRMMRMRRM"]
    # moves = ['RMMMLMMLMM', 'MMRMMRMRRM']
    moves = ['RMMMLMMLMM', 'MMRMMRMRRM']
    # moves = ["MMRMMRMRRM"]
    # moves = ['MMRMM', 'MMRMMRMRRM']
    # moves = ["MMRMMRMRRM"]
    # moves = ["LLLMMMLMMLMLM"]

    moves = deque(moves)
    final_output = []

    while moves:
        x_coordinate = int(input("Please insert the X coordinate:"))
        y_coordinate = int(input("Please insert the Y coordinate:"))

        if not check_valid_coordinates(x_coordinate, y_coordinate, plateau_width, plateau_height):
            print(
                "The chosen coordinates are out of the plateau field." + '\n' f"Please choose X less than "                                                                         f"{plateau_width} and Y less than {plateau_height}")
            continue

        direction = input("Please insert direction from: N, W, E, S")

        while direction not in MarsRover.POSSIBLE_DIRECTIONS:
            direction = input("Please insert direction from: N, W, E, S")

        mars_rover = MarsRover(plateau_width, plateau_height, x_coordinate, y_coordinate, direction)
        current_moves = moves.popleft()
        for move in current_moves:
            if move == "M":
                mars_rover.rover_move(move)
            elif move == "L":
                mars_rover.left_rotate()
            elif move == "R":
                mars_rover.right_rotate()
            if not check_valid_coordinates(mars_rover.x, mars_rover.y, plateau_width, plateau_height):
                mars_rover.return_rover_to_previous_position()

        final_output.append([mars_rover.x, mars_rover.y, mars_rover.direction])
        print(mars_rover.print_final_output(final_output))
        final_output = []


if __name__ == '__main__':
    main()
