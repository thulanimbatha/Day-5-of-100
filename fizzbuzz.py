# coding exercise
# program prints the solution to the FizzBuzz game
'''PRINT OUT EACH NUMBER 1-100'''
'''IF DIVISIBLE BY 3: PRINT FIZZ'''
'''IF DIVISIBLE BY 5: PRINT BUZZ'''
'''IF DIVISIBLE BY 3 AND 5: PRINT FIZZBUZZ'''


for num in range(1, 101, 1):
    # print(num)
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)