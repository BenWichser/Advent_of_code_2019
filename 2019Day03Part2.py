# Author: Ben Wichser
# Date: 12/02/2019
# Description:  Locate shortest signal sum of intersection.  See www.adventofcode.com/2019 (day 3) for more information


# Part 2

fin = open('./wire_direction_codes')

wire_1_codes = fin.readline().split(',')
wire_2_codes = fin.readline().split(',')


def wire_plotter(wire_code, current_location):
    """Accepts code (string) and current location (tuple of two ints).  Returns list of new locations (tuples of two ints)."""

    new_locations = []
    if wire_code[0] == 'U':
        upper_value = int(wire_code[1:])
        for i in range(1, upper_value+1):
            new_locations.append(
                (current_location[0], current_location[1] + i))
    elif wire_code[0] == 'L':
        left_value = int(wire_code[1:])
        for i in range(1, left_value+1):
            new_locations.append(
                (current_location[0] - i, current_location[1]))
    elif wire_code[0] == 'D':
        down_value = int(wire_code[1:])
        for i in range(1, down_value+1):
            new_locations.append(
                (current_location[0], current_location[1] - i))
    elif wire_code[0] == 'R':
        right_value = int(wire_code[1:])
        for i in range(1, right_value+1):
            new_locations.append(
                (current_location[0] + i, current_location[1]))
    else:
        print('And I oop')

    return new_locations


def signal_counter(wire_code, location_information, intersection):
    """
    Returns the signal total, while also looking out for the intersection.

    Accepts wire_code (string), location_information (tuple of three ints), and intersection (tuple of two ints).  
    Returns tuple of three ints (location_x, location_y, signal to that point)
    """

    if wire_code[0] == 'U':
        upper_value = int(wire_code[1:])
        for i in range(1, upper_value+1):
            new_information = (
                location_information[0], location_information[1] + i, location_information[2] + i)
            if (new_information[0], new_information[1]) == intersection:
                return new_information
    elif wire_code[0] == 'L':
        left_value = int(wire_code[1:])
        for i in range(1, left_value+1):
            new_information = (
                location_information[0] - i, location_information[1], location_information[2] + i)
            if (new_information[0], new_information[1]) == intersection:
                return new_information

    elif wire_code[0] == 'D':
        down_value = int(wire_code[1:])
        for i in range(1, down_value+1):
            new_information = (
                location_information[0], location_information[1] - i, location_information[2] + i)
            if (new_information[0], new_information[1]) == intersection:
                return new_information

    elif wire_code[0] == 'R':
        right_value = int(wire_code[1:])
        for i in range(1, right_value+1):
            new_information = (
                location_information[0] + i, location_information[1], location_information[2] + i)
            if (new_information[0], new_information[1]) == intersection:
                return new_information
    else:
        print('And I oop')

    return new_information


wire_1_info = set()
wire_2_info = set()


current_location = (0, 0)
for length in wire_1_codes:
    return_list = wire_plotter(length, current_location)
    current_location = return_list[-1]
    for item in return_list:
        wire_1_info.add(item)


current_location = (0, 0)
signal_total = 0
for length in wire_2_codes:
    return_list = wire_plotter(length, current_location)
    current_location = return_list[-1]
    for item in return_list:
        wire_2_info.add(item)

intersections = wire_1_info.intersection(wire_2_info)

smallest_signal = 0

intersection_distances = {}
for intersection in intersections:

    intersected_wire_1 = False
    wire_1_code_index = 0
    wire_1_information = (0, 0, 0)
    while not intersected_wire_1:
        new_wire_1_info = signal_counter(
            wire_1_codes[wire_1_code_index], wire_1_information, intersection)
        if (new_wire_1_info[0], new_wire_1_info[1]) == intersection:
            intersected_wire_1 = True
        wire_1_information = new_wire_1_info
        wire_1_code_index += 1
    wire_1_distance = new_wire_1_info[2]

    intersected_wire_2 = False
    wire_2_code_index = 0
    wire_2_information = (0, 0, 0)
    while not intersected_wire_2:
        new_wire_2_info = signal_counter(
            wire_2_codes[wire_2_code_index], wire_2_information, intersection)
        if (new_wire_2_info[0], new_wire_2_info[1]) == intersection:
            intersected_wire_2 = True
        wire_2_information = new_wire_2_info
        wire_2_code_index += 1
    wire_2_distance = new_wire_2_info[2]

    intersection_distance = wire_1_distance + wire_2_distance

    if intersection_distance in intersection_distances.keys():
        intersection_distances[intersection_distance].append(intersection)
    else:
        intersection_distances[intersection_distance] = [intersection]

minimum_distance = min(intersection_distances.keys())

print(minimum_distance)
