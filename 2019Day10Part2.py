# Author: Ben Wichser
# Date: 12/12/2019
# Description:  Asteroid destruction!!!  see www.adventofcode.com/2019 (day 10) for more information


def get_asteroid_map(file_name):
    """Reads asteroid layout map (file of string of lines of text), and finds the asteroids (#).  Returns string locations of the asteroids map rows."""
    asteroid_map = []
    map = open(file_name)
    for row in map:
        asteroid_map.append(str(row.strip()))
    return asteroid_map


def get_asteroid_layout(asteroid_map):
    """Reads asteroid map (list of rows of asteroid strings).  Returns list of tuples of asteroid locations."""
    asteroid_layout = []
    number_of_rows = len(asteroid_map)
    number_of_columns = len(asteroid_map[0])
    for i in range(number_of_rows):
        for j in range(number_of_columns):
            if asteroid_map[i][j] == '#':
                asteroid_layout.append((j, i))
    return asteroid_layout


def can_asteroid_see_you(asteroid, other_asteroid, asteroid_layout):
    """Reads two asteroids (tuples) and an asteroid_map (list).  Returns whether or not the asteroids can see each other."""
    asteroid_x = asteroid[0]
    asteroid_y = asteroid[1]
    other_x = other_asteroid[0]
    other_y = other_asteroid[1]
    delta_x = other_x - asteroid_x
    delta_y = other_y - asteroid_y

    # Vertical lines have no slope.  We check by changing y only
    if delta_x == 0:
        min_y = min(asteroid_y, other_y)
        for i in range(1, abs(delta_y)):
            if (asteroid_x, min_y + i) in asteroid_layout:
                return False
    # Non-vertical lines have slope.  We check by chaning by one x and the slope and see if there's an asteroid there.
    else:
        slope = delta_y / delta_x
        # We start with the asteroid on the left
        if asteroid_x < other_x:
            min_x = asteroid_x
            min_x_y = asteroid_y
        else:
            min_x = other_x
            min_x_y = other_y
        # Checking all the spots along the way for asteroids.
        for i in range(1, abs(delta_x)):
            maybe_other = (min_x + i, min_x_y + i*slope)
            if maybe_other in asteroid_layout:
                return False

    return True


def asteroid_counter(asteroid, asteroid_layout):
    """Reads particular asteroid (tuple of x,y) and asteroid_layout(list of asteroid_layouts).  Returns the number of asteroids that asteroid can see."""
    seen = 0
    for other_asteroid in asteroid_layout:
        if asteroid != other_asteroid:
            if can_asteroid_see_you(asteroid, other_asteroid, asteroid_layout):
                seen += 1
    return seen


def distance_calculator(start, end_list):
    """Accepts start (tuple of x,y) and end_list (list of tuples of (x,y)).  Returns list of tuples (x,y, distance to start)"""
    return_list = []
    for end_spot in end_list:
        distance = ((end_spot[0] - start[0])**2 +
                    (end_spot[1] - start[1])**2)**0.5
        return_list.append((end_spot[0], end_spot[1], distance))
    return return_list


def slope_dictionary_maker(laser_location, asteroid_layout_list, quadrant):
    """Makes dictionary with x/y slopes, and asteroid tuples in values.  Returns dictionary."""
    quadrant_dict = {}
    for asteroid in asteroid_layout_list:
        if asteroid[1] == laser_location[1]:
            slope = 100 * (-1)**(quadrant)
        else:
            slope = (asteroid[0] - laser_location[0]) / \
                (asteroid[1] - laser_location[1])
        if slope not in quadrant_dict.keys():
            quadrant_dict[slope] = [asteroid]
        else:
            quadrant_dict[slope].append(asteroid)
    return quadrant_dict


def zap_q1(laser_location, asteroid_layout_q1, asteroids_zapped):
    """Accepts asteroids in quadrant 1 and zaps them as we go through the quadrant, clockwise.  Returns list of new asteroid_layout_q1 tuples and list of asteroids zapped."""
    asteroid_dict_q1 = slope_dictionary_maker(
        laser_location, asteroid_layout_q1, 1)
    asteroid_slopes_q1 = [key for key in asteroid_dict_q1.keys()]
    asteroid_slopes_q1.sort()

    while asteroid_slopes_q1:
        current_slope = asteroid_slopes_q1.pop()
        current_slope_asteroids = asteroid_dict_q1[current_slope]
        smallest_distance = (0, 0, 0)
        for asteroid in current_slope_asteroids:
            if asteroid[2] < smallest_distance[2] or smallest_distance[2] == 0:
                smallest_distance = asteroid
        asteroid_layout_q1.remove(smallest_distance)
        asteroids_zapped.append(smallest_distance)

    return asteroids_zapped, asteroid_layout_q1


def zap_q2(laser_location, asteroid_layout_q2, asteroids_zapped):
    """Accepts asteroids in quadrant 2 and zaps them as we go through the quadrant, clockwise.  Returns list of new asteroid_layout_q2 tuples and list of asteroids zapped."""
    asteroid_dict_q2 = slope_dictionary_maker(
        laser_location, asteroid_layout_q2, 2)
    asteroid_slopes_q2 = [key for key in asteroid_dict_q2.keys()]
    asteroid_slopes_q2.sort()

    while asteroid_slopes_q2:
        current_slope = asteroid_slopes_q2.pop(-1)
        current_slope_asteroids = asteroid_dict_q2[current_slope]
        smallest_distance = (0, 0, 0)
        for asteroid in current_slope_asteroids:
            if asteroid[2] < smallest_distance[2] or smallest_distance[2] == 0:
                smallest_distance = asteroid
        asteroid_layout_q2.remove(smallest_distance)
        asteroids_zapped.append(smallest_distance)

    return asteroids_zapped, asteroid_layout_q2


def zap_q3(laser_location, asteroid_layout_q3, asteroids_zapped):
    """Accepts asteroids in quadrant 3 and zaps them as we go through the quadrant, clockwise.  Returns list of new asteroid_layout_q4 tuples and list of asteroids zapped."""
    asteroid_dict_q3 = slope_dictionary_maker(
        laser_location, asteroid_layout_q3, 3)
    asteroid_slopes_q3 = [key for key in asteroid_dict_q3.keys()]
    asteroid_slopes_q3.sort()

    while asteroid_slopes_q3:
        current_slope = asteroid_slopes_q3.pop()
        current_slope_asteroids = asteroid_dict_q3[current_slope]
        smallest_distance = (0, 0, 0)
        for asteroid in current_slope_asteroids:
            if asteroid[2] < smallest_distance[2] or smallest_distance[2] == 0:
                smallest_distance = asteroid
        asteroid_layout_q3.remove(smallest_distance)
        asteroids_zapped.append(smallest_distance)

    return asteroids_zapped, asteroid_layout_q3


def zap_q4(laser_location, asteroid_layout_q4, asteroids_zapped):
    """Accepts asteroids in quadrant 4 and zaps them as we go through the quadrant, clockwise.  Returns list of new asteroid_layout_q4 tuples and list of asteroids zapped."""
    asteroid_dict_q4 = slope_dictionary_maker(
        laser_location, asteroid_layout_q4, 4)
    asteroid_slopes_q4 = [key for key in asteroid_dict_q4.keys()]
    asteroid_slopes_q4.sort()

    while asteroid_slopes_q4:
        current_slope = asteroid_slopes_q4.pop(-1)
        current_slope_asteroids = asteroid_dict_q4[current_slope]
        smallest_distance = (0, 0, 0)
        for asteroid in current_slope_asteroids:
            if asteroid[2] < smallest_distance[2] or smallest_distance[2] == 0:
                smallest_distance = asteroid
        asteroid_layout_q4.remove(smallest_distance)
        asteroids_zapped.append(smallest_distance)

    return asteroids_zapped, asteroid_layout_q4


# Part 1 -- Get the best asteroid
asteroid_map = get_asteroid_map('./asteroid_locations.txt')
asteroid_layout = get_asteroid_layout(asteroid_map)

max_seen = 0
for asteroid in asteroid_layout:
    seen = asteroid_counter(asteroid, asteroid_layout)
    if seen > max_seen:
        max_seen = seen
        best_asteroid = asteroid

# Part 2 -- use best asteroid to place laser
laser_location = best_asteroid

# Divide asteroid_layout into quadrants, and make 3-tuples with distance
asteroid_layout_q1 = [asteroid for asteroid in asteroid_layout if asteroid[0]
                      >= laser_location[0] and asteroid[1] < laser_location[1]]
asteroid_layout_q2 = [asteroid for asteroid in asteroid_layout if asteroid[0]
                      > laser_location[0] and asteroid[1] >= laser_location[1]]
asteroid_layout_q3 = [asteroid for asteroid in asteroid_layout if asteroid[0]
                      <= laser_location[0] and asteroid[1] > laser_location[1]]
asteroid_layout_q4 = [asteroid for asteroid in asteroid_layout if asteroid[0]
                      < laser_location[0] and asteroid[1] <= laser_location[1]]
asteroid_layout_q1 = distance_calculator(laser_location, asteroid_layout_q1)
asteroid_layout_q2 = distance_calculator(laser_location, asteroid_layout_q2)
asteroid_layout_q3 = distance_calculator(laser_location, asteroid_layout_q3)
asteroid_layout_q4 = distance_calculator(laser_location, asteroid_layout_q4)

asteroids_zapped = []
while len(asteroids_zapped) < 200:
    asteroids_zapped, asteroid_layout_q1 = zap_q1(
        laser_location, asteroid_layout_q1, asteroids_zapped)
    asteroids_zapped, asteroid_layout_q2 = zap_q2(
        laser_location, asteroid_layout_q2, asteroids_zapped)
    asteroids_zapped, asteroid_layout_q3 = zap_q3(
        laser_location, asteroid_layout_q3, asteroids_zapped)
    asteroids_zapped, asteroid_layout_q4 = zap_q4(
        laser_location, asteroid_layout_q4, asteroids_zapped)


last_asteroid_zapped = asteroids_zapped[199]


print(last_asteroid_zapped[0]*100 + last_asteroid_zapped[1])
