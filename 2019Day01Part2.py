# Author: Ben Wichser
# Date: 12/01/2019
# Description:  Calculates the sum of the fuel required according to the following rule:  to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.  See ReadMe for more full problem.

def fuel_required(mass):
    """
    Calculates the amount of fuel required for a given mass.  Returns 0 if no fuel required (because less than zero).
    """

    new_fuel_required = mass // 3 - 2
    #Base case
    if new_fuel_required <= 0:
        return 0
    
    return new_fuel_required + fuel_required(new_fuel_required)


fin = open('./module_masses.txt')
module_masses = []
for line in fin:
    module_masses.append(int(line.strip()))

fuel_total = 0
for module in module_masses:
    fuel_total += fuel_required(module)


print(fuel_total)




