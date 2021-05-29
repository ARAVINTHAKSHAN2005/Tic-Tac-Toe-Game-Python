#Function that displays the Board

def display_board(board):

    print('\n'*100)
    #This clears the board every time a new input is entered.   

    
    print(f" { board[7] }  | { board[8] }  | { board[9] }  ")

    print('------------')

    print(f" { board[4] }  | { board[5] }  | { board[6] }  ")

    print('------------')

    print(f" { board[1] }  | { board[2] }  | { board[3] }  ")
    
  
   
    
#Function that takes the player_input 'X'or 'O' 
    
def player_input():
    '''

    OUTPUT = (player1marker,player2marker)
    
    '''
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1 choose 'X' or 'O'  ").upper()
        player1 = marker
        player2 = ''
        
        if player1 == 'X':
            player2 = 'O'
        elif player1 == 'O':
            player2 = 'X'
        else:
            pass
      
        continue            
    return (player1,player2)

# Takes in players position and assigns to board which is a list.

def place_marker(board,marker,position):
    board[position] = marker
    
    
#Function that check if a marker has won and returns True or False.

def win_check(board, mark):
    display_board(board)
    if   board[1] == mark and board[2] == mark and  board[3]== mark:
        return True
            
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
            
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
        
    elif board[2] == mark and board[5] == mark and board[8]== mark:
        return True
        
    elif board[7] == mark and board[5] == mark and  board[3]==mark:
        return True
    
    elif board[7]== mark  and board[8]== mark and  board[9] == mark:
        return True
  
    elif board[9] == mark and board[6] == mark and board[3] == mark:
        return True
            
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True 
             
    else:
        return False
             
#Funcion that randomly pics who goes first

import random

def choose_first():
    player = random.randint(1,2)
    if player == 1:
        return ("Player 1")
    else:
        return ("Player 2")
    
#fucntion which checks if a index position on the board is free returns boolean value 

def space_check(board,position):
    
    return board[position] == ''

#function checks if a space on the board is full

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
            #return true if full
    return True


#asks player for the positon in which to place the marker and returns player_position also validates user input.

def player_choice(board):
    position = "0"
    digitcheck = False
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position) or digitcheck == False:
        position = input("Enter the position in which you want to place you marker: ")
        if position.isdigit() == True:
            digitcheck = True
            if int(position) in [1,2,3,4,5,6,7,8,9]:
                if space_check(board,int(position)):
                    return int(position)
                else:
                    print("Sorry that position is filled")
            else:
                print("Enter a number within range 1 and 9")
        else:
            print("Please Enter a number, not any other charcter whose base is not 10 ")
            

#asks player if they want to play again.

def replay():
    play_game = input("Do you want to play again ? ")
    return play_game.lower()[0] == 'y'
    
print('Welcome to Tic Tac Toe!')



while True:
    
    theboard = ['']*10
    theboard[0] = '#'
    
    player1_marker, player2_marker = player_input() 
    
    #Assigning input of players to variables
    
    print(f"Player 1 chooses {player1_marker}")
    print(f"Player 2 chooses {player2_marker}")

    #choosing players turn 
    turn = choose_first()
    print(f'{turn} gets to go first ')
    play_game = input(f'Are you ready to play {turn}  ? Enter Yes or No ')
    
    if play_game.lower()[0] == 'y':
        game_on_ready = True
    else:
        game_on_ready = False
    


                
    while game_on_ready == True :

        if turn == 'Player 1':
            
            #Displaying Board
        
            display_board(theboard)
            
            #Choose a position 
            
            position = player_choice(theboard)
        
             
            
            #Place the marker on the position
            
            place_marker(theboard,player1_marker,position)
            print(theboard)
            
            #Check if won 
            
            if win_check(theboard,player1_marker) == True:
                display_board(theboard)
                print(f"Player 1 ' {player1_marker} ' has won !")
                game_on_ready = False
                
            else:
            #check if tie 
                if full_board_check(theboard) == True:
                    display_board(theboard)
                    print("The game is a DRAW")
                    break
                    
                else:
            #switch to player 2 
                    turn = "player 2"
                
        else:
            
            #Displaying Board
            
            display_board(theboard)
            
            #Choose a position 
            
            position = player_choice(theboard)
            
            
            #Place the marker on the position
            
            place_marker(theboard,player2_marker,position)
            print(theboard)
            #Check if won 
            
            if win_check(theboard,player2_marker) == True:
                display_board(theboard)
                print(f"Player 2 ' {player2_marker} 'has won !")
                game_on_ready = False
                
            else:
            #check if tie 
                if full_board_check(theboard) == True:
                    display_board(theboard)
                    print("The game is a DRAW !")
                    break
                
                    
                else:
            #switch to player 1
                    turn = "Player 1"

    if not replay():
        print("Thank you for playing ! HOPE YOU HAD FUN ....")
        break       