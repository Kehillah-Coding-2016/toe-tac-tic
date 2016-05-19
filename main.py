from models import Board
from models import Player
from models import Mark


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

    spot1x = ' '
    spot2x = ' '
    spot3x = ' '
    spot4x = ' '
    spot5x = ' '
    spot6x = ' '
    spot7x = ' '
    spot8x = ' '
    spot9x = ' '
    spot1o = ' '
    spot2o = ' '
    spot3o = ' '
    spot4o = ' '
    spot5o = ' '
    spot6o = ' '
    spot7o = ' '
    spot8o = ' '
    spot9o = ' '

    player = input('player: ')
    spot = input('selection: ')
        if spot == '1':
            spot1 = '1'
        elif spot == '2':
            spot2 = '2'
        elif spot == '3':
            spot3 = '3'
        elif spot == '4':
            spot4 = '4'
        elif spot == '5':
            spot5 = '5'
        elif spot == '6':
            spot6 = '6'
        elif spot != '1' or '2' or '3' or '4' or '5' or '6':
            print('error')

    print('''
 ''' + spot1 + ''' | ''' + spot2 + ''' | ''' + spot3 + '''
-----------
 ''' + spot4 + ''' | ''' + spot5 + ''' | ''' + spot6 + '''
-----------
   |   |
        ''')

    # if selection == '1':
    # if selection == '2':
    # if selection == '3':
    # if selection == '4':
    # if selection == '5':
    # if selection == '6':
    # if selection == '7':
    # if selection == '8':
    # if selection == '9':
    #
    # player1.make_move()
    # gameBoard.check_win()
    # player2.make_move()
    # gameBoard.check_win()
