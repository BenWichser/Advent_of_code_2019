# Author: Ben Wichser
# Date: 12/02/2019
# Description:  Locate intersection closest to central point.  see www.adventofcode.com/2019 (day 3) for more information


# Part 1

fin = open('./wire_direction_codes')

wire_1_codes = fin.readline().split(',')
wire_2_codes = fin.readline().split(',')

def wire_plotter(wire_code, current_location):
    """Accepts code list and current location (tuple).  Returns list of tuples of locations."""
    new_locations = []
    if wire_code[0] == 'U':
        upper_value = int(wire_code[1:])
        for i in range(1, upper_value+1):
            new_locations.append( (current_location[0], current_location[1] + i) )
        current_location = ( current_location[0], current_location[1] + upper_value)
    elif wire_code[0] == 'L':
        left_value = int(wire_code[1:])
        for i in range(1, left_value+1):
            new_locations.append( (current_location[0] - i, current_location[1]) )
        current_location = ( current_location[0] - left_value, current_location[1])
    elif wire_code[0] == 'D':
        down_value = int(wire_code[1:])
        for i in range(1, down_value+1):
            new_locations.append( (current_location[0], current_location[1]  - i) )
        current_location = ( current_location[0], current_location[1] - down_value)
    elif wire_code[0] == 'R':
        right_value = int(wire_code[1:])
        for i in range(1, right_value+1):
            new_locations.append( (current_location[0] + i, current_location[1] ))
        current_location = ( current_location[0] + right_value , current_location[1])
    else:
        print('And I oop')
   
    return { 'locations': new_locations, 'current': current_location}

wire_1_locations = set()
wire_2_locations = set()


current_location = (0,0)
for length  in wire_1_codes:
    return_dict = wire_plotter(length, current_location)
    for i in return_dict['locations']:
        wire_1_locations.add(i)
    current_location = return_dict['current']


current_location = (0,0)
for length  in wire_2_codes:
    return_dict = wire_plotter(length, current_location)
    for i in return_dict['locations']:
        wire_2_locations.add(i)
    current_location = return_dict['current']

intersections = set()
for location in wire_1_locations:
    if location in wire_2_locations:
        intersections.add(location)

smallest_distance = 0

for intersection in intersections:
    distance = abs(intersection[0]) + abs(intersection[1])
    if smallest_distance == 0:
        smallest_distance = distance
    elif distance < smallest_distance:
        smallest_distance = distance

print(smallest_distance)




