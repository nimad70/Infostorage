# Author: Nima Daryabar
import re


# Check names for being only letters
# True False as return value
def check_only_letters(name):
    is_name = True
    # only letters regex
    name_reg = re.compile('^([a-zA-Z]+)$')
    if not re.match(name_reg, name):
        is_name = False
    
    return is_name


# Check numbers for being only digits
# True False as return value
def check_only_digits(numb):
    is_digit = True
    # only letters regex
    digit_reg = re.compile('^([\d]+)$')
    if not re.match(digit_reg, numb):
        is_digit = False
    
    return is_digit