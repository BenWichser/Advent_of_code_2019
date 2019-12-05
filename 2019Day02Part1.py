# Author: Ben Wichser
# Date: 12/01/2019
# Description:  Recreates 1202 Intcode computer.  see www.adventofcode.com/2019 (day 2) for more information

list_of_codes = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0]


#Setup the computer
list_of_codes[1]= int(input('Please enter first digit for computer:') or '12')
list_of_codes[2]= int(input('Please enter second digit for computer:') or '2')
i = 0


def intcode_one(parameter_one, parameter_two, parameter_three, code_list):
    """Adds element in the first parameter's index with element in second parameter's index.  Places sum in third parameter's index. Returns True. """
    code_list[parameter_three] = code_list[parameter_one] + code_list[parameter_two]
    return True

def intcode_two(parameter_one, parameter_two, parameter_three, code_list):
    """Multiplies element in the first parameter's index with element in second parameter's index.  Places sum in third parameter's index. Returns True. """
    code_list[parameter_three] = code_list[parameter_one] * code_list[parameter_two]
    return True

def intcode_ninetynine(code_list):
    """Prints first value.  Returns False, so we can exit loop and script."""
    print(code_list[0])
    return False

keep_going = True
while keep_going:
    #creates intcode
    opcode = list_of_codes[i]
    i+=1
    #grabs parameters, as necessary
    if opcode not in {99}:
        first_parameter = list_of_codes[i]
        i+=1
    if opcode not in {99}:
        second_parameter = list_of_codes[i]
        i+=1
    if opcode not in {99}:
        third_parameter = list_of_codes[i]
        i+=1

    #does intcode operations
    if opcode == 99:
        keep_going = intcode_ninetynine(list_of_codes)

    elif opcode == 1:
        intcode_one(first_parameter, second_parameter, third_parameter, list_of_codes)

    elif opcode == 2:
        intcode_two(first_parameter, second_parameter, third_parameter, list_of_codes)

    else:
        print('and I oop... opcode error')

