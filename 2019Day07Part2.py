# Author: Ben Wichser
# Date: 12/09/2019
# Description:  Intcode computer seeks maximum thrust.  Must provide proper
#  input sequence for the 5 computers.  see www.adventofcode.com/2019 (day 5)
# for more information

from itertools import permutations


class IntCode:
    """
    IntCode Computer.
    """

    def __init__(self, list_of_codes):
        """
        Init.  Creates computer.
        """
        self.code_base = list_of_codes[:]

    def intcode_phase_setter(self, phase_setting):
        """
        First intcode run, processing the phase setting.
        """
        self.code_list = self.code_base[:]
        self.i = 0
        self.phase_setting = phase_setting
        # creates opcode and parameter list
        raw_opcode, raw_parameter_list, self.i = self.create_opcode(
            self.code_list, self.i)
        # does intcode operations
        (opcode, parameter_code_list) = self.intcode_parse(raw_opcode)
        # parses parameter_code_list
        parameter_list = self.parameter_parser(
            parameter_code_list, raw_parameter_list, self.code_list, opcode)

        if opcode == 3:
            self.intcode_three(
                parameter_list,
                self.code_list,
                self.phase_setting)
        else:
            print('And I oop...initial code is not 3.')
        return self.i

    def intcode_run(self, comp_input, i):
        """
        Runs computer with passed inputs, starting at given location.  Returns
        final diagnostic value.
        """
        self.i = i
        self.comp_input = comp_input
        while True:
            # creates opcode and parameter list
            raw_opcode, raw_parameter_list, self.i = self.create_opcode(
                self.code_list, self.i)
            # does intcode operations
            (opcode, parameter_code_list) = self.intcode_parse(raw_opcode)
            # parses parameter_code_list
            parameter_list = self.parameter_parser(
                parameter_code_list, raw_parameter_list, self.code_list,
                opcode)

            if opcode == 1:
                self.intcode_one(parameter_list, self.code_list)
            elif opcode == 2:
                self.intcode_two(parameter_list, self.code_list)
            elif opcode == 3:
                self.intcode_three(
                    parameter_list,
                    self.code_list,
                    self.comp_input)
            elif opcode == 4:
                output = self.intcode_four(parameter_list, self.code_list)
                return output, self.i
            elif opcode == 5:
                self.i = self.intcode_five(
                    parameter_list, self.code_list, self.i)
            elif opcode == 6:
                self.i = self.intcode_six(
                    parameter_list, self.code_list, self.i)
            elif opcode == 7:
                self.intcode_seven(parameter_list, self.code_list)
            elif opcode == 8:
                self.intcode_eight(parameter_list, self.code_list)
            elif opcode == 99:
                # self.intcode_ninetynine(parameter_list, self.code_list)
                return 0, False
            else:
                print('and I oop... opcode error')
        print('And I oop...out of while loop...')

    def create_opcode(self, code_list, i):
        self.i = i
        opcode = self.code_list[self.i]
        self.i += 1
        # initializes parameter list.
        raw_parameter_list = []
        # grabs parameters, as necessary
        if opcode % 100 not in {99}:
            raw_parameter_list.append(self.code_list[self.i])
            self.i += 1
        if opcode % 100 not in {3, 4, 99}:
            raw_parameter_list.append(self.code_list[self.i])
            self.i += 1
        if opcode % 100 not in {3, 4, 5, 6, 99}:
            raw_parameter_list.append(self.code_list[self.i])
            self.i += 1
        return opcode, raw_parameter_list, self.i

    def intcode_parse(self, code):
        """
        Accepts intcode.  Parses intcode and returns individual parameters.
        """
        actual_code = code % 100
        parameter_piece = code - actual_code
        parameter_piece = parameter_piece // 100
        parameter_code_list = []

        while parameter_piece > 0:
            parameter_code_list.append(parameter_piece % 10)
            parameter_piece = parameter_piece // 10
        return (actual_code, parameter_code_list)

    def parameter_parser(self, parameter_code_list,
                         parameter_list, code_list, opcode):
        """
        Accepts parameter_code_list, parameter_list and code_list [lists] from
        a particular opcode instruction and subsequent entries.
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
        """
        Adds elements in the parameter_list's first two elements.  Places
        sum in parameter_list[2]. Returns True.
        """
        self.code_list[parameter_list[2]
                       ] = parameter_list[0] + parameter_list[1]
        return True

    def intcode_two(self, parameter_list, code_list):
        """
        Multiplies elements in the parameter_list's first two elements.
        Places product in parameter_list[2]. Returns True.
        """
        self.code_list[parameter_list[2]
                       ] = parameter_list[0] * parameter_list[1]
        return True

    def intcode_three(self, parameter_list, code_list, input_code):
        """
        Accepts input_code and places it in parameter_list[0] place in
        code_list.  Returns True. """
        self.code_list[parameter_list[0]] = input_code
        return True

    def intcode_four(self, parameter_list, code_list):
        """
        Prints returns item  in parameter_list[0] place in code_list.
        Returns True.
        """
        return parameter_list[0]

    def intcode_five(self, parameter_list, code_list, i):
        """
        If first parameter is non-zero, sets instruction pointer to second
        parameter.  Returns i
        """
        if parameter_list[0] != 0:
            i = parameter_list[1]
        return i

    def intcode_six(self, parameter_list, code_list, i):
        """"
        If first parameter is zero, sets instruction pointer to second
        parameter.  Returns i
        """
        if parameter_list[0] == 0:
            i = parameter_list[1]
        return i

    def intcode_seven(self, parameter_list, code_list):
        """
        If first parameter is less than second parameter, stores 1 in third
        parameter.  Else stores 0 in third parameter.  Returns True
        """
        if parameter_list[0] < parameter_list[1]:
            self.code_list[parameter_list[2]] = 1
        else:
            self.code_list[parameter_list[2]] = 0
        return True

    def intcode_eight(self, parameter_list, code_list):
        """
        If first parameter is equal to  second parameter, stores 1 in third
        parameter.  Else stores 0 in third parameter.  Returns True
        """
        if parameter_list[0] == parameter_list[1]:
            self.code_list[parameter_list[2]] = 1
        else:
            self.code_list[parameter_list[2]] = 0
        return True

    def intcode_ninetynine(self, parameter_list, code_list):
        """Returns False, so we can exit loop and script."""
        return False


def first_computer_run(computer_list):
    """
    First run of IntCode Computers.  Accepts computer list and
    phase_setting.  Returns list of computers, phase settings, indices for
    future runs.
    """
    for i in range(len(computer_list)):
        index = computer_list[i][0].intcode_phase_setter(computer_list[i][1])
        computer_list[i] = [computer_list[i][0], index]
    return computer_list


def subsequent_computer_run(computers):
    # initialize the index and first input of 0
    i = 0
    output = 0
    while True:
        output, index = computers[i][0].intcode_run(output, computers[i][1])
        computers[i][1] = index
        if i == 4:
            if index is not False:
                last_e_output = output
            elif index is False:
                return last_e_output
        i = (i+1) % 5


# First sample code list
# code_list = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
#             27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]

# Second sample code list
# code_list = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55,
#   1005, 55, 26, 1001, 54, -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0,
#   55, 1001, 55, 1, 55, 2, 53, 55, 53, 4, 53, 1001, 56, -1, 56, 1005, 56, 6,
#   99, 0, 0, 0, 0, 10]

# Puzzle code list
code_list = [
    3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 46, 63, 76, 97, 118, 199, 280, 361,
    442, 99999, 3, 9, 102, 4, 9, 9, 101, 2, 9, 9, 1002, 9, 5, 9, 101, 4, 9, 9,
    102, 2, 9, 9, 4, 9, 99, 3, 9, 101, 5, 9, 9, 102, 3, 9, 9, 101, 3, 9, 9, 4,
    9, 99, 3, 9, 1001, 9, 2, 9, 102, 3, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 5, 9,
    101, 4, 9, 9, 1002, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 5, 9,
    101, 3, 9, 9, 1002, 9, 5, 9, 1001, 9, 5, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9,
    4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9,
    1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9,
    1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9,
    3, 9, 102, 2, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9,
    9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 102,
    2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9,
    101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9,
    99, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9,
    9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101,
    2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9,
    1001, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4,
    9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9,
    4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2,
    9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9,
    101, 2, 9, 9, 4, 9, 99, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4,
    9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9,
    4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2,
    9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99]


# Creates the computers
comp_1 = IntCode(code_list)
comp_2 = IntCode(code_list)
comp_3 = IntCode(code_list)
comp_4 = IntCode(code_list)
comp_5 = IntCode(code_list)
comp_list = [comp_1, comp_2, comp_3, comp_4, comp_5]

thrusters = 0
for test in list(permutations(range(5, 10))):
    # run computers through initial phase-setter
    initial_computer_list = [[comp_list[i], test[i]] for i in range(5)]
    computer_list = first_computer_run(initial_computer_list)
    # runs computers in loop until they exit.
    e_output = subsequent_computer_run(computer_list)
    thrusters = max(e_output, thrusters)

print(thrusters)
