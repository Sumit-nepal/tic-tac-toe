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
    # update elements of the board list to ' '
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    
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
            else:
                # convert the user input into row and column to fill the user entered cell
                row = (user - 1) // 3
                col = (user - 1) % 3
                # return row and col
                return row, col
        
        # print error message in case of invalid input
        except ValueError:
            print("Invalid Input")
        
        # catch any error if it occurs
        except Exception as error:
            print(f"Error:{error}")
        

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
    
def update_board(board, move, mark):
    row, col = move
    board[row][col] = mark
 
def play_game(board):
    """
    Play a game of tic-tac-toe.
    """
    initialise_board(board)
    draw_board(board)
    
    terminate = False  # initialize terminate as false
    outcome = None  # initialize outcome as None
    while not terminate:
        # Player's move
        player_mark = 'X'
        print("Player's turn (mark: {})".format(player_mark))
        move = get_player_move(board)
        update_board(board, move, player_mark)
        draw_board(board)

        # Check if player has won
        win = check_for_win(board, player_mark)
        if win:
            print("Player wins!")
            outcome = 1
            terminate = True
       
        # Check for a draw
        if check_for_draw(board):
            print("Draw!")
            outcome = 0
            terminate = True

        if not terminate:
            # Computer's move
            computer_mark = 'O'
            print("Computer's turn (mark: {})".format(computer_mark))
            move = choose_computer_move(board)
            update_board(board, move, computer_mark)
            draw_board(board)

            # Check if computer has won
            if check_for_win(board, computer_mark):
                print("Computer wins!")
                outcome = -1
                terminate = True
    
    return outcome  # return the outcome of the game


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
    leaders = {}
    try:
        with open("leaderboard.txt", "r") as file:
            data = json.load(file)
            for item in data:
                name = item.get("name", "")
                score_str = item.get("score", "")
                try:
                    score = int(score_str)
                    leaders[name] = score
                except ValueError:
                    print(f"Invalid score for {name}: {score_str}")
    except (PermissionError, FileNotFoundError, EOFError) as error:
        print(f"Error: {error}")
    return leaders

def save_score(score):
    # prompt user for their name
    name = input("Enter your name: ")

    # initialize an empty list to save player name and score
    data = []

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
        json.dump(data,file)
    
    print("Name and score saved!!")


def display_leaderboard(leaders):
    # iterate through each items in dictionary and print them
    try:
        for key, value in leaders.items():
            print(key,value)
    
    # catch and print the error in case of any
    except Exception as error:
        print(f"Error: {error}")