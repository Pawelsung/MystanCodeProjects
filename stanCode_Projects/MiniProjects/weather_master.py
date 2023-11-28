"""
File: weather_master.py
Name: Paul
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""
EXIT = -100


def main():
    """
    Pre-conditions: Showing instructions and waiting for user entering values.
    Post-conditions:
    1. This code asks for input each time till EXIT.
    2. While collecting all values, it calculates and prints the result .
    """
    print('stanCode "Weather Master 4.0"')
    data = float(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
    max_temp = data  # set input data to max_temp
    min_temp = data  # set input data to min_temp
    cold_temp = 0   # cold_temp is used for counting the temp < 16
    sum_temp = 0  # sums up all the input value
    sum_t = 0  # count the times of input actions
    if data == EXIT:  # Set boundary condition
        print('No temperatures were entered.')
    else:
        while True:
            sum_temp += data   # plus values and store
            sum_t += 1  # plus input times and store
            if data < 16:  # if temp <16, store the times in  cold_temp
                cold_temp += 1
            if data > max_temp:  # if input value is higher than max_temp, assign input value to max_temp
                max_temp = data
            if data < min_temp:  # if input value is lower than min_temp, assign input value to min_temp
                min_temp = data
            data = float(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
            if data == EXIT:  # exit the loop by entering -100 or -1
                break
        print('Highest temperature = ' + str(max_temp))
        print('Lowest temperature = ' + str(min_temp))
        print('Average = ' + str(sum_temp/sum_t))
        print(str(cold_temp) + ' cold day(s)')


# EXIT = -100
#
#
# def main():
#     """
#     TODO:
#     """
#     print('Enter your values!')
#     data = float(input('Enter Data:'))
#     max_temp = 0
#     min_temp = 0
#     cold_temp = 0
#     sum_temp = 0
#     sum_t = 0
#     if data == EXIT:
#         print('End code!')
#     else:
#         print('standCode \"Weather Master 4.o\"')
#         for i in range(sum_t):
#             # weather()
#             # print('Next Temperature:' + '(or ' + str(EXIT) + ' to quit' + ')? ' + str(data))
#         print('Highest temperature =' + str(max_temp()))
#         # print('Lowest temperature =' + str(min_temp))
#         # print('Average =' + str(sum_temp/sum_t))
#         # print(str(cold_temp) + 'cold day (s)')
#
#
# def max_temp(data):
#     data = max_temp()
#     if data > max_temp():
#         return data
#
# def weather():
#     max_temp = data
#     min_temp = data
#     while True:
#         sum_temp = sum_temp + data
#         sum_t += 1
#         data = int(input('Enter Data:'))
#         if data == EXIT:
#             break
#         if data > max_temp:
#             data = max_temp
#         if data < min_temp:
#             data = min_temp

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
    main()
