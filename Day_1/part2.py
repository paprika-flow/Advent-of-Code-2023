#Advent of Code day 1 part 2

"""

Input
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

"""

import re





# test_list:list = re.findall(pattern= "(one|two|three|four|five|six|seven|eight|nine|\d)",string="xvqeightwosixnine61eightsn2tdczfhx")

# first_digit = test_list[0]
# last_digit = test_list[-1]

# if not(first_digit.isnumeric()): 
#     first_digit = numbers_but_words.index(first_digit)+1
# if not(last_digit.isnumeric()): 
#     last_digit = numbers_but_words.index(last_digit)+1

# print(int(f"{first_digit}{last_digit}"))

input_file = open("input.txt")


list_of_inputs:list = input_file.readlines()
numbers_but_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
input_int = 0
for input in list_of_inputs:
    
    match_list:list = re.findall(pattern="(?=(one|two|three|four|five|six|seven|eight|nine|\d))",string=input)

    first_digit = match_list[0]
    last_digit = match_list[-1]

    if not(first_digit.isnumeric()): 
        first_digit = numbers_but_words.index(first_digit)+1
    if not(last_digit.isnumeric()): 
        last_digit = numbers_but_words.index(last_digit)+1

    input_int += int(f"{first_digit}{last_digit}")

print(input_int)