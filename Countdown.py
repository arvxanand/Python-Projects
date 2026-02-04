import time

run = True

while run:
    user_input = input("How many seconds would you like to have for the timer?: ")
    num_of_sec = int(user_input)


    if num_of_sec <= 0:
        print("Please give me a valid number.")

    while num_of_sec > 0:
        print(f"Time Left: {num_of_sec}", end="\r")
        time.sleep(1)
        num_of_sec -= 1

        if num_of_sec == 0:
            print("Countdown over.")

    while True:
        repeat_timer = input("Do you want to start another timer? (y/n)").lower()

        if repeat_timer == "n" or repeat_timer == "no":
            run = False
            break
        elif repeat_timer == "y" or repeat_timer == "yes":
            break
        else:
            print("Invalid response. Try again.")

