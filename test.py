import random

secret_number = random.randint(1, 20)
attempts = 0 

while True:
    guess = int(input("Guess a number 1 - 20: "))
    attempts += 1
    if guess == secret_number:
        print(f"You got the correct number! It only took you {attempts} attempts!")
        break
    elif guess > 20 or guess < 1:
        print("The number is betwen 1 and 20")
    elif guess < secret_number:
        print("Guess too low!")
    elif guess > secret_number:
        print("Guess too high!")
    
