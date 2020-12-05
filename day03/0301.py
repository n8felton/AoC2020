#!/usr/bin/env python3

with open('input_0301') as input:
    map_input = [list(x.strip()) for x in input.readlines()]

map_x = len(map_input[0])
map_y = len(map_input)
trees = []

for pos_y in range(1, map_y):
    pos_x = (pos_y * 3) % map_x
    
    if map_input[pos_y][pos_x] == "#":
        tree = (pos_x, pos_y)
        trees.append(tree)

print(len(trees))