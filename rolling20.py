import random


def random_roll(dice_amount, char_input, dice_type):
    """
    params: void
    returns: returns a random number between 1 and 20
    """
    results = 0
    for n in range(0, dice_amount):
        results += random.randint(1, dice_type)
    
    return results


def user_roll(user_input):
    """
    params: input from user
    returns: returns values of the dice amount and type chosen
    """

    char_input = "D"
    split_input = user_input.split(char_input)
    
    dice_amount_input = int(split_input[0])
    dice_type_input = int(split_input[1])
    print(f"You choice is: {dice_amount_input} {char_input} {dice_type_input} between {split_input}")
    roll = random_roll(dice_amount_input, char_input, dice_type_input)
    print(roll)


answer = input("Hello! Type the number of die you want to roll, plus \"D\" followed by the die type like this: 2D6\n")
user_roll(answer)



