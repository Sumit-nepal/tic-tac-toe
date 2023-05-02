import random
import os.path
import json
random.seed()

def draw_board(board):
    # develop code to draw the board
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[0][0], board[0][1], board[0][2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[1][0], board[1][1], board[1][2]))
    print('\t_____|_____|_____')
 
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(board[2][0], board[2][1], board[2][2]))
    print("\t     |     |")
    print("\n")


def welcome(board):
    # prints the welcome message
    print("Welcome to the \"Unbeatable Noughts and Crosses\" game. \nThe board layout is shown below:")

    # display the board by calling draw_board(board)
    draw_board(board)

    # print the message
    print("When prompted, enter the number corresponding to the square you want.")

def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    # define a list with blank items
    board = [ [' ',' ',' '],\
              [' ',' ',' '],\
              [' ',' ',' ']]
    
    # call the board function and pass the argument
    draw_board(board)
    return board

def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    terminate = False  # initialize terminate with initial value of False
    while not terminate:
        try:
            # prompt user where they want to put the X
            user = int(input("Choose your square:\n 1 2 3 \n 4 5 6 \n 7 8 9 : "))
            # check if user has entered valid cell or not
            if (user > 0 ) and (user < 10):
                   # convert the user input into row and column to fill the user entered cell
                if user == 1:
                    row = 0
                    col = 0
                elif user == 2:
                    row = 0
                    col = 1
                elif user == 3:
                    row = 0
                    col = 2
                elif user == 4:
                    row = 1
                    col = 0
                elif user == 5:
                    row = 1
                    col = 1
                elif user == 6:
                    row = 1
                    col = 2
                elif user == 7:
                    row = 2
                    col = 0
                elif user == 8:
                    row = 2
                    col = 1
                else:
                    row = 2
                    col = 2
                terminate = True  # if user input is valid break the loop 

        # print error message in case of invalid input
        except ValueError:
            print("Invalid Input")
        
        # dispaly error in case of any unexpected error
        except Exception as error:
            print(f"Error:{error}")
        
    # return row and col
    return row, col


def choose_computer_move(board):
    try:
        # develop code to let the computer chose a cell to put a nought in
        computer = random.randint(1,9)
        if computer == 1:
            row = 0
            col = 0
        elif computer == 2:
            row = 0
            col = 1
        elif computer == 3:
            row = 0
            col = 2
        elif computer == 4:
            row = 1
            col = 0
        elif computer == 5:
            row = 1
            col = 1
        elif computer == 6:
            row = 1
            col = 2
        elif computer == 7:
            row = 2
            col = 0
        elif computer == 8:
            row = 2
            col = 1
        else:
            row = 2
            col = 2
    except Exception as error:
        print(f"Error:{error}")
    # return row and col
    return row, col

def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    return False

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    return True
        
def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    # then draw the board
    # then in a loop, get the player move, update and draw the board
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    #repeat the loop
    return 0
                    
                
def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    return choice


def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    return leaders
    
def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    return


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    pass