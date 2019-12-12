# Author: Ben Wichser
# Date: 12/12/2019
# Description:  Find asteroid with the best view.  see www.adventofcode.com/2019 (day 10) for more information


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
    """Reads two asteroids (tuples) and an asteroid_layout (list).  Returns whether or not the asteroids can see each other."""
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


asteroid_map = get_asteroid_map('./asteroid_locations.txt')
asteroid_layout = get_asteroid_layout(asteroid_map)

max_seen = 0
for asteroid in asteroid_layout:
    seen = asteroid_counter(asteroid, asteroid_layout)
    max_seen = max(seen, max_seen)

print(max_seen)
