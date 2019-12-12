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


def layer_maker(top_layer, bottom_layer):
    for row in range(len(top_layer)):
        for column in range(len(top_layer[row])):
            if top_layer[row][column] == 2:
                top_layer[row][column] = bottom_layer[row][column]
    return top_layer


image_width = 25
image_height = 6
layer_size = image_height*image_width

code = get_image_code(
    './mars_image_data.txt')
image = image_layerer(code, image_width, image_height)
current_layer = [[2 for _ in range(image_width)] for _ in range(image_height)]
for layer in image:
    current_layer = layer_maker(current_layer, layer)

for row in current_layer:
    new_row = ''
    for i in range(len(row)):
        if row[i] == 1:
            row[i] = "X"
        else:
            row[i] = ' '
        new_row += row[i]

    print(new_row)
