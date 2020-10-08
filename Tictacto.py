#tic tac toe
from random import randint
def display_board(board):
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("----------")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("----------")
    print(board[7]+"|"+board[8]+"|"+board[9])
    
def check_win(board,position,player1=0,player2=0):
    if player1!=0:
        mark=player1
        board[position]=mark
        display_board(board)
        z=-1
    
        if(player1=="x"):
        #board[position]=mark
            if position==1:
                if ((board[1]==board[2]==board[3]=="x") or (board[1]==board[4]==board[7]=="x") or (board[1]==board[5]==board[9]=="x")):
                    print("x wins")
                    z=1
            elif position==2:
                if((board[1]==board[2]==board[3]=="x") or (board[2]==board[5]==board[8]=="x")):
                    print("x wins")
                    z=1
            elif position==3:
                if((board[1]==board[2]==board[3]=="x") or (board[3]==board [5]==board[7]=="x") or (board[3]==board[6]==board[9]=="x")):
                    print("player 1 wins")
                    z=1
            elif position==4:
                if ((board[4]==board[1]==board[7]=="x") or (board [4]==board[5]==board[6]=="x") ):
                    print("x wins ")
                    z=1
            elif position==5:
                if ((board[5]==board[2]==board[8]=="x") or (board[5]==board[4]==board[6]=="x") or (board[5]==board[3]==board[7]=="x") or (board[1]==board[5]==board[9]=="x")):
                    print("x wins ")
                    z=1
            elif position==6:
                if ((board[6]==board[5]==board[4]=="x") or (board[3]==board [6]==board[9]=="x")):
                    print("x wins")
                    z=1
            elif position ==7:
                if((board[1]==board[4]==board[7]=="x") or (board[7]==board [5]==board[3]=="x") or (board[7]==board[8]==board[9]=="x")):
                    print("x wins")
                    z=1
            elif position==8:
                if((board[8]==board[5]==board[2]=="x") or (board[8]==board [7]==board[9]=="x")):
                    print("x wins")
                    z=1
            elif position==9:
                if ((board[9]==board[5]==board[1]=="x") or (board[9]==board [8]==board[7]=="x") or (board[9]==board[6]==board[3]=="x")):
                    print("x wins")
                    z=1
    else: 
        mark=player2
        board[position]=mark
        
        if position==1:
            if ((board[1]==board[2]==board[3]=="0") or (board[1]==board[4]==board[7]=="0") or (board[1]==board[5]==board[9]=="0")):
                print("0 wins")
                z=1
                
        if position==2:
            if((board[1]==board[2]==board[3]=="0") or (board[2]==board[5]==board[8]=="0")):
                print("0 wins")
                z=1
        if position==3:
            if((board[1]==board[2]==board[3]=="0") or (board[3]==board [5]==board[7]=="0") or (board[3]==board[6]==board[9]=="0")):
                print("player 1 wins")
                z=1
        if position==4:
            if ((board[4]==board[1]==board[7]=="0") or (board [4]==board[5]==board[6]=="0")):
                print("0 wins ")
                z=1
        if position==5:
            if ((board[5]==board[2]==board[8]=="0") or (board[5]==board[4]==board[6]=="0") or (board[5]==board[3]==board[7]=="0") or (board[1]==board[5]==board[9]=="0")):
                print("0 wins ")
                z=1
        if position==6:
            if ((board[6]==board[5]==board[4]=="0") or (board[3]==board [6]==board[9]=="0")):
                print("0 wins")
                z=1
        if position ==7:
            if((board[1]==board[4]==board[7]=="0") or (board[7]==board [5]==board[3]=="0") or (board[7]==board[8]==board[9]=="0")):
                print("0 wins")
                z=1
        if position==8:
            if((board[8]==board[5]==board[2]=="0") or (board[8]==board [7]==board[9]=="0")):
                print("0 wins")
                z=1
        if position==9:
            if ((board[9]==board[5]==board[1]=="0") or (board[9]==board [8]==board[7]=="0") or (board[9]==board[6]==board[3]=="0")):
                print("0 wins")
                z=1
    return z
        
           
            
    

my_list=["  "]*10
string1="x"
print("WELCOME TO TIC TAC TOE GAME")  
print("player1 is x")
print("player2 is 0")
player1="x"
player2="0"
key=-1

b=randint(0,1)
if b==0:
    print("player 1 goes first")
else:
    print("player 2 goes fist")

while key==-1:
    
    # display_board(my_list)
    c=input("player1 enter your position")
    key=check_win(my_list,c,player1)
    print("_________________________")
    if key==-1:
        d=input("player2 enter your position")
        key=check_win(my_list,d,player2)
        print("_____________________________")
    
         #   print("game over ")
 
    