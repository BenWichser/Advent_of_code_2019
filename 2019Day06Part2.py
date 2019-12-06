# Author: Ben Wichser
# Date: 12/05/2019
# Description:  Total number of orbits.  see www.adventofcode.com/2019 (day 6) for more information



# Part 1
def make_orbit_codes(text_file):
    """Reads text file with each line in form "ASK)DGE" and returns list of codes."""
    fin = open(text_file)
    orbit_codes = []
    for line in fin:
        orbit_codes.append(line.strip())
    return orbit_codes


def make_orbit_dict(orbit_codes):
    """Takes list of codes in form 'ASD)GGH' and turns them into dictionary.  key is first three digits.  value is list of last three (mult. occurances)Returns dictionary."""
    orbit_dict = {}
    for code in orbit_codes:
        if code[0:3] in orbit_dict.keys():
            orbit_dict[code[0:3]].append(code[4:])
        else:
            orbit_dict[code[0:3]] = [code[4:]]
    return orbit_dict

def make_distance_dict(orbit_dict, key1):
    """Accepts dictionary of orbit codes, and initial key (center).  Returns dictionary of individual distances."""
    orbits = 0
    distances = {key1:orbits}
    key_set = set(orbit_dict.keys())
    value_set = set()
    for value in orbit_dict.values():
        value_set = value_set.union(set(value))

    orbit_set = key_set.union(value_set)
    orbit_set.remove(key1)
    current_vertices = orbit_dict[key1][:]
    while len(orbit_set) !=0:
        orbits += 1
        # print(orbits)
        new_vertices = []
        while len(current_vertices) != 0:
            current_vertex = current_vertices.pop(0)
            distances[current_vertex] = orbits
            if current_vertex in orbit_dict.keys():
                for new_vertex in orbit_dict[current_vertex]:
                    new_vertices.append(new_vertex)
            orbit_set.remove(current_vertex)
        current_vertices = new_vertices
    return distances

def path_maker(orbit_dict, vertex):
    """Accepts dictionary of orbit paths and a target vertex.  Returns list of path to target vertex."""
    path_list = [vertex]
    while path_list[-1] != 'COM':
        # print(path_list)
        target = path_list[-1]
        for key in orbit_dict.keys():
            if target in orbit_dict[key]:
                path_list.append(key)
    return path_list[::-1]


orbit_codes = make_orbit_codes('/Users/benjamenwichser/Documents/OregonState/2019Fall/AdventOfCode/Advent_of_code_2019/orbits.txt')

orbit_dict = make_orbit_dict(orbit_codes)

#First key is 'COM', as per specification
key1 = 'COM'
distances = make_distance_dict(orbit_dict, key1)


you_list = path_maker(orbit_dict, 'YOU')
san_list = path_maker(orbit_dict, 'SAN')
print(len(you_list))
print(len(san_list))
you_set = set(you_list) - set(san_list)
san_set = set(san_list) - set(you_list)

print(you_set)

print(len(you_set) )
print(len(san_set))

print(len(you_list) + len(san_list) - 2* 70 - 2)