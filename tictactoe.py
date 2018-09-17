#!/usr/bin/python
import sys

# Welcome to Ida's TicTacToe

class TicTacToe:

    # Initialises the board
    def __init__(self):
        self.board = [['.'  for x in range(3)] for y in range(3)]
        self.player = 1;
        self.player_move = 'X';
        self.x = 0;
        self.y = 0;
        # TODO: move this to be a list of different error messages defined up top
        self.error_message = ["Sorry, we could not recognise your input. Please try again!","Someone is already at this position! Please try again"]

    # Begins the game
    def start(self):
        print ("Welcome to Tic Tac Toe! \n\nHere's the current board:");
        self.print_current_board();
        self.get_player_input();

    # Prints the current board to console
    def print_current_board(self):
        print("\n");
        for y in self.board:
            row = '';
            for x in y:
                row += x + ' ';
            print(row + '\n');

    # Gets the value the player input
    def get_player_input(self):
        player_input = input("Player " + str(self.player) + " enter a coord x,y to place your " + self.player_move + " or enter 'q' to give up: ");
        while player_input != 'q': # Check that the player doesn't want to quit

            # Checks that the player entered a valid value
            if (self.check_validity_of_input(player_input)):

                if self.board[self.x][self.y] == '.': # Checks that no one has already placed there
                    self.board[self.x][self.y] = self.player_move;
                    self.increment_player(self)
                    if not self.check_if_they_won():
                        self.print_current_board();
                    elif self.last_move():
                        print("It's a draw!");
                        exit();
                    else:
                        print("\nCongratulations, you won!");
                        exit();
                else:
                    print (self.error_message[1]);
            else:
                print (self.error_message[0]);

            player_input = input("Player " + str(self.player) + " enter a coord x,y to place your X or enter 'q' to give up: ");

        exit(); # exit if the player wants to quit


    # Checks if the player entered a "<value>,<value>" where each value is
    def check_validity_of_input(self, input_value):
        if len(input_value) == 3:
            if (input_value[1] == ',' and str(input_value[0]).isdigit() and str(input_value[2]).isdigit() ):
                # Set the X and Y variables by minusing one
                x = int(input_value[0]) - 1;
                y = int(input_value[2]) - 1;
                if (x <= 2 and x >= 0 and y <= 2 and y >= 0):
                    self.x = x;
                    self.y = y
                    return True;
        return False;

    # Adds the player's X or O (depending on which player) to the board
    def increment_player(self):
        if self.player == 2:
            self.player_move = 'O';
            self.player = 1; # Decrement player from 2 to 1
        else:
            self.player_move = 'X';
            self.player = 2; # Increment player from 1 to 2

    #TODO CHECK IF THEY WON
    def check_if_they_won(self):
        return self.check_rows() or self.check_columns() or self.check_diagonal();

    def check_rows(self):
        for y in self.board:
            if (y[0] == y[1] == y[2]) and (y[0] != '.'):
                return True;
        return False;

    def check_columns(self):
        for x in range(0, 2):
            if (self.board[0][x] == self.board[1][x] == self.board[2][x]) and (self.board[0][x] != '.'):
                return True;
        return False;

    def check_diagonal(self):
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and (self.board[1][1] != '.'):
            return True;
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and (self.board[1][1] != '.'):
            return True;
        return False;

    #TODO: Check if it's a draw
    def last_move(self):
        for y in self.board:
            for x in y:
                if self.board[x][y] == ".":
                    return False;
        return True;

# Functions called to begin the game
ttt = TicTacToe();
ttt.start();
