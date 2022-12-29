import random

user_wins = 0
computer_wins = 0
counts = 0
equal = 0
options = ['rock', 'paper', 'scissors']
while True:
    user_input = input("Please type Rock/Paper/Scissors or Q to quit.")
    if user_input == 'q':
        break
    if user_input not in options:
        continue
    counts += 1
    random_number = random.randint(0, 2)
    #rock: 0, paper: 1, scissors: 2

    computer = options[random_number]
    print('Computer picked:', computer, '.')

    if user_input == 'rock' and computer == 'scissors':
        print('You won!')
        user_wins +=1
        continue
    elif user_input == 'paper' and computer == 'rock':
        print('You won!')
        user_wins +=1
        
    elif user_input == 'scissors' and computer == 'paper':
        print('You won!')
        user_wins +=1
    elif user_input == computer:
        print('Equal')    
        equal += 1
    else:
        print('You lost!')
        computer_wins += 1

print('Total play', counts, 'times')
print('You won', user_wins, 'times', 'The computer won', computer_wins, 'times', 'Equal', equal, 'times')
print('Thanks for your playing')
