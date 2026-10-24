import random

print("Sanke - Water - Gun Game")

n = int(input("Enter number of Rounds: "))

options = ["s", "w", "g"]

rounds = 1

user_score = 0
computer_score = 0

while rounds <= n:
    print(f"Rounds: {rounds}\nSnake - 's' \nWater - 'w' \nGun - 'g'")

    user_input = input("Enter your choice: ")
    computer_input = random.choice(options)
    print(f"Computer chose: {computer_input}")

    if user_input == computer_input:
        print("It's a TIE !")
    else:
        if (user_input == "s" and computer_input == "w"):
            print("You WIN !")
            user_score += 1
        elif (user_input == "g" and computer_input == "w"):
            print("You LOSE !")
            computer_score += 1
        elif (user_input == "w" and computer_input == "g"):
            print("You WIN !")
            user_score += 1
        elif (user_input == "s" and computer_input == "g"):
            print("You LOSE !")
            computer_score += 1
        elif (user_input == "g" and computer_input == "s"):
            print("You WIN !")
            user_score += 1
        elif (user_input == "w" and computer_input == "s"):
            print("You LOSE !")
            computer_score += 1
    
    # Announce winner of every round
    if user_input == computer_input:
        print(f"Round: {rounds} is DRAW !\n")
    elif user_score > computer_score:
        print(f"You WON round: {rounds}\n")
    else:
        print(f"Computer WON round: {rounds}\n")
        
    rounds += 1

# Final Winner based on total number of rounds won
print("FINAL RESULTS:")
print(f"Your Score: {user_score}")
print(f"Computer Score: {computer_score}\n")

if user_score > computer_score:
    print("CONGRATS ! You WON the Game.")
elif computer_score > user_score:
    print("YOU LOSE ! Computer WON the Game.")
else:
    print("The Game is DRAW !")
    
print("\nTHANK YOU for Playing the Game.\nGAME OVER !")
