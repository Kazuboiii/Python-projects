import random

lowest_number=1
highest_number=100
answer=random.randint(lowest_number,highest_number)
guesses=0
is_running=True

print("Welcome To Python Number Guessing Game!!!")
print(f"Please Guess A Number From {lowest_number} To {highest_number}!!")

while is_running:

    Guess=input("Enter Your Guess: ")

    if Guess.isdigit():
        Guess= int(Guess)
        guesses+=1

        if Guess > highest_number or Guess < lowest_number:
            print("The Number You Entered Is Out Of Range!!!")
            print(f"Please Guess A Number From {lowest_number} To {highest_number}!!")
        elif Guess<answer:
            print("TOO LOW!!!!")
        elif Guess>answer:
            print("TOO HIGH!!!!")
        else:
            print("YOU'VE WON!!!!")
            print(f"YOU'VE GUESSED {Guess} WHICH IS THE CORRECT ANSWER!!!")
            print(f"YOUR TOTAL GUESSES ARE {guesses}")

            is_running=False

    else:
        print("Please Enter  A Valid Number!!!")
        print(f"Please Guess A Number From {lowest_number} To {highest_number}!!")