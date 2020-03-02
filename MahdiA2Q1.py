# ICS3UI-02 for Ms. Harris

# Mahdi Amini

# P.Conc: finding the numbers which are dividable to 3 or 5

# Assignment NO: 2

# Question NO: 1


# date started: 02/26/2020
# date finished: 02/26/2020
# This program returns the sum of multiples of 3 and 5 between 0 and limit (parameter).

# get the limitation from the user
limitation = int(
    input("This program returns the sum of multiples of 3 and 5 between 0 and limit (parameter).type the limitation: "))
# using for loop to check any possible value
for check_Number in range(1, limitation):
    # check whether multiplication of 3 is less or equal to the limitation
    if 3 * check_Number <= limitation:
        print(3 * check_Number, end=",")
    # check whether multiplication of 5 is less or equal to the limitation and is not equal to the multiplication of
    # 3 to avoid repetition
    if limitation >= 5 * check_Number != 3 * check_Number:
        print(5 * check_Number, end=",")
