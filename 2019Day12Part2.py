# Author: Ben Wichser
# Date: 12/12/2019
# Description:  Jupiter oon movement.  see www.adventofcode.com/2019 (day 12) for more information


class Moon:
    """ Moon class."""

    def __init__(self, position_x, position_y, position_z):
        """Initialization.  Creates moon at given position.  Creates initial velocity of zero in all three dimensions as well."""

        self.position_x = position_x
        self.position_y = position_y
        self.position_z = position_z

        self.velocity_x = 0
        self.velocity_y = 0
        self.velocity_z = 0

        self.locations = dict()

    def velocity_update(self, moons):
        """Updates this moon's velocity based on the positions of all the moons.  Returns True."""

        for moon in moons:
            if self.position_x > moon.position_x:
                self.velocity_x -= 1
            elif self.position_x < moon.position_x:
                self.velocity_x += 1
            if self.position_y > moon.position_y:
                self.velocity_y -= 1
            elif self.position_y < moon.position_y:
                self.velocity_y += 1
            if self.position_z > moon.position_z:
                self.velocity_z -= 1
            elif self.position_z < moon.position_z:
                self.velocity_z += 1

        return True

    def position_update(self):
        """Updates this moon's position based on its velocity.  Returns True."""
        self.position_x += self.velocity_x
        self.position_y += self.velocity_y
        self.position_z += self.velocity_z

        return True

    def repeat_state(self):
        key = sum( [self.position_x, self.position_y, self.position_z, self.velocity_x, self.velocity_y, self.velocity_z])
        if key in self.locations:
            if (self.position_x, self.position_y, self.position_z, self.velocity_x, self.velocity_y, self.velocity_z) in self.locations[key]:
                return True
            else:
                self.locations[key].add((self.position_x, self.position_y, self.position_z, self.velocity_x, self.velocity_y, self.velocity_z))
                return False

        else:
            self.locations[key] = set( (self.position_x, self.position_y, self.position_z, self.velocity_x, self.velocity_y, self.velocity_z))
            return False


# Initial Moon Locations (input from AdventOfCode)
# <x=-1, y=-4, z=0>
# <x=4, y=7, z=-1>
# <x=-14, y=-10, z=9>
# <x=1, y=2, z=17>

io = Moon(-1, -4, 0)
europa = Moon(4, 7, -1)
ganymede = Moon(-14, -10, 9)
callisto = Moon(1, 2, 17)

time = 1
moons = [io, europa, ganymede, callisto]
repeat = False

while not repeat:
    for moon in moons:
        moon.velocity_update(moons)

    for moon in moons:
        moon.position_update()

    repeat = True
    for moon in moons:
        if moon.repeat_state() == False:
            repeat = False
            break
    
    print(time)


    time += 1


print(time - 1)
