#!/usr/bin/env python3

with open('input_0301') as input:
    map_input = [list(x.strip()) for x in input.readlines()]

map_x = len(map_input[0])
map_y = len(map_input)

def find_trees(x,y):
    trees = []
    for i, pos_y in enumerate(range(y, map_y, y)):
        pos_x = ((i+1) * x) % map_x
        
        if map_input[pos_y][pos_x] == "#":
            tree = (pos_x, pos_y)
            trees.append(tree)
    return trees

slopes = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2)
]

all_trees = 1
for slope in slopes:
    slope_trees = len(find_trees(*slope))
    print(slope_trees)
    all_trees *= slope_trees

print(all_trees)
