import random

options=("rock","paper","scissor")
player= None

computer= random.choice(options)

while player not in options:
    player=input("Choose your weapon(rock,paper,scissor):").lower()

print(f"Player: {player}")
print(f"Computer: {computer}")

if player== computer:
    print("ITS A TIE!!!!!")
elif player=="rock" and computer=="scissor":
    print("YOU WON!!!!")
elif player == "scissor" and computer == "paper":
    print("YOU WON!!!!")
elif player == "paper" and computer == "rock":
    print("YOU WON!!!!")
else:
    print("YOU LOSE (T_T) ")