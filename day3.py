#!/usr/bin/env python
"""How many trees will you hit?

https://adventofcode.com/2020/day/3
"""
import fileinput
from typing import List

test_data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


input_map = {'.': 0, '#': 1}
def lines_to_array(lines: List[str]) -> List[List[int]]:
    return [[input_map[char] for char in line] for line in lines]

def move_index(x, y, width, right=3, down=1):
    """Move index wrapping horizontally"""
    x = (x + right) % width
    y += down
    return x,y

def get_items(array):
    height = len(array)
    width = len(array[0])
    items = []
    x,y = 0,0
    while True:
        x,y = move_index(x,y,width)
        if y >= height:
            break
        items.append(array[y][x])
    return items

def count_items(lines):
    array = lines_to_array(lines)
    items = get_items(array)
    return sum(items)
    

if __name__ == '__main__':
    items = count_items([line.rstrip('\n') for line in fileinput.input()])
    print(items)
    
    
        


