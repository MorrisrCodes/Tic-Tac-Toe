import random as rd

print('Welcome to tic tac toe')
gamemode = input('Do you want to play against the computer or a friend? Enter 1 for computer and 2 for friend: ')

x = True
y = True

r1c1 = []
r1c2 = []
r1c3 = []
r2c1 = []
r2c2 = []
r2c3 = []
r3c1 = []
r3c2 = []
r3c3 = []

def check():
    global x, y
    #row wins
    if (r1c1 == ['x'] and r1c2 == ['x'] and r1c3 == ['x']) or (r2c1 == ['x'] and r2c2 == ['x'] and r2c3 == ['x']) or (r3c1 == ['x'] and r3c2 == ['x'] and r3c3 == ['x']):
        x = False
        return x
    elif (r1c1 == ['y'] and r1c2 == ['y'] and r1c3 == ['y']) or (r2c1 == ['y'] and r2c2 == ['y'] and r2c3 == ['y']) or (r3c1 == ['y'] and r3c2 == ['y'] and r3c3 == ['y']):
        y = False
        return y
    #diag wins
    elif (r1c1 == ['x'] and r2c2 == ['x'] and r3c3 == ['x']) or (r1c3 == ['x'] and r2c2 == ['x'] and r3c1 == ['x']):
        x = False
        return x
    elif (r1c1 == ['y'] and r2c2 == ['y'] and r3c3 == ['y']) or (r1c3 == ['y'] and r2c2 == ['y'] and r3c1 == ['y']):
        y = False
        return y
    #column wins
    elif (r1c1 == ['x'] and r2c1 == ['x'] and r3c1 == ['x']) or (r1c2 == ['x'] and r2c2 == ['x'] and r3c2 == ['x']) or (r1c3 == ['x'] and r2c3 == ['x'] and r3c3 == ['x']):
        x = False
        return x
    elif (r1c1 == ['y'] and r2c1 == ['y'] and r3c1 == ['y']) or (r1c2 == ['y'] and r2c2 == ['y'] and r3c2 == ['y']) or (r1c3 == ['y'] and r2c3 == ['y'] and r3c3 == ['y']):
        y = False
        return y
    


#computer mode

if gamemode == '1':

    playerChoice = input('Do you want to be "x" or "o"? ')

    if playerChoice == 'x':
    
        while x == True and y == True:
            move = 'x'
            loc = input('Enter the row and column of your move in this format "r1c1" for row 1 column: ')
            if loc in globals():
                globals()[loc].append(move)
            else:
                print('Invalid row or column number!')
            check()
            if x == False:
                print('You win!')
                break
            compLoc = rd.choice(['r1c1', 'r1c2', 'r1c3', 'r2c1', 'r2c2', 'r2c3', 'r3c1', 'r3c2', 'r3c3'])
            print(f'Computer chose {compLoc}')
            compMove = 'o'
            if compLoc in globals():
                globals()[compLoc].append(compMove)
            check()
            if y == False:
                print('Computer wins!')

    elif playerChoice == 'o':
        
        while x == True and y == True:
            move = 'o'
            loc = input('Enter the row and column of your move in this format "r1c1" for row 1 column: ')
            if loc in globals():
                globals()[loc].append(move)
            else:
                print('Invalid row or column number!')
            check()
            if y == False:
                print('You win!')
                break
            compLoc = rd.choice(['r1c1', 'r1c2', 'r1c3', 'r2c1', 'r2c2', 'r2c3', 'r3c1', 'r3c2', 'r3c3'])
            print(f'Computer chose {compLoc}')
            compMove = 'x'
            if compLoc in globals():
                globals()[compLoc].append(compMove)
            check()
            if x == False:
                print('Computer wins!')



#friend mode

if gamemode == '2':

    x = True
    y = True

    print('Player 1 is "x" and Player 2 is "o"')

    while x == True and y == True:
        move = 'x'
        loc = input('Player 1, enter the row and column of your move in this format "r1c1" for row 1 column: ')
        if loc in globals():
            globals()[loc].append(move)
        else:
            print('Invalid row or column number!')
        check()
        if x == False:
            print('Player 1 wins!')
            break
        move = 'y'
        loc = input('Player 2, enter the row and column of your move in this format "r1c1" for row 1 column: ')
        if loc in globals():
            globals()[loc].append(move)
        else:
            print('Invalid row or column number!')
        check()
        if y == False:
            print('Player 2 wins!')