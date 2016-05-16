from models import Board
from models import Player



gameBoard = Board()
player1 = Player('x', gameBoard)
player2 = Player('o', gameBoard)


while True:

    player1.make_move()
    gameBoard.check_win()
    player2.make_move()
    gameBoard.check_win()
