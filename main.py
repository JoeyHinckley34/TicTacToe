from board import GameBoard
from player import ai

def main():
    
    BOARD_SIZE = 3

    game = GameBoard(BOARD_SIZE)
    print(game)

    player1 = ai(BOARD_SIZE,1)
    player2 = ai(BOARD_SIZE,2)
    
    player = 0
    
    while game.end == False:
        print(game.end)
        if player % 2 == 0:
            player1.play(game)
        elif player % 2 == 1:
            player2.play(game)
        player += 1
        
        print(game)

if __name__ == '__main__':
    main()
