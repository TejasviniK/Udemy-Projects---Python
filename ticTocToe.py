import sys

n = 0
win = 0
loss = 0
board = list()
cellcount = 0

def boardFull():
    return not cellcount < n*n

def play(player) :
    global cellcount
    successplace = False            
    while(not successplace) :
        while True :
            try :
                c1, c2 = map(int,input("{} : Enter the cell values".format(player)).split())
            except Exception:
                print("Warning :Please enter proper cell values <row column> !")
            else :
                break
        if(checkAvailability(c1-1,c2-1)) :
            board[c1-1][c2-1] = player
            successplace = True
            cellcount += 1
            displayBoard()
            endgame = verifyWin()
            if(endgame) :
                print("Game Over! {} Won the game!".format(player))
                sys.exit()
        else :
            print("{} : Cell not available, try other".format(player))
            displayBoard()    

def checkAvailability(i,j) :
    if (i not in range(n)) or (j not in range(n)) or (board[i][j] != " ") :
        return False
    else :
        return True

def displayBoard() :
    print("-"+"-"*2*n)
    for i in range(n) :
        print("|", end="")
        for j in range(n) :
            print(board[i][j], end="|")
        print("\n"+"-"+"-"*2*n)
        #print("\n")
    #print(board)

def verifyWin() :
    global win

    # Check row wise
    for i in range(n):
        if " " in board[i][0:n] :
            continue
        else :
            item = board[i][0]
            for j in range(1,n) :
                if board[i][j] != item :
                    win = 0
                    break
                else :
                    win = 1
            if(win) :
                return win
        
    #check column wise
    for j in range(n) :
        col = list()
        for i in range(n):
            col.append(board[i][j])
        if " " in col :
            continue
        else :
            item = col[0]
            for c in range(1,len(col)) :
                if col[c] != item :
                    win = 0
                    break
                else :
                    win = 1
            if(win) :
                return win

    #check diagonally
    item = board[0][0]
    for i, j in zip(range(1,n),range(1,n)) :
        if(item == " " or board[i][j] == " " or board[i][j] != item) :
            win = 0
            break
        else :
            win = 1
    if(win) :
        return win
    
    item = board[0][n-1]
    for i, j in zip(range(1,n),range(1,-1,-1)) :
        if(item == " " or board[i][j] == " " or board[i][j] != item) :
            win = 0
            break
        else :
            win = 1
    if(win) :
        return win

    return win

        
if __name__ == "__main__":
    
    print("Welcome to the amazing tic tac toe game!!")

    while True :
        try :
            n = int(input("Please enter the value for the grid :"))
        except Exception :
            print("Warning : Please Enter integer value!")
            continue
        else :
            break

    board = [[" "] * n for i in range(n)]
    #board = [['0', '0', 'x'], ['0', 'x', 'x'], ['B', '0', '0']]
    displayBoard()

    
    #print("Win = ", verifyWin())
    endgame = 0
    while(not boardFull()) :
        play("X")
        if(not boardFull()) :
            play("0")
    print("It's a Tie!! Board Full!")
    
            

