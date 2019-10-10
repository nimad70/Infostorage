# Author: Nima Daryabar
import re


# Check names for being only letters
# True False as return value
def check_only_letters(name):
    is_name = True
    # only letters regex
    name_pattern = re.compile(r"^([a-zA-Z]+)$")
    if not re.match(name_pattern, name):
        is_name = False
    
    return is_name


# Check numbers for being only digits
# True False as return value
def check_only_digits(numb):
    is_digit = True
    # only letters regex
    digit_pattern = re.compile(r"^([\d]+)$")
    if not re.match(digit_pattern, numb):
        is_digit = False
    
    return is_digit


# Check and get user's given number
def digit_check():
    # Check if number is only digits
    digit_check = True
    while digit_check:
        try:
            # Get number from user
            num = int(input())
        except ValueError:
            print("-> Wrong! Enter a number please:", end=' ')
        else:
            digit_check = False
    return num