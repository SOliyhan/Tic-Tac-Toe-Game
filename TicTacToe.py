#Tic Tac Toe board game
#Developed by Shivanshu Oliyhan



#board data
board= ["-","-","-",
        "-","-","-",
        "-","-","-"]

#check if game is over
game_still_going= True

#tells who is winner
winner= None

#Tells the current player ("X go first")
current_player="X"

#play a game
def play_game():
    #show intial game board
    display_board()
    #loop until game ends
    while game_still_going:
        #handle turn
        handle_turn(current_player)
        #if game is over
        check_if_game_over()
        #flip to other player
        flip_player()
    #since game is over, print win or tie
    if winner== "X" or winner== "O":
        print(winner+ " won.")
    elif winner== None:
        print("Tie.")
            
#display board to screen
def display_board():
    print("\n")
    print(" "+board[0]+" | "+board[1]+" | "+board[2]+"     1 | 2 | 3")
    print(" "+board[3]+" | "+board[4]+" | "+board[5]+"     4 | 5 | 6")
    print(" "+board[6]+" | "+board[7]+" | "+board[8]+"     7 | 8 | 9")
    print("\n")

#handle turn for random player
def handle_turn(player):
    #set global var we need to edit
    global winner
    
    #get position from player
    print(player+"'s turn.")
    position=input("Choose a position from 1-9: ")

    #whatever the user input, it must be valid
    valid= False
    while not valid:
        #make sure input is valid
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            positon= input("Choose a position from 1-9: ")
        #get correct index in board list
        position= int(position)-1

        #make sure spot is available on the board
        if board[position]== "-":
            valid=True
        else:
            print("You can't go there. Go again.")

    #put game piece on board
    board[position]=player
    
    #show the game board
    display_board()

#check for game is over
def check_if_game_over():
    check_for_winner()
    check_for_tie()

#check to see if someone has won
def check_for_winner():
    global winner
    #check if there was winner anywhere
    row_winner= check_rows()
    column_winner= check_columns()
    diagonal_winner= check_diagonals()

    #get the winners
    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None

#check rows for a win
def check_rows():
    global game_still_going
    #check if any of rows have all same value(and is noT empty)
    row_1=board[0]==board[1]==board[2]!="-"
    row_2=board[3]==board[4]==board[5]!="-"
    row_3=board[6]==board[7]==board[8]!="-"

    #if any row have a maTch, flag thaT there is a win
    if row_1 or row_2 or row_3:
        game_still_going=False
    #return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    #or return none if there was no winner
    else:
        return None

#check columns for a win
def check_columns():
    global game_still_going
    column_1=board[0]==board[3]==board[6]!="-"
    column_2=board[1]==board[4]==board[7]!="-"
    column_3=board[2]==board[5]==board[8]!="-"

    if column_1 or column_2 or column_3:
        game_still_going=False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None

#check diagonals for win
def check_diagonals():
    global game_still_going
    diagonal_1=board[0]==board[4]==board[8]!="-"
    diagonal_2=board[2]==board[4]==board[6]!="-"

    if diagonal_1 or diagonal_2:
        game_still_going= False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None

#check if there is tie
def check_for_tie():
    global game_stil_going
    #if board is full then tie
    if "-" not in board:
        game_still_going=False
        return True
    #else there is no tie
    else:
        return False

#flip the current player from X to O, or O to X
def flip_player():
    global current_player
    #if currenT is X then make it O
    if current_player== "X":
        current_player= "O"
    #if current is O then make it X
    elif current_player== "O":
        current_player= "X"

#play game
play_game()
