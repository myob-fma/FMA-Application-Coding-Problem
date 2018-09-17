#!/usr/bin/python
import sys

# Welcome to Ida's TicTacToe

#TODO: ADD MORE ERROR MESSAGES
ERROR_MESSAGES=["Sorry, we could not recognise your input. Please try again!","Someone is already at this position! Please try again"]
COMMA=","
EMPTY_SPACE="."
PLAYER_1_MOVE="X"
PLAYER_2_MOVE="O"
PLAYER_QUIT="q"

class TicTacToe:

    # Initialises the tictactoe board, players and index values
    def __init__(self):
        self.board = [[EMPTY_SPACE for x in range(3)] for y in range(3)]
        self.player = 1;
        self.player_move = PLAYER_1_MOVE;
        self.i = 0; # indexes of the players coordinates
        self.j = 0;

    def start_game(self):
        print ("Welcome to Tic Tac Toe! \n\nHere's the current board:");
        self.show_current_board();
        self.play();

    # Prints the current board to console
    def show_current_board(self):
        print("\n");
        for j in self.board:
            row = '';
            for i in j:
                row += i + ' ';
            print(row + '\n');

    # Gets the value the player input
    def play(self):
        player_input_coordinates = self.get_player_input();
        while player_input_coordinates != PLAYER_QUIT: # Check that the player doesn't want to quit

            # Checks that the player entered a valid value
            if (self.player_input_is_valid(player_input_coordinates)):

                if self.board[self.i][self.j] == EMPTY_SPACE: # Checks that no one has already placed there
                    self.board[self.i][self.j] = self.player_move;
                    self.increment_player();
                    self.show_current_board();

                    if self.won_the_game():
                        print("\nCongratulations, you won!\n");
                        exit();

                    if self.last_move():
                        print("Game over - It's a draw!\n");
                        exit();

                else:
                    print (ERROR_MESSAGES[1]);
            else:
                print (ERROR_MESSAGES [0]);

            player_input_coordinates = self.get_player_input();

        exit(); # exit if the player wants to quit


    # Checks if the player entered a "<int>,<int>" for the coordinates in this format
    def player_input_is_valid(self, input_value):
        if len(input_value) == 3:
            if (input_value[1] == COMMA and str(input_value[0]).isdigit() and str(input_value[2]).isdigit()):
                x = int(input_value[0]);
                y = int(input_value[2]);
                if (x <= 3 and x >= 1 and y <= 3 and y >= 1):
                    self.i = y - 1;
                    self.j = x - 1;
                    return True;
        return False;

    def get_player_input(self):
        return input("Player " + str(self.player) + " enter a coord x,y to place your " + self.player_move + " or enter 'q' to give up: ");

    # Adds the player's X or O (depending on which player) to the board
    def increment_player(self):
        if self.player == 2:
            self.player_move = PLAYER_1_MOVE;
            self.player = 1; # Decrement player from 2 to 1
        else:
            self.player_move = PLAYER_2_MOVE;
            self.player = 2; # Increment player from 1 to 2

    def won_the_game(self):
        return self.row_win() or self.column_win() or self.diagonal_win();

    def row_win(self):
        for row in self.board:
            if (row[0] == row[1] == row[2]) and (row[0] != EMPTY_SPACE):
                return True;
        return False;

    def column_win(self):
        for column in range(0, 2):
            if (self.board[0][column] == self.board[1][column] == self.board[2][column]) and (self.board[0][column] != EMPTY_SPACE):
                return True;
        return False;

    def diagonal_win(self):
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and (self.board[1][1] != EMPTY_SPACE):
            return True;
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and (self.board[1][1] != EMPTY_SPACE):
            return True;
        return False;

    def last_move(self):
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j] == EMPTY_SPACE:
                    return False;
        return True;

# Functions called to begin the game
ttt = TicTacToe();
ttt.start_game();
