# Author: Ben Wichser
# Date: 12/13/2019
# Description:  Play the breakout game.  What's the score after winning?  see www.adventofcode.com/2019 (day 13) for more information

class IntCode:
    """
    IntCode Computer.

    Public Data Members:
    code_list -- intcode instruction set
    Public Methods:
    intcode_run -- runs computer.
    """


    def __init__(self, code_list):
        """
        Creates IntCode computer.  Sets i (index, int) and relative_base to zero.  Accepts code_list (instructions, list).
        """

        self.code_list = code_list
        self.i = 0
        self.relative_base = 0
        self.code_list[0] = 2

    
    def intcode_run(self, computer_input):
        """
        Runs computer.   Returns output from code 4 or 'Halt' from code 99
        """

        self.computer_input = computer_input
        
        while True:

            # reads raw opcode
            self.raw_opcode = self.code_list[self.i]
            self.i += 1
            # does intcode operation direction parsing
            (self.opcode, self.raw_parameter_code_list) = self.__intcode_parse(self.raw_opcode)

            # Ensure the parameter code list is correct length for the code.
            self.parameter_code_list = self.__parameter_code_sizer(
                self.opcode, self.raw_parameter_code_list)

            # Create actual list of parameters for each opcode operation
            self.parameter_list = []

            # grabs parameters, as necessary
            self.index = 0
            while len(self.parameter_list) < len(self.parameter_code_list):
                self.parameter_list.append(self.__parameter_tuple_maker(
                    self.parameter_code_list[self.index], self.code_list, self.i))
                self.i += 1
                self.index += 1
            
            if self.opcode == 1:
                self.__intcode_one(self.parameter_list, self.code_list, self.relative_base)

            elif self.opcode == 2:
                self.__intcode_two(self.parameter_list, self.code_list, self.relative_base)

            elif self.opcode == 3:
                # joystick_position = int(input("Please enter joystick position: ") or "0")
                self.__intcode_three(self.parameter_list, self.code_list,
                            self.relative_base, self.computer_input)
            

            elif self.opcode == 4:
                return self.__intcode_four(self.parameter_list, self.code_list, self.relative_base)

            elif self.opcode == 5:
                self.i = self.__intcode_five(self.parameter_list, self.code_list, self.relative_base, self.i)

            elif self.opcode == 6:
                self.i = self.__intcode_six(self.parameter_list, self.code_list, self.relative_base, self.i)

            elif self.opcode == 7:
                self.__intcode_seven(self.parameter_list, self.code_list, self.relative_base)

            elif self.opcode == 8:
                self.__intcode_eight(self.parameter_list, self.code_list, self.relative_base)

            elif self.opcode == 9:
                self.relative_base = self.__intcode_nine(
                    self.parameter_list, self.code_list, self.relative_base)

            elif self.opcode == 99:
                return self.__intcode_ninetynine(self.parameter_list, self.code_list)

            else:
                print('and I oop... opcode error')


    def __intcode_parse(self, code):
        """Private.  Accepts intcode.  Parses intcode and returns individual parameters. """
        self.code = code
        self.actual_code = self.code % 100
        self.parameter_piece = self.code - self.actual_code
        self.parameter_piece = self.parameter_piece // 100
        self.parameter_code_list = []

        while self.parameter_piece > 0:
            self.parameter_code_list.append(self.parameter_piece % 10)
            self.parameter_piece = self.parameter_piece // 10

        return (self.actual_code, self.parameter_code_list)



    def __parameter_code_sizer(self, opcode, raw_parameter_code_list):
        """Ensures parameter code list is the correct length, according to the particular opcode."""
        self.parameter_lengths = {1: 3, 2: 3, 3: 1, 4: 1,
                            5: 2, 6: 2, 7: 3, 8: 3, 9: 1, 99: 0}
        while len(self.raw_parameter_code_list) < self.parameter_lengths[self.opcode]:
            self.raw_parameter_code_list.append(0)
        return self.raw_parameter_code_list

    def __code_list_lengthener(self, code_list, parameter):
        """Ensures that code_list is long enough to accept an item in its parameter-th location"""
        while len(self.code_list) < parameter + 1:
            self.code_list.append(0)
        return self.code_list


    def __parameter_tuple_maker(self, parameter_code, code_list, i):
        """
        Accepts parameter_code, code_list, relative_base, and i.
        Returns parameter_code, parameter tuple for opcode operation.
        """

        return (parameter_code, self.code_list[i])


    def __parameter_tuple_parser(self, parameter_tuple, code_list, relative_base):
        """
        Accepts parameter_tuple, code_list, and relative_base.  Returns parameter for use in intcode operation.
        """

        if parameter_tuple[0] == 0:
            self.__code_list_lengthener(self.code_list, parameter_tuple[1])
            return self.code_list[parameter_tuple[1]]
        elif parameter_tuple[0] == 1:
            return parameter_tuple[1]
        elif parameter_tuple[0] == 2:
            self.__code_list_lengthener(self.code_list, parameter_tuple[1]+ self.relative_base)
            return self.code_list[parameter_tuple[1] + relative_base]
        else:
            print('And I oop.... parameter_tuple_parser')


    def __intcode_one(self, parameter_list, code_list, relative_base):
        """Adds elements in the parameter_list's first two elements.  Places sum in parameter_list[2]. Returns True. """
        for i in range(len(self.parameter_list) - 1):
            self.parameter_list[i] = self.__parameter_tuple_parser(
                self.parameter_list[i], self.code_list, self.relative_base)

        if self.parameter_list[-1][0] == 0:
            self.code_list = self.__code_list_lengthener(self.code_list, self.parameter_list[-1][1])
            self.code_list[self.parameter_list[-1][1]
                    ] = self.parameter_list[0] + self.parameter_list[1]
        elif self.parameter_list[-1][0] == 2:
            self.code_list = self.__code_list_lengthener(
                self.code_list, self.parameter_list[-1][1]+ self.relative_base)
            self.code_list[self.parameter_list[-1][1] +
                    self.relative_base] = self.parameter_list[0] + self.parameter_list[1]
        else:
            print("And I oop... intcode_one")
        return True


    def __intcode_two(self, parameter_list, code_list, relative_base):
        """Multiplies elements in the parameter_list's first two elements.  Places product in parameter_list[2]. Returns True. """
        for i in range(len(self.parameter_list) - 1):
            self.parameter_list[i] = self.__parameter_tuple_parser(
                self.parameter_list[i], self.code_list, self.relative_base)

        if self.parameter_list[-1][0] == 0:
            self.code_list = self.__code_list_lengthener(self.code_list, self.parameter_list[-1][1])
            self.code_list[self.parameter_list[-1][1]
                    ] = self.parameter_list[0] * self.parameter_list[1]
        elif self.parameter_list[-1][0] == 2:
            self.code_list = self.__code_list_lengthener(
                self.code_list, self.parameter_list[-1][1] + self.relative_base)
            self.code_list[self.parameter_list[-1][1] +
                    self.relative_base] = self.parameter_list[0] * self.parameter_list[1]
        else:
            print("And I oop...intcode_two")
        return True


    def __intcode_three(self, parameter_list, code_list, relative_base, computer_input):
        """ Accepts input and places it in parameter_list[0] place in code_list.  Returns True. """
        self.number_in = computer_input
        if self.parameter_list[0][0] == 0:
            self.code_list = self.__code_list_lengthener(self.code_list, self.parameter_list[0][1])
            self.code_list[self.parameter_list[0][1]] = self.number_in
        elif self.parameter_list[0][0] == 2:
            self.code_list = self.__code_list_lengthener(
                self.code_list, self.parameter_list[0][1]+ self.relative_base)
            self.code_list[self.parameter_list[0][1] + self.relative_base] = self.number_in
        else:
            print("And I oop...intcode_three")
        return True

    def __intcode_four(self, parameter_list, code_list, relative_base):
        """ Returns item in parameter_list[0] place in code_list. """
        for i in range(len(self.parameter_list)):
            self.parameter_list[i] = self.__parameter_tuple_parser(
                self.parameter_list[i], self.code_list, self.relative_base)
        return self.parameter_list[-1]

    def __intcode_five(self, parameter_list, code_list, relative_base, i):
        """If first parameter is non-zero, sets instruction pointer to second parameter.  Returns i"""
        for j in range(len(self.parameter_list)):
            self.parameter_list[j] = self.__parameter_tuple_parser(
                self.parameter_list[j], self.code_list, self.relative_base)
        if self.parameter_list[0] != 0:
            self.i = self.parameter_list[-1]
        return self.i

    def __intcode_six(self, parameter_list, code_list, relative_base,  i):
        """If first parameter is zero, sets instruction pointer to second parameter.  Returns i"""
        for j in range(len(self.parameter_list)):
            self.parameter_list[j] = self.__parameter_tuple_parser(
                self.parameter_list[j], self.code_list, self.relative_base)
        if self.parameter_list[0] == 0:
            self.i = self.parameter_list[-1]
        return self.i


    def __intcode_seven(self, parameter_list, code_list, relative_base):
        """If first parameter is less than second parameter, stores 1 in third parameter.  Else stores 0 in third parameter.  Returns True"""
        for i in range(len(self.parameter_list) - 1):
            self.parameter_list[i] = self.__parameter_tuple_parser(
                self.parameter_list[i], self.code_list, self.relative_base)
        if self.parameter_list[-1][0] == 0:
            self.parameter_list[-1] = self.parameter_list[-1][1]
        elif self.parameter_list[-1][0] == 2:
            self.parameter_list[-1] = self.parameter_list[-1][1] + self.relative_base

        if self.parameter_list[0] < self.parameter_list[1]:
            self.code_list = self.__code_list_lengthener(self.code_list, self.parameter_list[-1])
            self.code_list[self.parameter_list[-1]] = 1
        else:
            self.code_list = self.__code_list_lengthener(self.code_list, self.parameter_list[-1])
            self.code_list[self.parameter_list[-1]] = 0
        return True

    def __intcode_eight(self, parameter_list, code_list, relative_base):
        """If first parameter is equal to  second parameter, stores 1 in third parameter.  Else stores 0 in third parameter.  Returns True"""
        for i in range(len(self.parameter_list) - 1):
            self.parameter_list[i] = self.__parameter_tuple_parser(
                self.parameter_list[i], self.code_list, self.relative_base)
        if self.parameter_list[-1][0] == 0:
            self.parameter_list[-1] = self.parameter_list[-1][1]
        elif self.parameter_list[-1][0] == 2:
            self.parameter_list[-1] = self.parameter_list[-1][1] + self.relative_base

        if self.parameter_list[0] == self.parameter_list[1]:
            self.code_list = self.__code_list_lengthener(self.code_list, self.parameter_list[-1])
            self.code_list[parameter_list[-1]] = 1
        else:
            self.code_list = self.__code_list_lengthener(self.code_list, self.parameter_list[-1])
            self.code_list[self.parameter_list[-1]] = 0
        return True

    def __intcode_nine(self, parameter_list, code_list, relative_base):
        """ Adjust the relative base by the first parameter.  Returns new relative_base"""
        for i in range(len(self.parameter_list)):
            self.parameter_list[i] = self.__parameter_tuple_parser(
                self.parameter_list[i], self.code_list, self.relative_base)

        self.relative_base += self.parameter_list[0]
        return self.relative_base


    def __intcode_ninetynine(self, parameter_list, code_list):
        """Returns False, so we can exit loop and script."""
        return 'Halt'

class Breakout:
    """
    Breakout Game.  Requires IntCode Computer.

    Public Data Members:
    width - width of the game board
    height -- height of the game board
   
    Public Methods:
    play_game - plays the Breakout Game
    print_grid - prints the game board
    """

    def __init__(self, width, height):
        """
        Initializes the breakout game.  Sets the game's width and height according to inputs.  Initializes initial locations of _ball_location and _paddle_location, each to (0,0).
        """

        self.width = width
        self.height = height
        self._ball_location = (0,0)
        self._paddle_location = (0,0)
        self._grid = self.__grid_maker(self.width, self.height)


    def play_game(self, computer):
        """
        Autoplays the breakout game, using intcode computer object for calculations.
        """
        self.computer = computer
        instruction_list = []
        keep_going = True
        while keep_going:
            while len(instruction_list) < 3:
                self._computer_input = self.__input_generator(self._ball_location, self._paddle_location)
                output = self.computer.intcode_run(self._computer_input)
                if output == 'Halt':
                    keep_going = False
                else:
                    instruction_list.append(output)

            game_won = self.__win_check(instruction_list)
            if game_won == True:
                keep_going = False
            
            else:
                self._grid, self._ball_location, self._paddle_location  = self.__update_game(self._grid, instruction_list)
                self.print_grid(self._grid)

            instruction_list = []


    def print_grid(self, grid):
        """Prints the game grid."""
        for row in grid:
            for column in row:
                if column !='.':
                    print(column, end='')
            print('')
        return True


    def __input_generator(self, ball_location, paddle_location):
        """ Private.  Accepts ball and paddle locations.  Produces and returns the input for computer (paddle movement)."""
        if ball_location[1] > paddle_location[1]:
            computer_input  = 1
        elif ball_location[1] < paddle_location[1]:
            computer_input = -1
        else:
            computer_input = 0

        return computer_input



    def __grid_maker(self, width, height):
        """Private method.  Accepts width, height (ints).  Returns width x height grid with '.' as values."""
        grid = [['.' for _ in range(width)] for _ in range(height)]
        return grid


    def __update_game(self, grid, instruction_list):
        """Updates the game board according to rules."""
        location_y = instruction_list[1]
        location_x = instruction_list[0]
        tile = instruction_list[2]


        if tile == 0:
            grid[location_y][location_x] = ' '
        elif tile == 1:
            grid[location_y][location_x] = '#'
        elif tile == 2:
            grid[location_y][location_x] = 'B'
        elif tile == 3:
            grid[location_y][location_x] = '_'
            self._paddle_location = (location_y, location_x)
        elif tile == 4:
            grid[location_y][location_x] = 'O'
            self._ball_location = (location_y, location_x)
        else:
            print('And I oop...play_game')

        return grid, self._ball_location, self._paddle_location

    
    def __win_check(self, instruction_list):
        """Private.  Checks to see if the game is won.  If so, returns True and prints score.  Else returns false."""
        if instruction_list[0] == -1 and instruction_list[1] == 0:
            number_of_blocks = 0
            for k in range(len(self._grid)):
                for j in range(len(self._grid[k])):
                    if self._grid[k][j] == 'B':
                        number_of_blocks += 1
            if number_of_blocks == 0:
                print('Final score:', instruction_list[2])
                return True
        return False

    



code_list = [1,380,379,385,1008,2531,381039,381,1005,381,12,99,109,2532,1101,0,0,383,1101,0,0,382,21002,382,1,1,21002,383,1,2,21101,0,37,0,1106,0,578,4,382,4,383,204,1,1001,382,1,382,1007,382,43,381,1005,381,22,1001,383,1,383,1007,383,22,381,1005,381,18,1006,385,69,99,104,-1,104,0,4,386,3,384,1007,384,0,381,1005,381,94,107,0,384,381,1005,381,108,1106,0,161,107,1,392,381,1006,381,161,1101,-1,0,384,1105,1,119,1007,392,41,381,1006,381,161,1102,1,1,384,20101,0,392,1,21102,20,1,2,21101,0,0,3,21101,138,0,0,1106,0,549,1,392,384,392,20102,1,392,1,21102,20,1,2,21102,1,3,3,21101,0,161,0,1105,1,549,1101,0,0,384,20001,388,390,1,21001,389,0,2,21102,180,1,0,1105,1,578,1206,1,213,1208,1,2,381,1006,381,205,20001,388,390,1,20101,0,389,2,21101,205,0,0,1106,0,393,1002,390,-1,390,1102,1,1,384,20101,0,388,1,20001,389,391,2,21101,0,228,0,1106,0,578,1206,1,261,1208,1,2,381,1006,381,253,21001,388,0,1,20001,389,391,2,21102,253,1,0,1106,0,393,1002,391,-1,391,1101,0,1,384,1005,384,161,20001,388,390,1,20001,389,391,2,21101,0,279,0,1105,1,578,1206,1,316,1208,1,2,381,1006,381,304,20001,388,390,1,20001,389,391,2,21101,304,0,0,1106,0,393,1002,390,-1,390,1002,391,-1,391,1101,0,1,384,1005,384,161,21002,388,1,1,21002,389,1,2,21101,0,0,3,21102,1,338,0,1106,0,549,1,388,390,388,1,389,391,389,21002,388,1,1,20101,0,389,2,21101,4,0,3,21102,1,365,0,1106,0,549,1007,389,21,381,1005,381,75,104,-1,104,0,104,0,99,0,1,0,0,0,0,0,0,291,19,17,1,1,21,109,3,22101,0,-2,1,21202,-1,1,2,21102,0,1,3,21102,1,414,0,1105,1,549,22102,1,-2,1,22101,0,-1,2,21102,1,429,0,1106,0,601,1202,1,1,435,1,386,0,386,104,-1,104,0,4,386,1001,387,-1,387,1005,387,451,99,109,-3,2106,0,0,109,8,22202,-7,-6,-3,22201,-3,-5,-3,21202,-4,64,-2,2207,-3,-2,381,1005,381,492,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,481,21202,-4,8,-2,2207,-3,-2,381,1005,381,518,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,507,2207,-3,-4,381,1005,381,540,21202,-4,-1,-1,22201,-3,-1,-3,2207,-3,-4,381,1006,381,529,22101,0,-3,-7,109,-8,2106,0,0,109,4,1202,-2,43,566,201,-3,566,566,101,639,566,566,1202,-1,1,0,204,-3,204,-2,204,-1,109,-4,2106,0,0,109,3,1202,-1,43,593,201,-2,593,593,101,639,593,593,21002,0,1,-2,109,-3,2106,0,0,109,3,22102,22,-2,1,22201,1,-1,1,21102,479,1,2,21101,0,201,3,21101,946,0,4,21102,630,1,0,1105,1,456,21201,1,1585,-2,109,-3,2106,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,2,2,0,2,0,2,2,2,0,2,0,2,2,2,2,0,0,0,2,2,0,2,2,0,0,2,0,2,2,0,2,2,2,2,2,0,1,1,0,2,0,2,2,2,2,2,2,0,2,2,0,2,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2,2,0,2,0,2,0,0,0,0,0,0,1,1,0,2,2,0,2,0,0,0,2,2,0,2,0,0,0,2,0,0,0,0,2,2,2,0,2,0,0,0,2,0,2,2,0,0,2,0,2,0,2,2,0,1,1,0,0,2,0,2,0,0,2,2,2,2,2,0,2,0,2,2,0,0,0,2,2,0,0,2,2,0,2,2,2,0,0,2,0,2,0,2,0,0,2,0,1,1,0,2,0,2,0,2,2,2,0,0,0,0,0,0,2,0,2,0,0,2,0,2,0,0,2,0,0,0,0,2,2,0,2,2,0,0,2,0,0,0,0,1,1,0,0,0,2,2,2,2,0,2,2,2,2,0,2,0,0,2,2,0,2,2,2,0,0,0,2,2,0,0,2,2,0,0,0,0,2,2,0,0,2,0,1,1,0,0,0,0,0,0,2,2,2,2,2,2,0,0,2,2,0,0,2,2,2,0,0,2,2,2,0,2,0,2,0,0,2,0,2,2,2,0,2,0,0,1,1,0,2,0,0,0,0,2,2,2,0,0,2,0,0,2,0,2,2,2,2,0,2,0,2,0,0,0,0,2,0,2,2,0,2,2,0,2,2,0,2,0,1,1,0,0,2,2,0,2,2,0,2,0,2,0,2,0,2,0,0,0,0,2,2,2,2,0,2,0,2,2,0,2,0,2,2,0,2,2,0,2,2,0,0,1,1,0,0,2,0,0,2,2,2,0,2,0,0,2,2,0,2,2,0,0,0,2,2,0,2,2,2,0,0,2,0,0,0,0,2,2,2,0,0,0,2,0,1,1,0,0,2,2,0,0,2,0,2,2,2,2,0,2,2,2,2,2,2,2,2,2,0,2,2,0,2,2,0,2,0,2,2,0,2,2,0,2,2,2,0,1,1,0,0,0,2,2,2,0,2,0,0,0,0,2,2,2,2,2,2,2,2,0,0,0,2,2,2,2,2,0,0,2,0,0,0,0,2,2,0,2,2,0,1,1,0,2,0,0,2,2,0,2,0,0,0,2,2,2,2,2,2,0,2,2,0,2,0,2,2,0,2,2,0,2,2,2,2,2,0,0,2,0,0,0,0,1,1,0,2,0,0,2,0,2,0,0,2,0,0,2,2,2,2,2,0,2,0,2,2,0,2,2,0,0,2,2,0,0,0,2,2,0,2,2,0,2,2,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,37,59,35,82,55,63,50,72,81,61,59,5,1,69,3,36,79,19,94,73,56,24,20,10,1,25,20,49,14,41,74,10,1,48,97,35,54,11,81,35,36,54,58,49,82,25,96,37,51,26,65,35,51,78,95,58,66,62,83,44,62,53,19,35,90,77,50,38,53,16,24,10,59,72,21,24,91,15,80,80,83,67,27,51,49,31,38,51,10,47,22,68,71,30,19,57,64,6,63,91,63,34,53,95,87,27,83,15,5,2,22,23,34,80,75,27,15,88,73,28,23,4,85,54,68,43,55,31,81,78,16,88,75,85,8,9,27,82,95,34,86,94,31,33,42,94,26,98,73,73,74,89,43,1,55,63,21,93,97,18,57,41,66,83,32,13,67,23,80,22,95,8,68,26,8,76,22,10,53,56,76,11,82,77,83,31,43,49,45,19,72,13,7,21,40,58,94,67,16,84,38,11,62,22,56,5,2,42,2,38,37,83,3,74,9,4,52,91,38,45,31,60,81,52,19,7,54,49,64,73,26,11,38,84,49,79,48,92,48,28,88,71,8,66,86,44,90,21,73,33,15,5,34,34,30,66,29,13,59,30,7,52,59,77,71,4,42,28,73,50,40,77,33,18,66,5,36,49,98,48,29,32,21,10,18,2,79,44,67,19,26,64,27,92,29,3,19,67,73,44,41,49,45,34,61,65,97,56,4,44,85,38,19,43,61,10,97,44,3,93,86,71,36,52,95,36,13,28,53,2,79,66,92,38,8,92,47,40,78,51,67,22,42,76,49,41,23,47,49,87,81,26,11,20,17,11,93,64,78,63,29,80,54,20,62,45,78,38,6,14,14,62,86,10,17,77,60,20,77,42,6,68,28,62,37,44,17,85,16,33,55,85,11,35,2,8,3,88,4,67,16,97,51,40,72,70,45,28,36,47,48,95,60,77,63,1,31,54,52,18,25,46,39,58,86,26,75,48,85,34,56,93,16,98,36,24,61,63,90,32,93,16,53,48,74,73,95,43,81,55,85,29,32,91,34,4,14,3,24,41,44,64,7,78,19,17,75,71,16,22,75,78,89,93,12,90,54,38,61,3,54,61,69,58,17,27,46,75,19,13,46,53,33,87,25,65,67,22,50,90,53,98,11,54,52,57,4,49,92,73,26,70,43,12,7,70,7,58,13,8,27,12,20,86,45,3,98,56,66,58,47,52,87,79,31,37,48,56,46,26,50,75,1,24,96,67,94,11,56,57,7,58,2,21,57,40,64,73,81,13,58,68,45,32,55,13,91,43,59,62,34,28,44,35,68,35,70,1,78,77,69,3,38,11,63,12,56,13,20,82,58,59,22,69,34,82,80,86,15,30,92,39,49,75,27,83,59,89,35,86,19,26,18,50,9,91,82,4,63,57,22,96,54,72,3,76,8,19,24,81,92,76,86,48,70,72,72,75,97,36,95,44,53,40,81,81,33,7,55,58,23,13,24,16,24,67,88,13,32,98,62,71,49,72,52,34,9,61,78,33,72,38,30,35,17,66,35,81,79,62,45,64,11,67,69,49,33,91,74,24,21,36,84,14,75,87,21,57,88,79,70,74,62,4,45,35,76,1,84,74,59,25,3,88,38,34,97,82,31,17,56,95,40,21,77,9,4,1,40,68,60,26,45,55,17,51,7,34,82,27,82,24,72,84,42,72,23,11,48,42,51,22,49,9,80,31,51,39,15,64,44,40,36,67,97,70,39,48,71,75,12,62,11,22,19,80,78,11,58,98,98,69,3,6,14,29,41,10,76,27,5,58,18,22,73,80,34,53,51,87,5,31,13,82,34,10,59,20,10,39,89,12,59,84,31,66,73,7,19,69,86,85,2,34,20,87,28,98,19,50,74,95,69,87,63,63,67,11,47,56,38,9,28,25,46,69,28,63,95,65,83,41,19,78,50,96,77,52,84,37,71,92,51,92,35,97,46,17,71,43,58,54,26,38,9,90,56,9,55,85,52,63,20,8,63,23,24,63,81,22,86,11,90,74,23,19,52,53,22,52,15,85,13,37,52,69,36,10,68,20,54,77,35,15,17,46,88,38,57,69,15,38,60,70,40,17,12,79,33,17,88,90,72,2,62,23,91,41,18,56,22,38,35,37,11,23,381039]










#create computer
computer = IntCode(code_list)

# Create game
height = 25
width = 45
this_game = Breakout(width, height)
this_game.play_game(computer)
