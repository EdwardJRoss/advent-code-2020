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


#    byr (Birth Year) - four digits; at least 1920 and at most 2002.
#    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#    hgt (Height) - a number followed by either cm or in:
#        If cm, the number must be at least 150 and at most 193.
#        If in, the number must be at least 59 and at most 76.
#    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#    pid (Passport ID) - a nine-digit number, including leading zeroes.
#    cid (Country ID) - ignored, missing or not.

class NumberValidator():
    def __init__(self, num_digits, min=None, max=None):
        self.num_digits = num_digits
        self.min = min
        self.max = max
        self.pattern = re.compile('^[0-9]{%i}$' % num_digits) 

    def __call__(self, text):
        if not self.pattern.match(text):
            return False
        number = int(text)
        if self.min and number < self.min:
            return False
        if self.max and number > self.max:
            return False
        return True

def valid_hgt(text):
    if text.endswith('cm'):
        return NumberValidator(3, 150, 193)(text[:-2])
    if text.endswith('in'):
        return NumberValidator(2, 59, 76)(text[:-2])
    return False

def valid_hcl(text):
    return bool(re.match('^#[0-9a-f]{6}$', text))

ECLS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
def valid_ecl(text):
    return text in ECLS

validators = {
    'byr': NumberValidator(4, 1920, 2002),
    'iyr': NumberValidator(4, 2010, 2020),
    'eyr': NumberValidator(4, 2020, 2030),
    'hgt': valid_hgt,
    'hcl': valid_hcl,
    'ecl': valid_ecl,
    'pid': NumberValidator(9),
    }
    

def valid_passport(passport):
    if not REQUIRED_FIELDS.issubset(passport):
        return False
    validations = [val(passport[field]) for field, val in validators.items()]
    return all(validations)

def count_valid_passports(text):
    passports = parse_passports(text)
    valid_passports = [passport for passport in passports if valid_passport(passport) ]
    return len(valid_passports)

if __name__ == '__main__':
    valid = count_valid_passports(''.join([line for line in fileinput.input()]))
    print(valid)
