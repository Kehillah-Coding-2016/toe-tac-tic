from models import Board
from models import Player
#from models import Mark


gameBoard = Board()
player1 = Player('x', gameBoard)
player2 = Player('o', gameBoard)



while True:

    print('''
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
    ''')

    playererror = False
    spoterror = False

    spot1 = ' '
    spot2 = ' '
    spot3 = ' '
    spot4 = ' '
    spot5 = ' '
    spot6 = ' '
    spot7 = ' '
    spot8 = ' '
    spot9 = ' '

    player = input('player: ')
    spot = input('spot: ')
    if player == 'x':
        if spot == '1':
            spot1 = 'X'
        elif spot == '2':
            spot2 = 'X'
        elif spot == '3':
            spot3 = 'X'
        elif spot == '4':
            spot4 = 'X'
        elif spot == '5':
            spot5 = 'X'
        elif spot == '6':
            spot6 = 'X'
        elif spot == '7':
            spot7 = 'X'
        elif spot == '8':
            spot8 = 'X'
        elif spot == '9':
            spot9 = 'X'
        else:
            spoterror = True
    elif player == 'o':
        if spot == '1':
            spot1 = 'O'
        elif spot == '2':
            spot2 = 'O'
        elif spot == '3':
            spot3 = 'O'
        elif spot == '4':
            spot4 = 'O'
        elif spot == '5':
            spot5 = 'O'
        elif spot == '6':
            spot6 = 'O'
        elif spot == '7':
            spot7 = 'O'
        elif spot == '8':
            spot8 = 'O'
        elif spot == '9':
            spot9 = 'O'
        else:
            spoterror = True
    elif player != 'o' or 'x':
        playererror = True

    if playererror == True and spoterror == True:
        print('error: player, spot')
        quit()
    elif playererror == True and spoterror == False:
        print('error: player')
        quit()
    elif playererror == False and spoterror == True:
        print('error: spot')
        quit()
    elif playererror == False and spoterror == False:
        pass


    print('''
 ''' + spot1 + ''' | ''' + spot2 + ''' | ''' + spot3 + '''
-----------
 ''' + spot4 + ''' | ''' + spot5 + ''' | ''' + spot6 + '''
-----------
 ''' + spot7 + ''' | ''' + spot8 + ''' | ''' + spot9 + '''
        ''')


    if spot1 == 'X' and spot2 == 'X' and spot3 == 'X':
        print('x wins')
        quit()
    elif spot4 == 'X' and spot5 == 'X' and spot6 == 'X':
        print('x wins')
        quit()
    elif spot7 == 'X' and spot8 == 'X' and spot9 == 'X':
        print('x wins')
        quit()
    elif spot1 == 'X' and spot4 == 'X' and spot7 == 'X':
        print('x wins')
        quit()
    elif spot2 == 'X' and spot5 == 'X' and spot8 == 'X':
        print('x wins')
        quit()
    elif spot3 == 'X' and spot6 == 'X' and spot9 == 'X':
        print('x wins')
        quit()
    elif spot1 == 'X' and spot5 == 'X' and spot9 == 'X':
        print('x wins')
        quit()
    elif spot3 == 'X' and spot5 == 'X' and spot7 == 'X':
        print('x wins')
        quit()

    # player1.make_move()
    # gameBoard.check_win()
    # player2.make_move()
    # gameBoard.check_win()
