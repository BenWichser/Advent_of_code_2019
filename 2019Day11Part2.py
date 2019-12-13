# Author: Ben Wichser
# Date: 12/11/2019
# Description:  Start at white.  What gets painted?.  see www.adventofcode.com/2019 (day 11) for more information


code_list = [3, 8, 1005, 8, 339, 1106, 0, 11, 0, 0, 0, 104, 1, 104, 0, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4, 10, 1008, 8, 0, 10, 4, 10, 1002, 8, 1, 29, 2, 1108, 11, 10, 1, 1, 20, 10, 2, 107, 6, 10, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4, 10, 108, 0, 8, 10, 4, 10, 101, 0, 8, 62, 1006, 0, 29, 1006, 0, 12, 1, 1101, 5, 10, 1, 2, 20, 10, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 0, 10, 4, 10, 1001, 8, 0, 99, 1006, 0, 30, 3, 8, 1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 0, 10, 4, 10, 1001, 8, 0, 124, 1006, 0, 60, 3, 8, 1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 1, 10, 4, 10, 101, 0, 8, 149, 2, 1007, 2, 10, 1, 1105, 10, 10, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4, 10, 108, 0, 8, 10, 4, 10, 101, 0, 8, 178, 1, 1108, 15, 10, 1, 1101, 5, 10, 1, 109, 8, 10, 1006, 0, 20, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10, 108, 1, 8, 10, 4, 10, 101, 0, 8, 215, 1006, 0, 61, 1006, 0, 16, 2, 1105, 15, 10, 1006, 0, 50, 3, 8, 1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10, 108, 1, 8, 10, 4, 10, 101, 0, 8, 250, 1, 1003, 10, 10, 1, 9, 19, 10, 2, 1004, 6, 10, 2, 1106, 2, 10, 3, 8, 1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 1, 10, 4, 10, 101, 0, 8, 289, 1, 1103, 13, 10, 2, 105, 17, 10, 3, 8, 1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10, 108, 1, 8, 10, 4, 10, 1002, 8, 1, 318, 101, 1, 9, 9, 1007, 9, 1086, 10, 1005, 10, 15, 99, 109, 661, 104, 0, 104, 1, 21101, 0, 825599304340,1, 21101, 356, 0, 0, 1106, 0, 460, 21101, 0, 937108545948, 1, 21102, 1, 367, 0, 1106, 0, 460, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 1, 21102, 1, 21628980315, 1, 21101, 0, 414, 0, 1105, 1, 460, 21101, 0, 3316673539, 1, 21101, 425, 0, 0, 1106, 0, 460, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 0, 21102, 988753428840, 1, 1, 21102, 1, 448, 0, 1106, 0, 460, 21102, 825544569700, 1, 1, 21102, 459, 1, 0, 1106, 0, 460, 99, 109, 2, 21202, -1, 1, 1, 21102, 1, 40, 2, 21102, 491, 1, 3, 21102, 481, 1, 0, 1105, 1, 524, 109, -2, 2106, 0, 0, 0, 1, 0, 0, 1, 109, 2, 3, 10, 204, -1, 1001, 486, 487, 502, 4, 0, 1001, 486, 1, 486, 108, 4, 486, 10, 1006, 10, 518, 1101, 0, 0, 486, 109, -2, 2105, 1, 0, 0, 109, 4, 2102, 1, -1, 523, 1207, -3, 0, 10, 1006, 10, 541, 21102, 0, 1, -3, 21201, -3, 0, 1, 22102, 1, -2, 2, 21102, 1, 1, 3, 21102, 560, 1, 0, 1106, 0, 565, 109, -4, 2105, 1, 0, 109, 5, 1207, -3, 1, 10, 1006, 10, 588, 2207, -4, -2, 10, 1006, 10, 588, 22101, 0, -4, -4, 1105, 1, 656, 21202, -4, 1, 1, 21201, -3, -1, 2, 21202, -2, 2, 3, 21102, 1, 607, 0, 1106, 0, 565, 22102, 1, 1, -4, 21101, 0, 1, -1, 2207, -4, -2, 10, 1006, 10, 626, 21101, 0, 0, -1, 22202, -2, -1, -2, 2107, 0, -3, 10, 1006, 10, 648, 21202, -1, 1, 1, 21101, 0, 648, 0, 105, 1, 523, 21202, -2, -1, -2, 22201, -4, -2, -4, 109, -5, 2105, 1, 0]


def grid_maker(width, height):
    """Accepts width, height (ints).  Returns widthxheight grid with '.' as values."""
    grid = [['.' for i in range(width)] for j in range(height)]
    return grid


def intcode_parse(code):
    """Accepts intcode.  Parses intcode and returns individual parameters. """
    actual_code = code % 100
    parameter_piece = code - actual_code
    parameter_piece = parameter_piece // 100
    parameter_code_list = []

    while parameter_piece > 0:
        parameter_code_list.append(parameter_piece % 10)
        parameter_piece = parameter_piece // 10

    return (actual_code, parameter_code_list)


def parameter_code_sizer(opcode, raw_parameter_code_list):
    """Ensures parameter code list is the correct length, according to the particular opcode."""
    parameter_lengths = {1: 3, 2: 3, 3: 1, 4: 1,
                         5: 2, 6: 2, 7: 3, 8: 3, 9: 1, 99: 0}
    while len(raw_parameter_code_list) < parameter_lengths[opcode]:
        raw_parameter_code_list.append(0)
    return raw_parameter_code_list


def code_list_lengthener(code_list, parameter):
    """Ensures that code_list is long enough to accept an item in its parameter-th location"""
    while len(code_list) < parameter+1:
        code_list.append(0)
    return code_list


def parameter_tuple_maker(parameter_code, code_list, i):
    """
    Accepts parameter_code, code_list, relative_base, and i.
    Returns parameter_code, parameter tuple for opcode operation.
    """

    return (parameter_code, code_list[i])


def parameter_tuple_parser(parameter_tuple, code_list, relative_base):
    """
    Accepts parameter_tuple, code_list, and relative_base.  Returns parameter for use in intcode operation.
    """

    if parameter_tuple[0] == 0:
        code_list_lengthener(code_list, parameter_tuple[1])
        return code_list[parameter_tuple[1]]
    elif parameter_tuple[0] == 1:
        return parameter_tuple[1]
    elif parameter_tuple[0] == 2:
        return code_list[parameter_tuple[1] + relative_base]
    else:
        print('And I oop.... parameter_tuple_parser')


def color_coder(grid, current):
    """Accepts spaceship grid.  Returns 0 if current space is black ('.'), and 1 if current space is white ('.')"""
    if grid[current[0]][current[1]] == '.':
        return 0
    elif grid[current[0]][current[1]] == '#':
        return 1
    else:
        print("And I oop...color_coder")


def intcode_one(parameter_list, code_list, relative_base):
    """Adds elements in the parameter_list's first two elements.  Places sum in parameter_list[2]. Returns True. """
    for i in range(len(parameter_list) - 1):
        parameter_list[i] = parameter_tuple_parser(
            parameter_list[i], code_list, relative_base)

    if parameter_list[-1][0] == 0:
        code_list = code_list_lengthener(code_list, parameter_list[-1][1])
        code_list[parameter_list[-1][1]
                  ] = parameter_list[0] + parameter_list[1]
    elif parameter_list[-1][0] == 2:
        code_list = code_list_lengthener(
            code_list, parameter_list[-1][1]+relative_base)
        code_list[parameter_list[-1][1] +
                  relative_base] = parameter_list[0] + parameter_list[1]
    else:
        print("And I oop... intcode_one")
    return True


def intcode_two(parameter_list, code_list, relative_base):
    """Multiplies elements in the parameter_list's first two elements.  Places product in parameter_list[2]. Returns True. """
    for i in range(len(parameter_list) - 1):
        parameter_list[i] = parameter_tuple_parser(
            parameter_list[i], code_list, relative_base)

    if parameter_list[-1][0] == 0:
        code_list = code_list_lengthener(code_list, parameter_list[-1][1])
        code_list[parameter_list[-1][1]
                  ] = parameter_list[0] * parameter_list[1]
    elif parameter_list[-1][0] == 2:
        code_list = code_list_lengthener(
            code_list, parameter_list[-1][1]+relative_base)
        code_list[parameter_list[-1][1] +
                  relative_base] = parameter_list[0] * parameter_list[1]
    else:
        print("And I oop...intcode_two")
    return True


def intcode_three(parameter_list, code_list, relative_base, grid, current):
    """ Accepts input and places it in parameter_list[0] place in code_list.  Returns True. """
    number_in = color_coder(grid, current)
    if parameter_list[0][0] == 0:
        code_list = code_list_lengthener(code_list, parameter_list[0][1])
        code_list[parameter_list[0][1]] = number_in
    elif parameter_list[0][0] == 2:
        code_list = code_list_lengthener(
            code_list, parameter_list[0][1]+relative_base)
        code_list[parameter_list[0][1] + relative_base] = number_in
    else:
        print("And I oop...intcode_three")
    return True


def intcode_four(parameter_list, code_list, relative_base):
    """ Returns item in parameter_list[0] place in code_list. """
    for i in range(len(parameter_list)):
        parameter_list[i] = parameter_tuple_parser(
            parameter_list[i], code_list, relative_base)

    if parameter_list[-1] not in {0, 1}:
        print("And I oop...intcode_four")
    return parameter_list[-1]


def intcode_five(parameter_list, code_list, relative_base, i):
    """If first parameter is non-zero, sets instruction pointer to second parameter.  Returns i"""
    for j in range(len(parameter_list)):
        parameter_list[j] = parameter_tuple_parser(
            parameter_list[j], code_list, relative_base)
    if parameter_list[0] != 0:
        i = parameter_list[-1]
    return i


def intcode_six(parameter_list, code_list, relative_base,  i):
    """If first parameter is zero, sets instruction pointer to second parameter.  Returns i"""
    for j in range(len(parameter_list)):
        parameter_list[j] = parameter_tuple_parser(
            parameter_list[j], code_list, relative_base)
    if parameter_list[0] == 0:
        i = parameter_list[-1]
    return i


def intcode_seven(parameter_list, code_list, relative_base):
    """If first parameter is less than second parameter, stores 1 in third parameter.  Else stores 0 in third parameter.  Returns True"""
    for i in range(len(parameter_list) - 1):
        parameter_list[i] = parameter_tuple_parser(
            parameter_list[i], code_list, relative_base)
    if parameter_list[-1][0] == 0:
        parameter_list[-1] = parameter_list[-1][1]
    elif parameter_list[-1][0] == 2:
        parameter_list[-1] = parameter_list[-1][1] + relative_base

    if parameter_list[0] < parameter_list[1]:
        code_list = code_list_lengthener(code_list, parameter_list[-1])
        code_list[parameter_list[-1]] = 1
    else:
        code_list = code_list_lengthener(code_list, parameter_list[-1])
        code_list[parameter_list[-1]] = 0
    return True


def intcode_eight(parameter_list, code_list, relative_base):
    """If first parameter is equal to  second parameter, stores 1 in third parameter.  Else stores 0 in third parameter.  Returns True"""
    for i in range(len(parameter_list) - 1):
        parameter_list[i] = parameter_tuple_parser(
            parameter_list[i], code_list, relative_base)
    if parameter_list[-1][0] == 0:
        parameter_list[-1] = parameter_list[-1][1]
    elif parameter_list[-1][0] == 2:
        parameter_list[-1] = parameter_list[-1][1] + relative_base

    if parameter_list[0] == parameter_list[1]:
        code_list = code_list_lengthener(code_list, parameter_list[-1])
        code_list[parameter_list[-1]] = 1
    else:
        code_list = code_list_lengthener(code_list, parameter_list[-1])
        code_list[parameter_list[-1]] = 0
    return True


def intcode_nine(parameter_list, code_list, relative_base):
    """ Adjust the relative base by the first parameter.  Returns new relative_base"""
    for i in range(len(parameter_list)):
        parameter_list[i] = parameter_tuple_parser(
            parameter_list[i], code_list, relative_base)

    relative_base += parameter_list[0]
    return relative_base


def intcode_ninetynine(parameter_list, code_list):
    """Returns False, so we can exit loop and script."""
    return False


def robot_paint(grid, painted_locations, current, instruction_list):
    """Makes robot paint given location on grid.  Updates and returns grid, painted_locations. """
    painted_locations.add(current)
    if instruction_list[0] == 0:
        grid[current[0]][current[1]] = '.'
    elif instruction_list[0] == 1:
        grid[current[0]][current[1]] = '#'
    else:
        print('And I oop...robot_paint')

    return grid, painted_locations


def robot_move(current, direction):
    """Moves robot one square, depending on current direction it is facing.  Returns new current."""
    if direction == 0:
        current = (current[0] - 1, current[1])
    elif direction == 1:
        current = (current[0], current[1] + 1)
    elif direction == 2:
        current = (current[0] + 1, current[1])
    elif direction == 3:
        current = (current[0], current[1] - 1)
    else:
        print("And I oop...robot_move")
    return current


def robot_turn(direction, instruction_list):
    """ Turns robot.  Returns direction."""
    if instruction_list[1] == 0:
        direction -= 1
    elif instruction_list[1] == 1:
        direction += 1
    else:
        print("And I oop....robot_do_it (2)")
    direction %= 4

    return direction


def robot_do_it(grid, painted_locations, current, direction, instruction_list):
    """Paints, moves, turns robot."""
    grid, painted_locations = robot_paint(
        grid, painted_locations, current, instruction_list)
    direction = robot_turn(direction, instruction_list)
    current = robot_move(current, direction)

    return grid, painted_locations, current, direction


# Create grid
height = 100
width = 100
grid = grid_maker(height, width)

# Initialize placement and direction
current = (height//2, width//2)
direction = 0
grid[current[0]][current[1]] = "#"


i = 0
relative_base = 0
instruction_list = []
painted_locations = set()
keep_going = True
while keep_going:
    while len(instruction_list) < 2:
        # reads raw opcode
        raw_opcode = code_list[i]
        i += 1
        # does intcode operation direction parsing
        (opcode, raw_parameter_code_list) = intcode_parse(raw_opcode)

        # Ensure the parameter code list is correct length for the code.
        parameter_code_list = parameter_code_sizer(
            opcode, raw_parameter_code_list)

        # Create actual list of parameters for each opcode operation
        parameter_list = []

        # grabs parameters, as necessary
        index = 0
        while len(parameter_list) < len(parameter_code_list):
            parameter_list.append(parameter_tuple_maker(
                parameter_code_list[index], code_list, i))
            i += 1
            index += 1

        if opcode == 1:
            intcode_one(parameter_list, code_list, relative_base)

        elif opcode == 2:
            intcode_two(parameter_list, code_list, relative_base)

        elif opcode == 3:
            intcode_three(parameter_list, code_list,
                          relative_base, grid, current)

        elif opcode == 4:
            instruction_list.append(intcode_four(
                parameter_list, code_list, relative_base))

        elif opcode == 5:
            i = intcode_five(parameter_list, code_list, relative_base, i)

        elif opcode == 6:
            i = intcode_six(parameter_list, code_list, relative_base, i)

        elif opcode == 7:
            intcode_seven(parameter_list, code_list, relative_base)

        elif opcode == 8:
            intcode_eight(parameter_list, code_list, relative_base)

        elif opcode == 9:
            relative_base = intcode_nine(
                parameter_list, code_list, relative_base)

        elif opcode == 99:
            keep_going = intcode_ninetynine(parameter_list, code_list)

        else:
            print('and I oop... opcode error')

    # We have two instructions.
    grid, painted_locations, current, direction = robot_do_it(
        grid, painted_locations, current, direction, instruction_list)
    instruction_list = []

for line in grid:
    for char in line:
        print(char, end='')
    print('')
