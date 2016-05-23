from models import Board
from models import Player
#from models import Mark

'''
a note: the formatting bit that prints enough blank lines for the screen is from stackoverflow
'''

gameBoard = Board()
player1 = Player('x', gameBoard)
player2 = Player('o', gameBoard)

runprogram = 0

while runprogram < 1:

    #setup for errors in user input
    playererror = False
    spoterror = False

    #define gameboard spots as blank
    spot1 = ' '
    spot2 = ' '
    spot3 = ' '
    spot4 = ' '
    spot5 = ' '
    spot6 = ' '
    spot7 = ' '
    spot8 = ' '
    spot9 = ' '

    #print boards
    print(chr(27) + "[2J")
    print('''
|-------------------------------------|
| NOTE:                               |
| All spots are single-digit numbers, |
| ex. 1, NOT 11 or 1111               |
|        <Spots         Board>        |
|-------------|         |-------------|
 11 | 22 | 33 |         | ''' + spot1 + spot1 + ''' | ''' + spot2 + spot2 + ''' | ''' + spot3 + spot3 + '''
 11 | 22 | 33 |         | ''' + spot1 + spot1 + ''' | ''' + spot2 + spot2 + ''' | ''' + spot3 + spot3 + '''
--------------|         |--------------
 44 | 55 | 66 |         | ''' + spot4 + spot4 + ''' | ''' + spot5 + spot5 + ''' | ''' + spot6 + spot6 + '''
 44 | 55 | 66 |         | ''' + spot4 + spot4 + ''' | ''' + spot5 + spot5 + ''' | ''' + spot6 + spot6 + '''
--------------|         |--------------
 77 | 88 | 99 |         | ''' + spot7 + spot7 + ''' | ''' + spot8 + spot8 + ''' | ''' + spot9 + spot9 + '''
 77 | 88 | 99 |---------| ''' + spot7 + spot7 + ''' | ''' + spot8 + spot8 + ''' | ''' + spot9 + spot9 + '''
               \       /
                \     /
                 \---/
    ''')

    #possible spots
    for x in range(9):
        #setup for errors in user input
        playererror = False
        spoterror = False

        #take the player input
        player = input('player: ')
        if player == 'x cheat':
            print('x wins by cheating')
            quit()
        elif player == 'o cheat':
            print('o wins by cheating')
            quit()
        elif player != 'x' and player != 'o':
            playererror = True
        pass

        #check for errors in user inputs
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

        spot = input('spot: ')

        #check for errors in user inputs
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

        #testing:
        #print('fjklfj')

        #turns the spot selection into a mark for the player
        if player == 'x':
            if spot == '1':
                if spot1 != ' ':
                    spoterror == True
                else:
                    spot1 = 'X'
            elif spot == '2':
                if spot2 != ' ':
                    spoterror == True
                else:
                    spot2 = 'X'
            elif spot == '3':
                if spot3 != ' ':
                    spoterror == True
                else:
                    spot3 = 'X'
            elif spot == '4':
                if spot4 != ' ':
                    spoterror == True
                else:
                    spot4 = 'X'
            elif spot == '5':
                if spot5 != ' ':
                    spoterror == True
                else:
                    spot5 = 'X'
            elif spot == '6':
                if spot6 != ' ':
                    spoterror == True
                else:
                    spot6 = 'X'
            elif spot == '7':
                if spot7 != ' ':
                    spoterror == True
                else:
                    spot7 = 'X'
            elif spot == '8':
                if spot8 != ' ':
                    spoterror == True
                else:
                    spot8 = 'X'
            elif spot == '9':
                if spot9 != ' ':
                    spoterror == True
                else:
                    spot9 = 'X'
            else:
                spoterror = True
        elif player == 'o':
            if spot == '1':
                if spot1 != ' ':
                    spoterror == True
                else:
                    spot1 = 'O'
            elif spot == '2':
                if spot2 != ' ':
                    spoterror == True
                else:
                    spot2 = 'O'
            elif spot == '3':
                if spot3 != ' ':
                    spoterror == True
                else:
                    spot3 = 'O'
            elif spot == '4':
                if spot4 != ' ':
                    spoterror == True
                else:
                    spot4 = 'O'
            elif spot == '5':
                if spot5 != ' ':
                    spoterror == True
                else:
                    spot5 = 'O'
            elif spot == '6':
                if spot6 != ' ':
                    spoterror == True
                else:
                    spot6 = 'O'
            elif spot == '7':
                if spot7 != ' ':
                    spoterror == True
                else:
                    spot7 = 'O'
            elif spot == '8':
                if spot8 != ' ':
                    spoterror == True
                else:
                    spot8 = 'O'
            elif spot == '9':
                if spot9 != ' ':
                    spoterror == True
                else:
                    spot9 = 'O'
            else:
                spoterror = True
        else:
            pass

        #check for errors in user inputs
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

        if player != 'o' and player != 'x':
            playererror = True
        else:
            pass

        #check for errors in user inputs
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

        #print the current game board with x's and o's
        print(chr(27) + "[2J")
        print('''
|-------------------------------------|
| NOTE:                               |
| All spots are single-digit numbers, |
| ex. 1, NOT 11 or 1111               |
|        <Spots         Board>        |
|-------------|         |-------------|
 11 | 22 | 33 |         | ''' + spot1 + spot1 + ''' | ''' + spot2 + spot2 + ''' | ''' + spot3 + spot3 + '''
 11 | 22 | 33 |         | ''' + spot1 + spot1 + ''' | ''' + spot2 + spot2 + ''' | ''' + spot3 + spot3 + '''
--------------|         |--------------
 44 | 55 | 66 |         | ''' + spot4 + spot4 + ''' | ''' + spot5 + spot5 + ''' | ''' + spot6 + spot6 + '''
 44 | 55 | 66 |         | ''' + spot4 + spot4 + ''' | ''' + spot5 + spot5 + ''' | ''' + spot6 + spot6 + '''
--------------|         |--------------
 77 | 88 | 99 |         | ''' + spot7 + spot7 + ''' | ''' + spot8 + spot8 + ''' | ''' + spot9 + spot9 + '''
 77 | 88 | 99 |---------| ''' + spot7 + spot7 + ''' | ''' + spot8 + spot8 + ''' | ''' + spot9 + spot9 + '''
               \       /
                \     /
                 \---/
        ''')

        #check wins for player x
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

        #check wins for player o
        if spot1 == 'O' and spot2 == 'O' and spot3 == 'O':
            print('o wins')
            quit()
        elif spot4 == 'O' and spot5 == 'O' and spot6 == 'O':
            print('o wins')
            quit()
        elif spot7 == 'O' and spot8 == 'O' and spot9 == 'O':
            print('o wins')
            quit()
        elif spot1 == 'O' and spot4 == 'O' and spot7 == 'O':
            print('o wins')
            quit()
        elif spot2 == 'O' and spot5 == 'O' and spot8 == 'O':
            print('o wins')
            quit()
        elif spot3 == 'O' and spot6 == 'O' and spot9 == 'O':
            print('o wins')
            quit()
        elif spot1 == 'O' and spot5 == 'O' and spot9 == 'O':
            print('o wins')
            quit()
        elif spot3 == 'O' and spot5 == 'O' and spot7 == 'O':
            print('o wins')
            quit()

        if spot1 != ' ' and spot2 != ' ' and spot3 != ' ' and spot4 != ' ' and spot5 != ' ' and spot6 != ' ' and spot7 != ' ' and spot8 != ' ' and spot9 != ' ':
            print('nobody wins')
            quit()
        pass

    # player1.make_move()
    # gameBoard.check_win()
    # player2.make_move()
    # gameBoard.check_win()
