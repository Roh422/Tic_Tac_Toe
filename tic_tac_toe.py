def ConstBoard(board):
    print("\n\n")
    for i in range(0,9):
        if((i>0) and (i%3==0)): 
            print("\n")
        if(board[i]==0):
            print("_", end=" ") # if box is empty
        if(board[i]==-1):
            print("X", end=" ") # X== -1
        if(board[i]==1):
            print("O", end=" ") # O== 1
    print("\n\n")

def User1Turn(board):           # it will ask conti until user enters valid position
    while True: 
        pos = input("Enter X's position from [1,2,3,...9]")
        pos= int(pos)
        if(pos>0 and pos <10 and board[pos-1]==0):
            break
        else:
            print("Please Enter a valid position")    
    board[pos-1]=-1

def User2Turn(board):
    while True:
        pos = input("Enter O's position from [1,2,3,...9]")
        pos= int(pos)
        if(pos>0 and pos <10 and board[pos-1]==0):
            break
        else:
            print("Please Enter a valid position")
    board[pos-1]=1

def analyzeboard(board):
    cb = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    for i in range(0,8):
        if(board[cb[i][0]] !=0 and
           board[cb[i][0]]==board[cb[i][1]] and
           board[cb[i][0]]==board[cb[i][2]]):
            return board[cb[i][0]]
    return 0

def minmax(board, player): #here player value will be either 1 or -1
    #first we will check if somebody is won or not
    x=analyzeboard(board)
    if(x!=0):
        return(x*player) # return negative score if current player loosing else positive 
    pos = -1
    value= -2
    for i in range(0,9):
        if(board[i]==0):
            board[i]= player 
            #player * -1 switches the player between X (-1) and O (1)
            score =-minmax(board, player*-1) # -1 is of X and it is his turn now
            #The score returned by the opponent's move (score) is negated since we are evaluating the board from the perspective of the current player
            board[i]=0 # Undo the move to explore other possible moves
            if(score>value):
                value= score
                pos=i
    if(pos==-1):
        return 0 # # If no available moves, return 0 (draw)
    return value


def CompTurn(board):
    pos = -1
    value= -2
    for i in range(0,9):
        if(board[i]==0):
            board[i]=1  #computer played
            score =-minmax(board, -1) # -1 is of X and it is his turn now
            board[i]=0
            if(score>value):
                value= score
                pos=i
    board[pos]=1
        

def main():
    while True:
        choice = input("Enter 1 for Sinlge Player, 2 for Multiplayer: ")
        choice = int(choice)
        board = [0,0,0,0,0,0,0,0,0]
        if(choice==1):
            print("Computer: O, You: X")
            player = input("Enter 1 to play 1st, 2 to play 2nd: ")
            player=int(player)
            for i in range(0,9):
                if(analyzeboard(board)!=0):
                    break
                if((i+player)%2==0):
                    CompTurn(board)
                else:
                    ConstBoard(board) # showing board to user
                    User1Turn(board)
        else:
            for i in range(0,9):
                if(analyzeboard(board)!=0):
                    break
                if((i)%2==0):
                    ConstBoard(board)
                    User1Turn(board)
                else:
                    ConstBoard(board)
                    User2Turn(board)

        x= analyzeboard(board)
        if(x==0):
            ConstBoard(board)
            print("Draw")
        if(x==1):
            ConstBoard(board)
            print("Player O wins!! X Looses!")
        
        if(x==-1):
            ConstBoard(board)
            print("Player X wins!! O Looses!")
        play_again = input("Do you want to play again? (Press Enter to play again, or any other key to quit): ")
        if not play_again:
            continue
        else:
            break


if __name__ == "__main__":
    main()


            
