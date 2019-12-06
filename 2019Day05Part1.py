# Author: Ben Wichser
# Date: 12/05/2019
# Description:  Modified Intcode Computer diagnostic code.  see www.adventofcode.com/2019 (day 5) for more information

code_list = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,32,43,225,101,68,192,224,1001,224,-160,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1001,118,77,224,1001,224,-87,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,1102,5,19,225,1102,74,50,224,101,-3700,224,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1102,89,18,225,1002,14,72,224,1001,224,-3096,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1101,34,53,225,1102,54,10,225,1,113,61,224,101,-39,224,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1101,31,61,224,101,-92,224,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1102,75,18,225,102,48,87,224,101,-4272,224,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1101,23,92,225,2,165,218,224,101,-3675,224,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1102,8,49,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,226,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,1007,677,226,224,1002,223,2,223,1006,224,344,1001,223,1,223,108,677,226,224,102,2,223,223,1006,224,359,1001,223,1,223,7,226,226,224,1002,223,2,223,1005,224,374,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,419,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,434,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,449,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,464,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,479,1001,223,1,223,1008,226,226,224,102,2,223,223,1005,224,494,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,509,101,1,223,223,8,226,677,224,1002,223,2,223,1006,224,524,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,539,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,554,101,1,223,223,1108,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,1107,226,677,224,102,2,223,223,1005,224,584,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,599,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,614,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,629,101,1,223,223,107,226,677,224,102,2,223,223,1005,224,644,101,1,223,223,8,677,677,224,102,2,223,223,1005,224,659,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226]



def intcode_one(parameter_one, parameter_two, parameter_three, code_list):
    """Adds element in the first parameter's index with element in second parameter's index.  Places sum in third parameter's index. Returns True. """
    code_list[parameter_three] = code_list[parameter_one] + code_list[parameter_two]
    return True

def intcode_two(parameter_one, parameter_two, parameter_three, code_list):
    """Multiplies element in the first parameter's index with element in second parameter's index.  Places sum in third parameter's index. Returns True. """
    code_list[parameter_three] = code_list[parameter_one] * code_list[parameter_two]
    return True

def intcode_three(parameter_one, code_list):
    """ Accepts input and places it in given spot in code_list.  Returns True. """
    number_in = int(input('Please enter a number: ') or "1")
    code_list[parameter_one] = number_in
    return True


def intcode_ninetynine(code_list):
    """Returns False, so we can exit loop and script."""
    return False

i = 0
keep_going = True
while keep_going:
    #creates intcode
    opcode = code_list[i]
    i+=1
    #grabs parameters, as necessary
    if opcode not in {99}:
        first_parameter = code_list[i]
        i+=1
    if opcode not in {3, 4, 99}:
        second_parameter = code_list[i]
        i+=1
    if opcode not in {3, 4, 99}:
        third_parameter = code_list[i]
        i+=1

    #does intcode operations

    if opcode == 1:
        intcode_one(first_parameter, second_parameter, third_parameter, code_list)

    elif opcode == 2:
        intcode_two(first_parameter, second_parameter, third_parameter, code_list)

    elif opcode ==3:
        intcode_three(first_parameter, code_list)

    elif opcode == 99:
        keep_going = intcode_ninetynine(code_list)

    else:
        print('and I oop... opcode error')



terminate = False
i = 0
while not terminate:
    if i == 0:
        code_list[code_list[1]] = int(input('Please enter the error code:') or '1')
        i += 2

    elif code_list[i] == 4:
        i+= 1
        print(code_list[code_list[i]])
        i+= 1

    elif code_list[i] == 1:
        code_list[code_list[i+3]] = code_list[code_list[i+1]] + code_list[code_list[i+2]]
        i+= 4

    elif code_list[i] == 2:
        code_list[code_list[i+3]] = code_list[code_list[i+1]] * code_list[code_list[i+2]]
        i+= 4

    elif code_list[i] == 99:
        terminate = True
    
    elif code_list[i] > 100 and code_list[i] !=104:
        value = code_list[i]
        print('Value =', value)
        i+=1
        opcode = value % 100

        if (value% 1000)   // 100 == 0:
            first_term = code_list[code_list[i]]
        elif (value % 1000) // 100 == 1:
            first_term = code_list[i]
        else:
            print('And I oop...1')
        i+=1

        if  value // 1000 == 0:
            second_term = code_list[code_list[i]]
        elif value // 1000 == 1:
            second_term = code_list[i]
        else:
            print('And I oop...2')
        i+=1
        
        if opcode == 1:
            code_list[code_list[i]] = first_term + second_term
        elif opcode == 2:
            code_list[code_list[i]] = first_term * second_term
        elif opcode == 99:
            terminate = True
        else:
            print('And I oop...3')
        i+=1
    
    elif code_list[i] == 104:
        i+=1
        print(code_list[i])
        i+=1

    else:
        print('And I oop...4')







    


