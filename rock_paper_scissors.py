import random

choices = ["rock", "paper", "scissors"]
user_score = 0
cpu_score = 0
ties = 0
round_num = 0

while cpu_score < 3 and user_score < 3:
    round_num += 1
    print(f"Round {round_num}")
    print("_________________")
    object = input("Of Rock, Paper, or Scissors, which one do you choose: ")
    object = object.lower()
    computer = random.choice(choices)

    #Rock win & lose conditions
    if object == "rock" and computer == "rock":
        print(f"No one wins. You both chose {computer}")
        ties += 1
    elif object == "rock" and computer == "scissors":
        print(f"You win this round! Computer chose {computer}.")
        user_score += 1
    elif object == "rock" and computer == "paper":
        print(f"Computer wins this round! They chose {computer}.")
        cpu_score += 1
    # Paper win & lose conditions
    elif object == "paper" and computer == "paper":
        print(f"No one wins. You both chose {computer}")
        ties += 1
    elif object == "paper" and computer == "rock":
        print(f"You win this round! Computer chose {computer}.")
        user_score += 1
    elif object == "paper" and computer == "scissors":
        print(f"Computer wins this round! They chose {computer}.")
        cpu_score += 1
    # Scissors win & lose conditions
    elif object == "scissors" and computer == "scissors":
        print(f"No one wins. You both chose {computer}")
        ties += 1
    elif object == "scissors" and computer == "rock":
        print(f"Computer wins this round! They chose {computer}.")
        cpu_score += 1
    elif object == "scissors" and computer == "paper":
        print(f"You win this round! Computer chose {computer}.")
        user_score += 1
    elif object == "stop":
        break

    

print(f"User Score: {user_score}.")
print(f"Computer Score: {cpu_score}.")
print(f"Number of ties: {ties}.")


    
