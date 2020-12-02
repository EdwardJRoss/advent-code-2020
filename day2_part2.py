#!/usr/bin/env python
"""How many passwords are valid according to their policies?

https://adventofcode.com/2020/day/2
"""
import re
import fileinput

test_data = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

policy_pattern = re.compile(r"(?P<min>[0-9]+)-(?P<max>[0-9]+) (?P<letter>[a-z]): (?P<password>[a-z]+) *")
def parse_policy_line(line):
    """Return lower, upper, letter and password of a policy line

    parse_policy_line("1-3 a: abcde") == (1, 3, "a", "abcde")
    """
    match = policy_pattern.match(line)
    lower = int(match.group('min'))
    upper = int(match.group('max'))
    assert upper >= lower
    letter = match.group('letter')
    assert len(letter) == 1
    password = match.group('password')
    assert len(password) >= 1
    return lower, upper, letter, password

def valid_password(lower, upper, letter, password):
    """Returns whether a password is valid
    Each policy actually describes two positions in the password
    Exactly one of these positions must contain the given letter.
    
    valid_password(1, 3, "a", "abcde") == True
    valid_password(1, 3, "b", "cdefg") == False
    valid_password(2, 9, "c", "ccccccccc") == False
    """
    # Note the -1 to turn 1 indexing into 0 indexing
    matches = [idx for idx in (lower, upper) if password[idx - 1] == letter]
    return len(matches) == 1
    
def count_valid_passwords(lines):
    valid = 0
    for line in lines:
        lower, upper, letter, password = parse_policy_line(line)
        if valid_password(lower, upper, letter, password):
            valid += 1
    return valid

if __name__ == '__main__':
    valid = count_valid_passwords(fileinput.input())
    print(valid)

