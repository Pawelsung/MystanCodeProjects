"""
File: hangman.py
Name: Paul
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def hide(n):
    """
    :param n: a string that is going to be hidden
    :return: the length of _ to be the hidden word
    """
    ans = ""
    for i in range(len(n)):  # Replace each character in the word with a dash
        ans += "-"
    return ans


def check_input(n1, n2, n3):
    """
    :param n1: a str, the original word
    :param n2: a str, the hidden dash word
    :param n3: a str,  user's guess
    :return: a str, the stored hidden word
    """
    ans = ""
    if n1.find(n3) != -1:  # Check if the user's guess is in the original word
        for i in range(len(n1)):   # Store the guessed character
            if n1[i] == n3:
                ans += n3
            else:
                ans += n2[i]
        return ans
    return n2  # Return the current hidden word if it's not in original word


hang_pattern = [
    """
    ＿＿＿＿＿
    |/      
    |
    |
    |
    |
    =====""",
    """
    ＿＿＿＿＿
    |/      |
    |
    |
    |
    |
    =====""",
    """
    ＿＿＿＿＿
    |/      |
    |       Ｏ
    |
    |
    |
    =====""",
    """
    ＿＿＿＿＿
    |/      |
    |       Ｏ
    |       |
    |       |
    |
    =====""",
    """
    ________
    |/      |
    |       Ｏ
    |      /|
    |       |
    |
    =====""",
    """
    ＿＿＿＿＿
    |/      |
    |       Ｏ
    |      /|\\
    |       |
    |
    =====""",
    """
    ＿＿＿＿＿
    |/      |
    |       Ｏ
    |      /|\\
    |       |
    |      /
    =====""",
    """
    ＿＿＿＿＿
    |/      |
    |       0
    |      /|\\
    |       |
    |      / \\  You're dead!
    ====="""
]


def main():
    """
    Pre-conditions: The program generates a random word and hides it
    Post-conditions: Guess the word within N_TURNS turns and wins or loses
    """
    length = random_word()  # Generate a random word and hide it with dash
    dash = hide(length)
    life = N_TURNS  # Assign N-TURNS to life as remaining turns
    print('THe word looks like ' + str(dash))  # Print the initial hidden word
    while life >= 1:  # While there are still life
        print(hang_pattern[N_TURNS - life])
        print('You have ' + str(life) + ' wrong guess left.')
        input_ch = input('Your guess: ').upper()  # Uppercase user input
        while not input_ch.isalpha() or len(input_ch) != 1:  # Check input is valid
            print("illegal format.")
            input_ch = input('Your guess: ').upper()
        if input_ch in dash:   # Check if there is guessed character.
            print('You are correct!')
            print('The word looks like ' + str(dash))
        else:
            new_dash = check_input(length, dash, input_ch)  # Store the new results
            if new_dash == dash:  # Check input if it is in original word.(here means not correct)
                print('There is no ' + str(input_ch) + "'s in the word.")
                print('The word looks like ' + str(dash))
                life -= 1
            else:  # Input is in original world (user's guess correct)
                dash = new_dash
                print('You are correct!')
                print('The word looks like ' + str(dash))
                if dash == length:  # Check if if all characters have been revealed. (User wins)
                    print('You win!!')
                    print('The word was: ' + str(length))
                    break
    if life == 0:  # End game if there is no remaining life.
        print(hang_pattern[N_TURNS - life])
        print('You are completely hung : (')
        print('The word was: ' + str(length))


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
