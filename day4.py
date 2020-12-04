#!/usr/bin/env python
"""How many passports are valid?

https://adventofcode.com/2020/day/4

   ./day4.py <input.txt
"""
import re
import fileinput

test_data = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

def parse_passports(text):
    passport_texts = [line.strip() for line in re.split('\n\n+', text)]
    passports = [dict(field.split(':') for field in text.split()) for text in passport_texts]
    return passports

# Not cid
REQUIRED_FIELDS = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def valid_passport(passport):
    return REQUIRED_FIELDS.issubset(passport)

def count_valid_passports(text):
    passports = parse_passports(text)
    valid_passports = [passport for passport in passports if valid_passport(passport) ]
    return len(valid_passports)

if __name__ == '__main__':
    valid = count_valid_passports(''.join([line for line in fileinput.input()]))
    print(valid)
