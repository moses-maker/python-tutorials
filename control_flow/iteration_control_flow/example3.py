import random

random_numbers = random.randrange(1,10)

while True:
    user = int(input("Guess a number?"))

    if random_numbers == user:
        print("HURRAY found", random_numbers)

    else:
        print("Fail try again it is", random_numbers)
