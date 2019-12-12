# Author: Ben Wichser
# Date: 12/09/2019
# Description:  Intcode computer seeks maximum thrust.  Must provide proper input sequence for the 5 computers.  see www.adventofcode.com/2019 (day 5) for more information

from itertools import permutations


class IntCode:
    """
    IntCode Computer.
    """

    def __init__(self, list_of_codes):
        """
        Init.  Creates computer.
        """

        self.input_one = False
        self.input_two = False
        self.code_list = list_of_codes[:]

    def intcode_run(self,  input_one, input_two):
        """
        Runs computer with passed inputs.  Returns final diagnostic value.
        """

        self.input_one = input_one
        self.input_two = input_two
        self.input_list = [input_one, input_two]

        i = 0
        keep_going = True
        while keep_going:
            # creates opcode
            opcode = self.code_list[i]
            i += 1
            # initializes parameter list.
            parameter_list = []
            # grabs parameters, as necessary
            if opcode % 100 not in {99}:
                parameter_list.append(self.code_list[i])
                i += 1
            if opcode % 100 not in {3, 4, 99}:
                parameter_list.append(self.code_list[i])
                i += 1
            if opcode % 100 not in {3, 4, 5, 6, 99}:
                parameter_list.append(self.code_list[i])
                i += 1

            # does intcode operations
            (opcode, parameter_code_list) = self.intcode_parse(opcode)

            # parses parameter_code_list
            parameter_list = self.parameter_parser(
                parameter_code_list, parameter_list, self.code_list, opcode)

            if opcode == 1:
                self.intcode_one(parameter_list, self.code_list)

            elif opcode == 2:
                self.intcode_two(parameter_list, self.code_list)

            elif opcode == 3:
                self.intcode_three(
                    parameter_list, self.code_list, self.input_list.pop(0))

            elif opcode == 4:
                output = self.intcode_four(parameter_list, self.code_list)

            elif opcode == 5:
                i = self.intcode_five(parameter_list, self.code_list, i)

            elif opcode == 6:
                i = self.intcode_six(parameter_list, self.code_list, i)

            elif opcode == 7:
                self.intcode_seven(parameter_list, self.code_list)

            elif opcode == 8:
                self.intcode_eight(parameter_list, self.code_list)

            elif opcode == 99:
                keep_going = self.intcode_ninetynine(
                    parameter_list, self.code_list)

            else:
                print('and I oop... opcode error')
        return output

    def intcode_parse(self, code):
        """Accepts intcode.  Parses intcode and returns individual parameters. """
        actual_code = code % 100
        parameter_piece = code - actual_code
        parameter_piece = parameter_piece // 100
        parameter_code_list = []

        while parameter_piece > 0:
            parameter_code_list.append(parameter_piece % 10)
            parameter_piece = parameter_piece // 10

        return (actual_code, parameter_code_list)

    def parameter_parser(self, parameter_code_list, parameter_list, code_list, opcode):
        """
        Accepts parameter_code_list, parameter_list and code_list [lists] from a particular opcode instruction and subsequent entries.
        Returns list of parameters.
        """

        for i in range(len(parameter_list)-1):
            if i >= len(parameter_code_list):
                parameter_list[i] = self.code_list[parameter_list[i]]
            elif parameter_code_list[i] == 0:
                parameter_list[i] = self.code_list[parameter_list[i]]
            elif parameter_code_list[i] == 1:
                parameter_list[i] = parameter_list[i]
            else:
                print('And I oop....parameter_creator')

        if opcode in {4} and len(parameter_code_list) < 1:
            parameter_list[-1] = self.code_list[parameter_list[-1]]

        if opcode in {5, 6} and len(parameter_code_list) < 2:
            parameter_list[-1] = self.code_list[parameter_list[-1]]

        return parameter_list

    def intcode_one(self, parameter_list, code_list):
        """Adds elements in the parameter_list's first two elements.  Places sum in parameter_list[2]. Returns True. """
        self.code_list[parameter_list[2]
                       ] = parameter_list[0] + parameter_list[1]
        return True

    def intcode_two(self, parameter_list, code_list):
        """Multiplies elements in the parameter_list's first two elements.  Places product in parameter_list[2]. Returns True. """
        self.code_list[parameter_list[2]
                       ] = parameter_list[0] * parameter_list[1]
        return True

    def intcode_three(self, parameter_list, code_list, input_code):
        """ Accepts input_code and places it in parameter_list[0] place in code_list.  Returns True. """
        self.code_list[parameter_list[0]] = input_code
        return True

    def intcode_four(self, parameter_list, code_list):
        """ Prints returns item  in parameter_list[0] place in code_list.  Returns True. """
        return parameter_list[0]

    def intcode_five(self, parameter_list, code_list, i):
        """If first parameter is non-zero, sets instruction pointer to second parameter.  Returns i"""
        if parameter_list[0] != 0:
            i = parameter_list[1]
        return i

    def intcode_six(self, parameter_list, code_list, i):
        """If first parameter is zero, sets instruction pointer to second parameter.  Returns i"""
        if parameter_list[0] == 0:
            i = parameter_list[1]
        return i

    def intcode_seven(self, parameter_list, code_list):
        """If first parameter is less than second parameter, stores 1 in third parameter.  Else stores 0 in third parameter.  Returns True"""
        if parameter_list[0] < parameter_list[1]:
            self.code_list[parameter_list[2]] = 1
        else:
            self.code_list[parameter_list[2]] = 0
        return True

    def intcode_eight(self, parameter_list, code_list):
        """If first parameter is equal to  second parameter, stores 1 in third parameter.  Else stores 0 in third parameter.  Returns True"""
        if parameter_list[0] == parameter_list[1]:
            self.code_list[parameter_list[2]] = 1
        else:
            self.code_list[parameter_list[2]] = 0
        return True

    def intcode_ninetynine(self, parameter_list, code_list):
        """Returns False, so we can exit loop and script."""
        return False


code_list = [3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 46, 63, 76, 97, 118, 199, 280, 361, 442, 99999, 3, 9, 102, 4, 9, 9, 101, 2, 9, 9, 1002, 9, 5, 9, 101, 4, 9, 9, 102, 2, 9, 9, 4, 9, 99, 3, 9, 101, 5, 9, 9, 102, 3, 9, 9, 101, 3, 9, 9, 4, 9, 99, 3, 9, 1001, 9, 2, 9, 102, 3, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 5, 9, 101, 4, 9, 9, 1002, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 5, 9, 101, 3, 9, 9, 1002, 9, 5, 9, 1001, 9, 5, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9,
             4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99]


# code_list_test = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]


# Creates the computers
comp_1 = IntCode(code_list)
comp_2 = IntCode(code_list)
comp_3 = IntCode(code_list)
comp_4 = IntCode(code_list)
comp_5 = IntCode(code_list)


thrusters = 0
for test in list(permutations(range(0, 5))):
    output = 0
    i = 0
    for computer in [comp_1, comp_2, comp_3, comp_4, comp_5]:
        output = computer.intcode_run(test[i], output)
        i += 1
    if thrusters == 0 or output > thrusters:
        thrusters = output


print(thrusters)
