# All the importing
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
import random

# Code to add widgets will go here
window = tk.Tk()
window.title("Tic Tac Toe Board")
window.configure(bg = "white")

# define font size
myFont = font.Font(size="12")

#Assigning values to variables to be refrenced in future code
theboard = ['']*10
theboard[0] = '#'
marker = ''
player1_marker = ''
player2_marker = ''
turn = ''

#Function that takes in user input
def player_input():
    '''
    OUTPUT = (player1marker,player2marker)
    '''
    
    user_input = Entry1.get()
    marker = str(user_input)
    marker = marker.upper()
    print('User has entered :',marker)
    player1 = str(marker)
    player2 = ''
        
    if player1 == 'X':
        player2 = 'O'
        return player1,player2
    elif player1 == 'O':
        player2 = 'X'
        return player1,player2
    else:
        pass 
        
#Function that randomly pics who goes first

def choose_first():
    player = random.randint(1,2)
    if player == 1:
        return "Player 1"
    else:
        return "Player 2"

#fucntion which checks if a index position on the board is free returns boolean value 

def space_check(board,position):
    return board[position] == ''

#function checks whether the board is full

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
            #return true if full
    return True

#Function checks if marker has won 

def win_check(board, mark):
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
       
#Labels that go in the top row of winddow(left)
Label1 = tk.Label(window,text ="Player 1 :")
Label1.config(font=("Courier", 15))
Label1.grid(row=0,column=0)

#Main textbox that dispalys instruction goes in the middle 
DisplayMain = tk.Text(master =window,width = 25,height = 3)
DisplayMain.insert(0.0, 'Click the Button to Start\nPlaying ')
DisplayMain.config(state = 'disabled')
DisplayMain.grid(row = 0, column = 1)

#Widget that takes in user input 
Entry1 = tk.Entry(master = window)
Entry1.grid(row=1,column=1)

#Labels that go in the top row of winddow(right)
Label2 = tk.Label(window,text ="Player 2 :")
Label2.config(font=("Courier", 15))
Label2.grid(row=0,column=2)

#Function that takes in the marker entered in the Entry Widget and makes game related variable assignmenets.
def executer(button_new):
    global user_input,Label1,Label2,turn,player1_marker, player2_marker

    user_input = Entry1.get()

    (player1_marker,player2_marker) = player_input() 
        
    Label1['text'] = "Player 1 :" + player1_marker
    Label2['text'] = "Player 2 :" + player2_marker
    #choosing players turn 
    turn = choose_first()
    #Assigning input of players to variables
    DisplayMain.config(state='normal')
    DisplayMain.insert(0.0,'\n'*10)
    DisplayMain.insert(0.0,f'{turn} gets to go first\nStart Playing- {turn}')
    DisplayMain.config(state='disabled')

    #dissables button so it is not double clicked
    button_new.config(state = 'disabled')


#This funcion gives the user instructions

def button_user_entry_instruction(button_new):
    DisplayMain.config(state='normal')
    DisplayMain.insert(0.0,'Welcome to Tic-Tac-Toe,\nType X or O,\nthen press the button !\n')
    DisplayMain.config(state ='disabled')
    button_new.config(command = lambda: executer(Button10))

#This is the main game code

def buttonclicked(button,board,position):
    global turn,theboard

    print(button,'is clicked' )

    while True:
        #Checks player turn 
        if turn == 'Player 1':
            #board value assignment 
            board[position] = player1_marker
            #Displays marker on button 
            button['text'] =  player1_marker
            button['fg'] = 'blue'
            #This just prints the board at every step
            print(theboard)

            #Check if won 
            if win_check(theboard,player1_marker) == True:
                        print(f"Player 1 ' {player1_marker}' has won !")
                        #Text Box changing text displayed
                        DisplayMain.config(state='normal')
                        DisplayMain.insert(0.0,'\n'*10)
                        DisplayMain.insert(0.0,f"Player 1 ' {player1_marker}' has won !")
                        DisplayMain.config(state ='disabled')
                        #Message box pop up 
                        messagebox.showinfo("Game Message", f"Player 1 ' {player1_marker}' has won !")
                        
                        #Dissables all the buttons once result is declared
                        Button1.config(state='disable')
                        Button2.config(state='disable')
                        Button3.config(state='disable')
                        Button4.config(state='disable')
                        Button5.config(state='disable')
                        Button6.config(state='disable')
                        Button7.config(state='disable')
                        Button8.config(state='disable')
                        Button9.config(state='disable')
                        break
                    
            else:
                #check if tie 
                if full_board_check(theboard) == True:
                    print("The Game is a DRAW !")
                    #Text Box changing text displayed
                    DisplayMain.config(state='normal')
                    DisplayMain.insert(0.0,'\n'*10)
                    DisplayMain.insert(0.0,"The Game is a DRAW")
                    DisplayMain.config(state ='disabled')
                    #Message box pop up 
                    messagebox.showinfo("Game Message", "The Game is a DRAW !")        
                    break 

                else:
                    turn = 'Player 2'
                    break

        elif turn == 'Player 2':
            #board value assignment 
            board[position] = player2_marker
            #Displays marker on button
            button['text'] =  player2_marker
            button.config(fg = 'red')
            #This prints the board at every step
            print(theboard)
    
            #Check if won
            if win_check(theboard,player2_marker) == True:
                        print(f"Player 2 ' {player2_marker}' has won !")
                        #Text Box changing text displayed
                        DisplayMain.config(state='normal')
                        DisplayMain.insert(0.0,'\n'*10)
                        DisplayMain.insert(0.0,f"Player 2 ' {player2_marker}' has won !")
                        DisplayMain.config(state ='disabled')
                        #Message box pop up 
                        messagebox.showinfo("Game Message", f"Player 2 '{player2_marker}' has won !")
                        
                        #Dissables all the buttons once result is declared
                        Button1.config(state='disable')
                        Button2.config(state='disable')
                        Button3.config(state='disable')
                        Button4.config(state='disable')
                        Button5.config(state='disable')
                        Button6.config(state='disable')
                        Button7.config(state='disable')
                        Button8.config(state='disable')
                        Button9.config(state='disable')
                        break
                    
            else:
                #check if tie 
                if full_board_check(theboard) == True:
                    print("The Game is a DRAW !")
                    #Text Box changing text displayed
                    DisplayMain.config(state='normal')
                    DisplayMain.insert(0.0,'\n'*10)
                    DisplayMain.insert(0.0,"The Game is a DRAW")
                    DisplayMain.config(state ='disabled')
                    #Message box pop up 
                    messagebox.showinfo("Game Message", "The game is a DRAW !")         
                    break
     
                else:
                #switch to player 1      
                    turn = "Player 1"
                    break         
        else:
            #When there is some sort of unexpexted button press
            print("Unexpected button press")
            break
                
    
#All buttons being assigned a variable name 
        
Button1 = tk.Button(window,border = 5,width = 25,height = 10, text = '',fg ='red', font =myFont, command= lambda: buttonclicked(Button1,theboard,1)) 
Button1.grid(row=2,column=0)

Button2 = tk.Button(window,border = 5,width = 25,height = 10, text = '',fg ='red',font =myFont, command= lambda: buttonclicked(Button2,theboard,2))
Button2.grid(row=2,column=1)

Button3 = tk.Button(window,border = 5,width = 25,height = 10, text = '',fg = 'red',font =myFont, command= lambda: buttonclicked(Button3,theboard,3))
Button3.grid(row=2,column=2)

Button4 = tk.Button(window,border = 5,width = 25,height = 10, text = '',fg = 'red',font =myFont, command= lambda: buttonclicked(Button4,theboard,4))
Button4.grid(row=3,column=0)

Button5 = tk.Button(window,border = 5,width = 25,height = 10, text = '',fg = 'red', font =myFont,command= lambda: buttonclicked(Button5,theboard,5))
Button5.grid(row=3,column=1)

Button6 = tk.Button(window,border = 5,width = 25,height = 10, text = '',fg = 'red', font =myFont,command= lambda: buttonclicked(Button6,theboard,6))
Button6.grid(row=3,column=2)

Button7 = tk.Button(window,border = 5,width = 25,height = 10, text = '',fg = 'red',font =myFont, command= lambda: buttonclicked(Button7,theboard,7))
Button7.grid(row=4,column=0)

Button8 = tk.Button(window,border = 5,width = 25,height = 10, text = '',fg = 'red',font =myFont, command= lambda: buttonclicked(Button8,theboard,8))
Button8.grid(row=4,column=1)

Button9 = tk.Button(window,border = 5,width = 25,height = 10, text = '',fg = 'red', font =myFont,command= lambda: buttonclicked(Button9,theboard,9))
Button9.grid(row=4,column=2)

#Start game button 
Button10 = tk.Button(window,border = 5,width = 30,height=3, text="START GAME",fg = 'red',font = ('Times New Roman',10),command = lambda: button_user_entry_instruction(Button10))
Button10.grid(row=5,column=1)

#This keeps the window displayed continuously 
window.mainloop()