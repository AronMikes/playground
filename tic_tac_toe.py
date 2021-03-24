import random
import re

print("""              _                            _        
__      _____| | ___ ___  _ __ ___   ___  | |_ ___  
\ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \ 
 \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |
  \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/ 
                                                    
 _____ ___ ____   _____  _    ____   _____ ___  _____ 
|_   _|_ _/ ___| |_   _|/ \  / ___| |_   _/ _ \| ____|
  | |  | | |       | | / _ \| |       | || | | |  _|  
  | |  | | |___    | |/ ___ \ |___    | || |_| | |___ 
  |_| |___\____|   |_/_/   \_\____|   |_| \___/|_____|\n\n\n""")


board={'tl':'', 'tm':'', 'tr':'',
       'ml':'', 'mm':'', 'mr':'',
       'bl':'', 'bm':'', 'br':''}


def printBoard(a_board): #shows the board
    print(a_board['tl']+'|'+a_board['tm']+'|'+a_board['tr'])
    print('-+-+-')
    print(a_board['ml']+'|'+a_board['mm']+'|'+a_board['mr'])
    print('-+-+-')
    print(a_board['bl']+'|'+a_board['bm']+'|'+a_board['br'])


player_name=input('Hello! What is your name? \n:') # the mark of the player
bot_mark='' # the mark of the bot
player_mark=''
print(f"Welcome, {player_name}!")

def chooseMark(): #lets a player choose X or O as their mark
    global bot_mark
    global player_mark
    
    player_mark=input(F"Type 'X' or 'O' to choose your mark. \n:")
    
    if player_mark.upper()=='X':
        player_mark='X'
        bot_mark='O'
    elif player_mark.upper()=='O':
        player_mark='X'
        bot_mark='X'
    else:bot_mark=''

while bot_mark=='': #if no mark is chosen, ask the player again
    chooseMark()

print(f"You are playing as {player_mark} and I play as {bot_mark}.\n")
printBoard(board)

counter=0

def playermove():
    global board
    global counter #count number of turns
    global won
    playable_fields=[]
    playable_board=board #clone existing board
    for field, mark in playable_board.items(): #get fields with no marks
        if not mark=='X' and not mark=='O':
            playable_fields.append(field)
            if len(playable_fields)==0: #if no more valid moves left
                won=2
    move_made=input("""
Where do you want to put your mark?
(Type 'help' if you are unsure how to play).\n:""")
    if move_made.lower()=='help': #show the player how to play
        print("""
Type 'tl', 'tm' or 'tr' for the top-left, top-middle or top-right field.
Type 'ml', 'mm' or 'mr' for  the mid-left, center or mid-right field.
Type 'bl', 'bm' or 'br' for the bottom-left, bottom-middle or bottom-right field.""")
        playermove()
    elif move_made in playable_fields: #if valid field selected: overwrite
        board[move_made]=player_mark
        counter+=1
        printBoard(board)
    else:
        print('\nInvalid entry. Please try again.')
        playermove()

def botmove():
    print('\nMy move:\n')
    global counter #count number of turns
    global board
    global won
    playable_fields=[]
    playable_board=board #clone existing board
    for field, mark in playable_board.items(): #get fields with no marks
        if not mark=='X' and not mark=='O':
            playable_fields.append(field)
    if len(playable_fields)==0:
        won=2
    else:
        move_made=random.choice(playable_fields)
        board[move_made]=bot_mark
        counter+=1
        printBoard(board)

won=0 #if won= 1 the player has won, if won=-1 the bot has won, 2 is a draw

marks_top_row=[]
marks_middle_row=[]
marks_bottom_row=[]

def get_rows():
    global board
    global marks_top_row
    global marks_middle_row
    global marks_bottom_row
    marks_top_row=[] #deletes previous marks from last round
    marks_middle_row=[]  #deletes previous marks from last round
    marks_bottom_row=[]  #deletes previous marks from last round
    top_row=[ field for field, mark in board.items() if field.startswith('t')] #fields in top row
    middle_row=[ field for field, mark in board.items() if field.startswith('m')] #fields in middle row
    bottom_row=[ field for field, mark in board.items() if field.startswith('b')] #fields in bottom row
    for field in top_row:
        marks_top_row.append(board[field]) #fill marks in top row
    for field in middle_row:
        marks_middle_row.append(board[field]) #fill marks in middle row
    for field in bottom_row:
        marks_bottom_row.append(board[field]) #fill marks in middle row

def check_if_row_won(row): #check if any row was won
    global won
    global bot_mark
    global player_mark
    if all(mark == row[0] for mark in row) and row[0]==bot_mark:#if row all bot_mark
        won=-1
    if all(mark == row[0] for mark in row) and row[0]==player_mark:#if row all player_mark    
        won=1

def check_if_col_won(): #check if any column was won
    global won
    global bot_mark
    global player_mark
    global marks_top_row
    global marks_middle_row
    global marks_bottom_row
    for i in range(3):
        if marks_top_row[i] == marks_middle_row[i] == marks_bottom_row[i] and marks_bottom_row[i] == bot_mark:
            won=-1
        elif marks_top_row[i] == marks_middle_row[i] == marks_bottom_row[i] and marks_bottom_row[i] == player_mark:
            won=1

def check_if_diag_won(): #check if any diagonal was won
    global won
    global bot_mark
    global player_mark
    global marks_top_row
    global marks_middle_row
    global marks_bottom_row
    if marks_top_row[0] == marks_middle_row[1] == marks_bottom_row[2] and marks_bottom_row[2] == bot_mark:
        won=-1
    elif marks_top_row[2] == marks_middle_row[1] == marks_bottom_row[0] and marks_bottom_row[0] == bot_mark:
        won=-1
    elif marks_top_row[0] == marks_middle_row[1] == marks_bottom_row[2] and marks_bottom_row[2] == player_mark:
        won=1
    elif marks_top_row[2] == marks_middle_row[1] == marks_bottom_row[0] and marks_bottom_row[0] == player_mark:
        won=1


while won==0:
    playermove()
    get_rows()
    check_if_row_won(marks_top_row)
    check_if_row_won(marks_middle_row)
    check_if_row_won(marks_bottom_row)
    check_if_col_won()
    check_if_diag_won()
    botmove()
    get_rows()
    check_if_row_won(marks_top_row)
    check_if_row_won(marks_middle_row)
    check_if_row_won(marks_bottom_row)
    check_if_col_won()
    check_if_diag_won()
    
        
if won==2:
    print("""
  __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
 / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
| (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
 \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
 |___/                                            
   ____  ____      ___        __
  |  _ \|  _ \    / \ \      / /
  | | | | |_) |  / _ \ \ /\ / / 
  | |_| |  _ <  / ___ \ V  V /  
  |____/|_| \_\/_/   \_\_/\_/  """)
elif won==1:
    print("""
  __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
 / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
| (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
 \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
 |___/                                            
__   _____  _   _  __        _____  _   _ 
\ \ / / _ \| | | | \ \      / / _ \| \ | |
 \ V / | | | | | |  \ \ /\ / / | | |  \| |
  | || |_| | |_| |   \ V  V /| |_| | |\  |
  |_| \___/ \___/     \_/\_/  \___/|_| \_|""")
    print(f"\nIt took you {int(counter/2)} rounds.")
elif won==-1:
    print("""
  __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
 / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
| (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
 \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
 |___/                                            
__   _____  _   _   _     ___  ____ _____ 
\ \ / / _ \| | | | | |   / _ \/ ___|_   _|
 \ V / | | | | | | | |  | | | \___ \ | |  
  | || |_| | |_| | | |__| |_| |___) || |  
  |_| \___/ \___/  |_____\___/|____/ |_| """)
    print(f"\nIt took me {int(counter/2)} rounds.")
