"""
File: class_reviews.py
Name: Paul
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


def main():
    """
    TODO: Calculate and print the max, min, and average scores for classes SC001 and SC101.
    """
    sc001_max = sc001_min = sc001_sum = sc001_count = 0  # Initial variables for SC001
    sc101_max = sc101_min = sc101_sum = sc101_count = 0  # Initial variables for SC101
    while True:  # Loop until the user enters '-1'
        class_name = input("Which class? ").upper()
        if class_name == '-1':
            break
        score = int(input("Score: "))
        if class_name == 'SC001':
            if sc001_count == 0 or score > sc001_max:  # Sore the max score
                sc001_max = score
            if sc001_count == 0 or score < sc001_min:  # Sore the min score
                sc001_min = score
            sc001_sum += score
            sc001_count += 1
        elif class_name == 'SC101':
            if sc101_count == 0 or score > sc101_max:
                sc101_max = score
            if sc101_count == 0 or score < sc101_min:
                sc101_min = score
            sc101_sum += score
            sc101_count += 1

    if sc001_count == 0 and sc101_count == 0:  # If no entered score on both classes, print text.
        print('No class scores were entered')
    else:
        if sc001_count > 0:  # If scores were entered for SC001, calculate and print the max, min, and average.
            print('==========SC001============')
            print(f'Max (001): {sc001_max}')
            print(f'Min (001): {sc001_min}')
            print(f'Avg (001): {sc001_sum / sc001_count}')
        else:  # If no entered score, print this section with the text.
            print('No score for SC001')

        if sc101_count > 0:  # If scores were entered for SC101, calculate and print the max, min, and average.
            print('============SC101============')
            print(f'Max (101): {sc101_max}')
            print(f'Min (101): {sc101_min}')
            print(f'Avg (101): {sc101_sum / sc101_count}')
        else:  # If no entered score, print this section with the text.
            print('No score for SC101')




# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
