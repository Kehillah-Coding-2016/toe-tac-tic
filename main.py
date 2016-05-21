from models import Board
from models import Player
#from models import Mark


gameBoard = Board()
player1 = Player('x', gameBoard)
player2 = Player('o', gameBoard)



while True:

    #possible spots
    print('''
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
    ''')

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

    for x in range(9):
        #take the player input
        player = input('player: ')
        if player == 'x cheat':
            print('x wins by cheating')
            quit()
        elif player == 'o cheat':
            print('o wins by cheating')
            quit()
        else:
            pass
        spot = input('spot: ')

        #checking for duplicate spot selections
        if spot == '1' and spot1 == ' ':
            spoterror = False
        spoterror = True
        if spot == '2' and spot2 == ' ':
            spoterror = False
        spoterror = True
        if spot == '3' and spot3 == ' ':
            spoterror = False
        spoterror = True
        if spot == '4' and spot4 == ' ':
            spoterror = False
        spoterror = True
        if spot == '5' and spot5 == ' ':
            spoterror = False
        spoterror = True
        if spot == '6' and spot6 == ' ':
            spoterror = False
        spoterror = True
        if spot == '7' and spot7 == ' ':
            spoterror = False
        spoterror = True
        if spot == '8' and spot8 == ' ':
            spoterror = False
        spoterror = True
        if spot == '9' and spot9 == ' ':
            spoterror = False
        spoterror = True
    else: 
        spoterror = False
        pass

        
        

        #turns the spot selection into a mark for the player
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
        print('''
 ''' + spot1 + ''' | ''' + spot2 + ''' | ''' + spot3 + '''
-----------
 ''' + spot4 + ''' | ''' + spot5 + ''' | ''' + spot6 + '''
-----------
 ''' + spot7 + ''' | ''' + spot8 + ''' | ''' + spot9 + '''
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
