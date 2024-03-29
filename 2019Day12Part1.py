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

    def energy_calculation(self):
        """Calculates this moon's energy is the product of the sum of the absolute positions and product of the absolute velocities.  Returns the energy amount."""

        energy = (abs(self.position_x) + abs(self.position_y) + abs(self.position_z)) * \
            (abs(self.velocity_x) + abs(self.velocity_y) + abs(self.velocity_z))
        return energy


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

while time <= 1000:
    for moon in moons:
        moon.velocity_update(moons)

    for moon in moons:
        moon.position_update()

    time += 1


total_energy = 0
for moon in moons:
    total_energy += moon.energy_calculation()

print(total_energy)
