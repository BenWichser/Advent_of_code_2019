# Author: Ben Wichser
# Date: 12/10/2019
# Description:  Image layer visualization.  see www.adventofcode.com/2019 (day 8) for more information

def get_image_code(file_name):
    """Reads specified text file of single string and returns that string."""
    code_object = open(file_name)
    for line in code_object:
        code = str(line.strip())
    return code

def image_layerer(code, width, height):
    """Accepts long string and returns it as a list of list of list of elements.  layers of rows of values."""
    image = []
    while code:
        image_layer = []
        for _ in range(height):
            image_layer_row = []
            for _ in range(width):
                image_layer_row.append(int(code[0]))
                code = code[1:]
            image_layer.append(image_layer_row)
        image.append(image_layer)
    return image







image_width = 25
image_height = 6
layer_size = image_height*image_width

code = get_image_code('/Users/benjamenwichser/Documents/OregonState/2019Fall/AdventOfCode/Advent_of_code_2019/mars_image_data.txt')
image = image_layerer(code, image_width, image_height)
max_count_list = [150 ,0, 0]
for layer in image:
    count_list = code_counter(layer)
    if count_list[0] < max_count_list[0]:
        max_count_list = count_list

print( max_count_list[1] * max_count_list[2])




