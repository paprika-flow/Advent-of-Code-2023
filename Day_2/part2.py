# Day 2 Advent of Code part 2

"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

only 12 red cubes, 13 green cubes, and 14 blue cubes
"""

import re

total_power = 0

with open("input.txt") as input_file:
    list_of_games = input_file.readlines()
    
   

    for game in list_of_games:

        test_red = re.findall(pattern="(\d+)\sred", string= game)
        test_blue= re.findall(pattern="(\d+)\sblue", string= game)
        test_green= re.findall(pattern="(\d+)\sgreen", string= game)

        max_red = max([int(number) for number in test_red ], default=1)
        max_blue = max([int(number) for number in test_blue ], default=1)
        max_green = max([int(number) for number in test_green ], default=1)

        total_power += max_blue*max_green*max_red

    print(total_power)