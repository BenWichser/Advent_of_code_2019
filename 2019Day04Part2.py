# Author: Ben Wichser
# Date: 12/03/2019
# Description:  Calculate number of possible passwords with given rules.  see www.adventofcode.com/2019 (day 3) for more information


# Part 2

min = 245318
max = 765747

possible_passwords = 0
for number in range(min, max):
    passing_conditions = 0
    doubles = 0
    number_string = str(number)
    for i in range(5):
        if i == 4:
            if number_string[i] == number_string[i+1] and number_string[i] != number_string[i-1]:
                doubles += 1
        elif i == 0:
            if number_string[i] == number_string[i+1] and number_string[i] != number_string[i+2]:
                doubles += 1
        elif number_string[i] == number_string[i+1] and number_string[i] != number_string[i-1] and number_string[i] != number_string[i+2]:
            doubles += 1
    if doubles > 0:
        passing_conditions += 1
    
    goes_down = False
    for i in range(5):
        if int(number_string[i]) > int(number_string[i+1]):
            goes_down = True
    if goes_down == False:
        passing_conditions += 1
    
    if passing_conditions == 2:
        possible_passwords += 1


print(possible_passwords)