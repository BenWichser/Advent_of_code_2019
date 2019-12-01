# Author: Ben Wichser
# Date: 12/01/2019
# Description:  Calculates the sum of the fuel required according to the following rule:  to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.  See ReadMe for full story.


fin = open('./module_masses.txt')
module_masses = []
for line in fin:
    module_masses.append(int(line.strip()))

fuel_total = 0
for module in module_masses:
    fuel_total += module //3 - 2

print(fuel_total)





