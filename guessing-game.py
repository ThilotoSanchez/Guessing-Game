import random

attempts_list = []

def high_score():
    if len(attempts_list) <=0:
        print(f'The high score is all yours! Go for it...')
    else:
        print(f'The current high score is {min(attempts_list)} attempts.')

def play_game():
    #help(random)
    num = random.randint(0, 10)
    print('Welcome to the guessing game brave player!')
    while True:
        name = input('Whats your name? ')
        if len(name) > 1: break
        print('No name entered. Dont be shy')
    print(f'\nWell, {name}. All you have to do in this game is to guess a number between 0 and 10.')
    high_score()
    while True:
        wanna_play = input(f'Are you ready to play? (y/n) : ')
        if wanna_play.lower() == 'y' or wanna_play.lower() == 'n':
            break
        print('Not valid. Enter y or n.')
        continue
    attempts = 0
    while wanna_play.lower() == 'y':
        try:
            user_num = input("\nEnter your lucky number: ")
            user_num = int(user_num)
            if user_num <0 or user_num > 10:
                print('Number has to be between 0 and 10. Try again.')
                continue
            if num == user_num:
                attempts += 1
                print(f'Awesome. You got it with {attempts} attempts.\n')
                attempts_list.append(attempts)
                while True:
                    new_round = input(f'Wanna go for the next round? (y/n): ')
                    if new_round.lower() == 'y' or new_round.lower() == 'n':
                        break
                    print('Not valid. Enter y or no.')
                if new_round.lower() != 'y':
                    print('Ok. Have a nice one!')
                    break
                attempts = 0
                num = random.randint(1, 9)
                print(f'\nOk, lets start the next round, {name}')
                high_score()
            elif num > user_num:
                print("Not quite. It's higher.")
                attempts += 1
            elif num < user_num:
                print("Actually, it's lower.")
                attempts += 1
        except ValueError as err:
            print(f'Thats no valid number.')
    else:
        print('Ok, have a good one!')

play_game()
