import random

'''
random.randint(low, high):
it would generate a number between low and high
(low and high included)
'''

# Guess_Numbers(Computer)
def guess(x):
    return

# Guess_Numbers(User)
def computer_guess(x):
    return


if __name__ == '__main__':
    
    mode = int(input('Choose a play mode : \n1. Guess_Number(Computer) \n2. Guess_Number(User) \n:'))
    if mode == 1:
        x = int(input('The highest number:'))
        guess(x)
    elif mode == 2:
        x = int(input('The highest number:'))
        computer_guess(x)
    else:
        print('You type the wrong thing!')