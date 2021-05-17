# Tic Tac Toe game
# board
import sys


class game:

    def __init__(self):
        print('One of you choose X and the other one O , X takes the first turn')
        # positions of all inuts
        self.positions = []
        self.board = ['-', '-', '-',
                      '-', '-', '-',
                      '-', '-', '-']

    def displayBoard(self):
        print(self.board[0]+' | '+self.board[1]+' | '+self.board[2])
        print(self.board[3]+' | '+self.board[4]+' | '+self.board[5])
        print(self.board[6]+' | '+self.board[7]+' | '+self.board[8])
        self.playersTurn()

    # players Turn

    def playersTurn(self):

        if sorted(self.positions) == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            print('Game over Its a tie')
            self.finish()

        self.x_count = self.board.count('X')
        self.o_count = self.board.count('O')
        # win check
        if self.x_count > 2 or self.o_count > 2:
            # row check
            if self.board[0] == self.board[1] == self.board[2] == 'X':
                print('player X wins the game')
                sys.exit()

            if self.board[0] == self.board[1] == self.board[2] == 'O':
                print('player O wins the game')
                sys.exit()
            if self.board[3] == self.board[4] == self.board[5] == 'X':
                print('player X wins the game')
                sys.exit()
            if self.board[3] == self.board[4] == self.board[5] == 'O':
                print('player O wins the game')
                sys.exit()
            if self.board[6] == self.board[7] == self.board[8] == 'X':
                print('player X wins the game')
                sys.exit()
            if self.board[6] == self.board[7] == self.board[8] == 'O':
                print('player O wins the game')
                sys.exit()
            # column check
            if self.board[0] == self.board[3] == self.board[6] == 'X':
                print('player X wins the game')
                self.finish()

            if self.board[0] == self.board[3] == self.board[6] == 'O':
                print('player O wins the game')
                self.finish()

            if self.board[1] == self.board[4] == self.board[7] == 'X':
                print('player X wins the game')
                self.finish()
            if self.board[1] == self.board[4] == self.board[7] == 'O':
                print('player O wins the game')
                self.finish()
            if self.board[2] == self.board[5] == self.board[8] == 'X':
                print('player X wins the game')
                self.finish()
            if self.board[2] == self.board[5] == self.board[8] == 'O':
                print('player O wins the game')
                self.finish()

            # diagnol check
            if self.board[0] == self.board[4] == self.board[8] == 'X':
                print('player X wins the game')
                self.finish()
            if self.board[0] == self.board[4] == self.board[8] == 'O':
                print('player O wins the game')
                self.finish()
            # another diagnol
            if self.board[2] == self.board[4] == self.board[6] == 'X':
                print('player  X wins the game')
                self.finish()
            if self.board[2] == self.board[4] == self.board[6] == 'O':
                print('player  O wins the game')
                self.finish()

        if self.x_count == self.o_count:

            self.player_x()

        else:

            self.player_o()

    # player X

    def player_x(self):
        # displaying the turn
        print('player x turn ')
        # Taking input from the user
        self.x_input = int(input('Enter a number between 0-8: '))
        # checking if the number is greater than 8
        if self.x_input > 8 or self.x_input < 0:
            self.x_input = int(input(
                'Oops invalid index please enter a number between 0-8'))
        # checking if the input is already filled or not
        if self.x_input in self.positions:
            print('The place is already occupied!!!!!!!!!!!!!!')
            self.player_x()
        else:
            self.positions.append(self.x_input)

        self.player_x_fill()

    # filling the board for player_x

    def player_x_fill(self):
        # removing the element from the given position
        self.board.pop(self.x_input)
        # placing x at the given position
        self.board.insert(self.x_input, 'X')
        # displaying board
        self.displayBoard()
        # calling players function
        self.playersTurn()

    # player o

    def player_o(self):
        # displaying the turn
        print('player o turn')
        # Taking input from the user
        self.o_input = int(input('Enter a number between 0-8 : '))
        # checking if the number is greater than 8
        if self.o_input > 8 or self.o_input < 0:
            self.o_input = int(input(
                'Oops invalid index please enter a number between 0-8'))
        # checking if the input is already filled or not
        if self.o_input in self.positions:
            print('The place is already occupied!!!!!!!!!!!')
            self.player_o()
        else:
            self.positions.append(self.o_input)

        self.player_o_fill()

    # Filling the board for player o
    def player_o_fill(self):
        # removing the element from the given position
        self.board.pop(self.o_input)
        # placing x at the given position
        self.board.insert(self.o_input, 'O')
        # displaying board
        self.displayBoard()
        # calling palyers function
        self.playersTurn()

    def finish(self):
        self.option = input('Would you like to play again y/n')
        self.option.lower()
        if self.option == 'y':
            g = game()
            g.displayBoard()
        else:
            print('We hope you enjoyed!!!!')
            sys.exit()


g = game()
g.displayBoard()
