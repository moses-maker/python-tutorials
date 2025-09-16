"""
t = 1 # 2, 3, 4, 5, 6

while t <= 5: # is t less than 5  ? (True, False)
    
    print(t) # 1, 2, 3, 4, 5

    # increment
    t += 1 # t = t + 1, 2+1, 3+1, 4+1, 5+1

"""

import random

while True:
    guess = int(input("Please guess a number to win?"))

    random_number = random.randrange(1, 10)

    if random_number == guess:
        print("Hurray! you have won, winning number is", random_number)

    else:
        print("Fail, the winning number is", random_number)


    