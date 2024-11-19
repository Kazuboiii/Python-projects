import random

def play():
    user= input("What do you want to choose? 'R' for rock, 'P' for paper, 'S' for scissor:").upper()
    computer = random.choice (['R','P','S'])
    if user == computer:
        return "ITS A TIE!!!"


    if is_win(user,computer):
        return"YOU WON!!!!"

    return"YOU LOST!!!"


def is_win(player,opponent):
    if (player=='R' and opponent=='S') or (player=='S' and opponent=='P') or (player=='P' and opponent=='R'):
        return True



print(play())