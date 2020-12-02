#!/usr/bin/env python
"""Find the two entries that sum to 2020 and then multiply those two numbers together.

Usage - if the numbers are in a file called day1.txt:
   ./day1_part2.py <day1.txt
"""
import fileinput

numbers = []
for line in fileinput.input():
    numbers.append(int(line.strip()))

# Brute force search
# O(n^2) ~ 400 checks
for n1 in numbers:
    for n2 in numbers:
        for n3 in numbers:
            if n1 < n2 < n3 and n1 + n2 + n3 == 2020:
                print(n1 * n2 * n3)
