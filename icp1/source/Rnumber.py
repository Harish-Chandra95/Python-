import random

input_num = int(input("Enter any number between 0 to 9"))
r_num = random.randint(0,9)

if(input_num == r_num):
    print("Congratulations! you have guessed correctly")
elif(input_num < r_num):
    print("Your Guessed number is less than the random number")
elif(input_num > r_num):
    print("Your guessed number id greater than the random number")