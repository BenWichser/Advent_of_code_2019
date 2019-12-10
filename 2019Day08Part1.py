# Author: Ben Wichser
# Date: 12/10/2019
# Description:  Image layer checksum.  see www.adventofcode.com/2019 (day 8) for more information

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
        for i in range(height):
            image_layer_row = []
            for j in range(width):
                image_layer_row.append(int(code[0]))
                code = code[1:]
            image_layer.append(image_layer_row)
        image.append(image_layer)
    return image

def code_counter(data_list):
    """ Counts each code in each element of a list of lists.  Assumes elements are 0, 1, 2.  Returns list of counts"""
    count_list = [0, 0, 0]
    for item in data_list:
        for i in item:
            if i == 0:
                count_list[0] += 1
            elif i == 1:
                count_list[1] += 1
            elif i == 2:
                count_list[2] +=1
            else:
                print('And I oop... not just 0, 1, 2')
    return count_list







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





# def make_orbit_codes(text_file):
#     """Reads text file with each line in form "ASK)DGE" and returns list of codes."""
#     fin = open(text_file)
#     orbit_codes = []
#     for line in fin:
#         orbit_codes.append(line.strip())
#     return orbit_codes


# def make_orbit_dict(orbit_codes):
#     """Takes list of codes in form 'ASD)GGH' and turns them into dictionary.  key is first three digits.  value is list of last three (mult. occurances)Returns dictionary."""
#     orbit_dict = {}
#     for code in orbit_codes:
#         if code[0:3] in orbit_dict.keys():
#             orbit_dict[code[0:3]].append(code[4:])
#         else:
#             orbit_dict[code[0:3]] = [code[4:]]
#     return orbit_dict

# def make_distance_dict(orbit_dict, key1):
#     """Accepts dictionary of orbit codes, and initial key (center).  Returns dictionary of individual distances."""
#     orbits = 0
#     distances = {key1:orbits}
#     key_set = set(orbit_dict.keys())
#     value_set = set()
#     for value in orbit_dict.values():
#         value_set = value_set.union(set(value))

#     orbit_set = key_set.union(value_set)
#     orbit_set.remove(key1)
#     current_vertices = orbit_dict[key1]
#     while len(orbit_set) !=0:
#         orbits += 1
#         print(orbits)
#         new_vertices = []
#         while len(current_vertices) != 0:
#             current_vertex = current_vertices.pop(0)
#             distances[current_vertex] = orbits
#             if current_vertex in orbit_dict.keys():
#                 for new_vertex in orbit_dict[current_vertex]:
#                     new_vertices.append(new_vertex)
#             orbit_set.remove(current_vertex)
#         current_vertices = new_vertices
#     return distances



# orbit_codes = make_orbit_codes('/Users/benjamenwichser/Documents/OregonState/2019Fall/AdventOfCode/Advent_of_code_2019/orbits.txt')

# orbit_dict = make_orbit_dict(orbit_codes)

# #First key is 'COM', as per specification
# key1 = 'COM'
# distances = make_distance_dict(orbit_dict, key1)

# print(sum(distances.values()))