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

def move_index(x, y, width, right, down):
    """Move index wrapping horizontally"""
    x = (x + right) % width
    y += down
    return x,y

def get_items(array, right, down):
    height = len(array)
    width = len(array[0])
    items = []
    x,y = 0,0
    while True:
        x,y = move_index(x,y,width, right, down)
        if y >= height:
            break
        items.append(array[y][x])
    return items

def count_items(lines, right, down):
    array = lines_to_array(lines)
    items = get_items(array, right, down)
    return sum(items)

def product(items):
    ans = 1
    for item in items:
        ans *= item
    return ans

if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in fileinput.input()]
    counts = []
    for right, down in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        count = count_items(lines, right, down)
        print(count)
        counts.append(count)
    print(product(counts))
    
    
        


