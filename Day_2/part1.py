# Day 2 Advent of Code part 1

"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

only 12 red cubes, 13 green cubes, and 14 blue cubes
"""

import re



original_red = 12
original_green = 13
original_blue = 14

with open("input.txt") as input_file:
    list_of_games = input_file.readlines()


#test_games = ["Game 1: 3 blue, 4 red; 133 red, 201 green, 6 blue; 2 green", "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"]

    total_id = 0

    for game in list_of_games:

        test_id = re.findall(pattern="Game\s(\d+)", string= game)
        test_id = (int(test_id[0]))

        test_red = re.findall(pattern="(\d+)\sred", string= game)
        test_blue= re.findall(pattern="(\d+)\sblue", string= game)
        test_green= re.findall(pattern="(\d+)\sgreen", string= game)


        should_continue = False 

        for number_of_red in test_red:
            number_of_red = int(number_of_red)
            if number_of_red > original_red:
                should_continue = True
                break
        if(should_continue):
            continue

        for number_of_blue in test_blue:
            number_of_blue = int(number_of_blue)
            if number_of_blue > original_blue:
                should_continue = True
                break
        if(should_continue):
            continue

        for number_of_green in test_green:
            number_of_green = int(number_of_green)
            if number_of_green > original_green:
                should_continue = True
                break
        if(should_continue):
            continue

        total_id += test_id

print(total_id)

    

