"""
File: similarity.py
Name: Paul
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry. ATcgAtCGatCgC   tCgc
"""


def match(n1, n2):
    """
    :param n1: A str, representing the long DNA sequence
    :param n2: A str, representing the short DNA sequence
    :return: The best match
    """
    if not len(n1) >= len(n2):  # Check if long-se is longer than short_se.
        return " Invalid input"
    else:
        new_correct = 0  # Store the most correct matches
        similar = ""  # Store the best match
        for i in range(len(n1)-len(n2)+1):
            extra = n1[i: len(n2)+i]  # Extract a substring(same length as n2) of the long sequence.
            correct = 0  # Store correct matches for this substring
            for j in range(len(n2)):
                if extra[0+j] == n2[0+j]:  # If the characters match, assign +1 to correct
                    correct += 1
            if correct > new_correct:  # Update new_correct and similar if this substring has more correct matches.
                new_correct = correct
                similar = extra
        return print('The best match is ' + similar)


def main():
    """
    Pre-conditions: Wait for starting function.
    Post-conditions: Print the best match of the short DNA sequence within the long DNA sequence.
    """
    long_sequence = input("Please give me a DNA sequence to search: ").upper()
    short_sequence = input("What DNA sequence would you like to match? ").upper()
    # extract(long_sequence, short_sequence)
    match(long_sequence, short_sequence)
    # count(correct)

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    main()
