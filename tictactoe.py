import random as rd

print('Welcome to tic tac toe')

r1c1 = []
r1c2 = []
r1c3 = []
r2c1 = []
r2c2 = []
r2c3 = []
r3c1 = []
r3c2 = []
r3c3 = []

x = True
y = True

def check():
    global x, y
    #row wins
    if r1c1 == ['x'] and r1c2 == ['x'] and r1c3 == ['x']:
        x = False
        return x
    elif r1c1 == ['y'] and r1c2 == ['y'] and r1c3 == ['y']:
        y = False
        return y
    elif r2c1 == ['x'] and r2c2 == ['x'] and r2c3 == ['x']:
        x = False
        return x
    elif r2c1 == ['y'] and r2c2 == ['y'] and r2c3 == ['y']:
        y = False
        return y
    elif r3c1 == ['x'] and r3c2 == ['x'] and r3c3 == ['x']:
        x = False
        return x
    elif r3c1 == ['y'] and r3c2 == ['y'] and r3c3 == ['y']:
        y = False
        return y
    #diag wins
    elif r1c1 == ['x'] and r2c2 == ['x'] and r3c3 == ['x']:
        x = False
        return x
    elif r1c1 == ['y'] and r2c2 == ['y'] and r3c3 == ['y']:
        y = False
        return y
    elif r1c3 == ['x'] and r2c2 == ['x'] and r3c1 == ['x']:
        x = False
        return x
    elif r1c3 == ['y'] and r2c2 == ['y'] and r3c1 == ['y']:
        y = False
        return y
    #column wins
    elif r1c1 == ['x'] and r2c1 == ['x'] and r3c1 == ['x']:
        x = False
        return x
    elif r1c1 == ['y'] and r2c1 == ['y'] and r3c1 == ['y']:  
        y = False
        return y
    elif r1c2 == ['x'] and r2c2 == ['x'] and r3c2 == ['x']:  
        x = False
        return x
    elif r1c2 == ['y'] and r2c2 == ['y'] and r3c2 == ['y']:
        y = False
        return y
    elif r1c3 == ['x'] and r2c3 == ['x'] and r3c3 == ['x']:
        x = False
        return x
    elif r1c3 == ['y'] and r2c3 == ['y'] and r3c3 == ['y']:
        y = False
        return y

while x == True and y == True:
    move = str(input('Enter either "x" or "o": '))
    loc = input('Enter the row and column of your move in this format "r1c1" for row 1 column: ')
    if loc in globals():
        globals()[loc].append(move)
    else:
        print('Invalid row or column number!')
    check()
    if x == False:
        print('Player 1 wins!')
    elif y == False:
        print('Player 2 wins!')