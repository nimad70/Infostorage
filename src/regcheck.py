# Author: Nima Daryabar
import re


# Check names for being only letters
# True False as return value
def check_only_letters(name):
    is_name = True
    name_pattern = re.compile(r"^([a-zA-Z]+)$") # only letters regex
    if not re.match(name_pattern, name):
        is_name = False
    return is_name


# Check numbers for being only digits
# True False as return value
def check_only_digits(numb):
    is_digit = True
    digit_pattern = re.compile(r"^([\d]+)$") # only letters regex
    if not re.match(digit_pattern, numb):
        is_digit = False
    return is_digit


# Check and get user's given number
def digit_check():
    while True: # Check if number is only digits
        try:
            num = int(input()) # Get number from user
        except ValueError: # if num is not digit
            print("-> Wrong! Enter a number please:", end=' ')
        else: # num is digit
            break
    return num
