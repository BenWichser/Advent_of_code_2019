# Author: Ben Wichser
# Date: 12/01/2019
# Description:  Recreates 1202 Intcode computer.  see www.adventofcode.com/2019 (day 2) for more information

list_of_codes = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0]

list_of_codes[1]=12
list_of_codes[2]=2

i = 0
while i < len(list_of_codes):
    if list_of_codes[i] == 99:
        print(list_of_codes[0])
        i = len(list_of_codes)
    elif list_of_codes[i] == 1:
        list_of_codes[list_of_codes[i+3]] = list_of_codes[list_of_codes[i+1]] + list_of_codes[list_of_codes[i+2]]
    elif list_of_codes[i] == 2:
        list_of_codes[list_of_codes[i+3]] = list_of_codes[list_of_codes[i+1]] * list_of_codes[list_of_codes[i+2]]
    else:
        print('ERROR ERROR.  PLEASE REBOOT YOUR CODING EFFORTS')
    i += 4
