import random

user_action = input("Please enter a choice(rock, paper or scissors), if you want to stop playing enter 'End': ")
choices = ["rock", "paper", "scissors"]
comp_action = random.choice(choices)
print(user_action)
print(comp_action)

is_playing = True
if user_action == 'End':
    is_playing = False
    print('End game')

while is_playing:
    if user_action == 'rock' and comp_action == 'rock':
        print('No winner')
    elif user_action == 'rock' and comp_action == 'paper':
        print('You lose, computer won')
    elif user_action == 'rock' and comp_action == 'scissors':
        print('You won, computer lose')
    elif user_action == 'paper' and comp_action == 'paper':
        print('No winner')
    elif user_action == 'paper' and comp_action == 'scissors':
        print('You lose, computer won')
    elif user_action == 'scissors' and comp_action == 'scissors':
        print('No winner')
    user_action = input("Please enter a choice(rock, paper or scissors), if you want to stop playing enter 'End': ")
    comp_action = random.choice(choices)
    print(user_action)
    print(comp_action)
    if user_action == 'End':
        print('End game')
        is_playing = False