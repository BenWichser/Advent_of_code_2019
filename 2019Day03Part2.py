# Author: Ben Wichser
# Date: 12/02/2019
# Description:  Locate shortest signal sum of intersection.  See www.adventofcode.com/2019 (day 3) for more information


# Part 2

fin = open('/Users/benjamenwichser/Documents/OregonState/2019Fall/AdventOfCode/Advent_of_code_2019_day1_part1/wire_direction_codes')

wire_1_codes = fin.readline().split(',')
wire_2_codes = fin.readline().split(',')

def wire_plotter(wire_code, current_location, signal_total):
    """Accepts code (string), current location (tuple), and signal_total (int).  Returns dictionary of dictionary of signal totals and location, tuple of current location, and int of signal total."""

    new_signal_informations = []
    if wire_code[0] == 'U':
        upper_value = int(wire_code[1:])
        for i in range(1, upper_value+1):
            new_signal_informations.append( (current_location[0], current_location[1] + i, signal_total + i ))
    elif wire_code[0] == 'L':
        left_value = int(wire_code[1:])
        for i in range(1, left_value+1):
            new_signal_informations.append( (current_location[0] - i, current_location[1], signal_total + i ))
    elif wire_code[0] == 'D':
        down_value = int(wire_code[1:])
        for i in range(1, down_value+1):
            new_signal_informations.append( (current_location[0], current_location[1]  - i, signal_total + i ))
    elif wire_code[0] == 'R':
        right_value = int(wire_code[1:])
        for i in range(1, right_value+1):
            new_signal_informations.append( (current_location[0] + i, current_location[1], signal_total + i) )
    else:
        print('And I oop')
   
    return new_signal_informations

wire_1_info = set()
wire_2_info = set()


current_location = (0,0)
signal_total = 0
for length in wire_1_codes:
    return_list = wire_plotter(length, current_location, signal_total)
    current_location = (return_list[-1][0], return_list[-1][1] )
    signal_total = return_list[-1][2]
    for item in return_list:
        wire_1_info.add(item)


current_location = (0,0)
signal_total = 0
for length in wire_2_codes:
    return_list = wire_plotter(length, current_location, signal_total)
    current_location = (return_list[-1][0], return_list[-1][1] )
    signal_total = return_list[-1][2]
    for item in return_list:
        wire_2_info.add(item)

intersections = set()
for location_1 in wire_1_info:
    for location_2 in wire_2_info:
        if location_1[0] == location_2[0] and location_1[1] == location_2[1]:
            intersections.add( (location_1[0], location_2[1], location_1[2] + location_2[2]))

smallest_signal = 0

for intersection in intersections:
    if smallest_signal == 0:
        smallest_signal = intersection[2]
    elif intersection[2] < smallest_signal:
        smallest_signal = intersection[2]

print(smallest_signal)




