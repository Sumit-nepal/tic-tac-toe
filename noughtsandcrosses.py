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
    user = None  # initialize terminate with initial value of False
    while user is None:
        try:
            # prompt user where they want to put the X
            user = int(input("Choose your square:\n 1 2 3 \n 4 5 6 \n 7 8 9 : "))
            # check if user has entered valid cell or not
            if not (user > 0 ) and (user < 10):
                print("number should be between 1 to 9")
        
        # print error message in case of invalid input
        except ValueError:
            print("Invalid Input")
        
        # catch any error if it occurs
        except Exception as error:
            print(f"Error:{error}")
        
        # convert the user input into row and column to fill the user entered cell
        row = (user - 1) // 3
        col = (user - 1) % 3
    # return row and col
    return row, col

def choose_computer_move(board):
    try:
        # generate random number from 1-9
        computer = random.randint(1,9)

        # convert the number into row and colum to fill in "O"
        row = (computer - 1) // 3
        col = (computer - 1) % 3

    # catch error in case of any
    except Exception as error:
        print(f"Error:{error}")
    # return row and col
    return row, col

def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # check row
    for row in range(3):
        if board[row][0] == mark and board[row][1] == mark and board[row][2] == mark: 
            return True
    
    # check columns
    for col in range(3):
        if board[0][col] == mark and board[1][col] == mark and board[2][col] == mark: 
            return True
    
    # check diagnols
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    

    # if no one wins return false
    return False

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # check row
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True
    
        
def play_game(board):
    # develop code to play the game
    # start with a call to the initialise_board(board) function to set
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
    # prompt the user for their choice
    option = ["1","2","3","q"]
    terminate = False  # initialize terminate as fasle
    while not terminate:
        try:
            choice = input("""Enter one of the following option:
            1- Play the game
            2- Save your score in the leaderboard
            3- Load and display the leaderboard
            q- End the program
            1,2,3 or q?  """)
            # check if user has entered the valid option
            if choice not in option:
                print("Invalid option")   
            else:
                terminate = not terminate 
        except Exception as error:
            print(f"Error: {error}")
     
    return choice


def load_scores():
    # initialize an empty dictionary
    leaders = {}

    # open file and read player name and score
    try:
        with open("leaderboard.txt","r") as file:
            data = json.load(file)
            leaders = {name:int(score)for name, score in data.items()}
    
    # handle any exception that may occur
    except (PermissionError,FileNotFoundError,EOFError,ValueError) as error:
        print(f"Error: {error}")
    
    return leaders
load_scores()

def save_score(score):
    # prompt user for their name
    name = str(input("Enter your name: "))

    # open the existing leaderboard
    try:
        with open("leaderboard.txt","r") as file:
            data = json.load(file)
    except (PermissionError,EOFError,ValueError) as error:
        print(f"Error: {error}")
    
    # if there is no file create a leaderboard list
    except FileNotFoundError:
        data = []
    
    # add new score to a leaderboard
    data.append({
        "name" : name,
        "score" : score
    })

    # save user name and score in file
    with open("leaderboard.txt","w") as file:
        json.dump("data",file)
    
    print("Name and score saved!!")
    


# def display_leaderboard(leaders):
#     # develop code to display the leaderboard scores
#     # passed in the Python dictionary parameter leader
#     pass