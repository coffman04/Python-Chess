import turtle
from tkinter import *
from tkinter import ttk

class Chessboard:
    def __init__(self):
        self.pieces = []

    def addPiece(self, piece):
        self.pieces.append(piece)

    def containsPiece(self, rank, file):
        for piece in self.pieces:
            if piece.rank == rank and piece.file == file:
                return True
        return False

    def pieceContained(self, rank, file):
        if(self.containsPiece(rank,file)):
            for piece in self.pieces:
                if piece.rank == rank and piece.file == file:
                    return piece
        else:
            return "no piece"

    def drawPieces(self, t):
        for piece in self.pieces:
            piece.draw(t)

    def capture(self, captured):
        for piece in self.pieces:
            if piece is captured:
                self.pieces.remove(piece)
        

class Piece:
    def __init__(self, w, rank, file):
        self.isWhite = w
        self.rank = rank
        self.file = file
        self.type = "general"

    def isFriendly(self, otherPiece):
        if (self.isWhite == otherPiece.isWhite):
            return True
        return False

    def draw(self,t):
        t.up()
        t.goto(1000,1000)
        t.stamp()

    def setFile(self, f):
        self.file = f

    def setRank(self, r):
        self.rank = r

class Pawn(Piece):
    def __init__(self, w, rank, file):
        self.isWhite = w
        self.rank = rank
        self.file = file
        self.moved = False
        self.type = "pawn"

    def validMove(self, board):
        #creates and returns a list full of all the valid moves an individual pawn can make
        #this function does not move the piece
        validMoves = []
        if(self.isWhite):
            if(not board.containsPiece(self.rank+1, self.file)):
                validMoves.append(numToFile(self.file)+str(self.rank+1))
                if((not board.containsPiece(self.rank+2, self.file)) and (not self.moved)):
                    validMoves.append(numToFile(self.file)+str(self.rank+2))
            if(board.containsPiece(self.rank+1, self.file+1) and not self.isFriendly(board.pieceContained(self.rank+1, self.file+1))):
                validMoves.append(numToFile(self.file)+"x"+numToFile((self.file+1))+str(self.rank+1))
            if(board.containsPiece(self.rank+1, self.file-1) and not self.isFriendly(board.pieceContained(self.rank+1, self.file-1))):
                validMoves.append(numToFile(self.file)+"x"+numToFile((self.file-1))+str(self.rank+1))
        else:
            if(not board.containsPiece(self.rank-1, self.file)):
                validMoves.append(numToFile(self.file)+str(self.rank-1))
                if((not board.containsPiece(self.rank-2, self.file)) and (not self.moved)):
                    validMoves.append(numToFile(self.file)+str(self.rank-2))
            if(board.containsPiece(self.rank-1, self.file+1) and not self.isFriendly(board.pieceContained(self.rank-1, self.file+1))):
                validMoves.append(numToFile(self.file)+"x"+numToFile((self.file+1))+str(self.rank-1))
            if(board.containsPiece(self.rank-1, self.file-1) and not self.isFriendly(board.pieceContained(self.rank-1, self.file-1))):
                validMoves.append(numToFile(self.file)+"x"+numToFile((self.file-1))+str(self.rank-1))

        return validMoves

    def draw(self, t):
        t.up()
        t.goto((self.file-1)*100 - 400, (self.rank-1)*100 - 400)
        t.seth(90)
        t.forward(10)
        t.rt(90)
        t.forward(15)
        t.seth(0)
        t.down()
        if(self.isWhite):
            t.color("black","old lace")
        else:
            t.color("black","saddle brown")
        t.begin_fill()
        for i in range(2):
            t.forward(70)
            t.left(90)
            t.forward(15)
            t.left(90)
        t.rt(90)
        t.end_fill()
        t.up()
        t.backward(15)
        t.lt(90)
        t.down()
        t.begin_fill()
        t.circle(25,90)
        t.forward(15)
        t.rt(90)
        t.fd(20)
        t.rt(90)
        t.fd(15)
        t.circle(25,90)
        t.rt(180)
        t.fd(70)
        t.end_fill()
        t.up()
        t.rt(90)
        t.fd(35)
        t.rt(90)
        t.fd(35)
        t.down()
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        

class Bishop(Piece):
    def __init__(self, w, rank, file):
        self.isWhite = w
        self.rank = rank
        self.file = file
        self.type = "bishop"

    def validMove(self, board):
        validMoves = []
        for i in range(1, min(8-self.rank, 8-self.file)+1):
            if(not board.containsPiece(self.rank+i, self.file+i)):
                validMoves.append("B"+numToFile(self.file+i)+str(self.rank+i))
            elif(not self.isFriendly(board.pieceContained(self.rank+i, self.file+i))):
                validMoves.append("Bx"+numToFile(self.file+i)+str(self.rank+i))
                break
            else:
                break
        for i in range(1, min(8-self.rank+1, self.file)):
            if(not board.containsPiece(self.rank+i, self.file-i)):
                validMoves.append("B"+numToFile(self.file-i)+str(self.rank+i))
            elif(not self.isFriendly(board.pieceContained(self.rank+i, self.file-i))):
                validMoves.append("Bx"+numToFile(self.file-i)+str(self.rank+i))
                break
            else:
                break
        for i in range(1, min(self.rank, 8-self.file+1)):
            if(not board.containsPiece(self.rank-i, self.file+i)):
                validMoves.append("B"+numToFile(self.file+i)+str(self.rank-i))
            elif(not self.isFriendly(board.pieceContained(self.rank-i, self.file+i))):
                validMoves.append("Bx"+numToFile(self.file+i)+str(self.rank-i))
                break
            else:
                break
        for i in range(1, min(self.rank, self.file)):
            if(not board.containsPiece(self.rank-i, self.file-i)):
                validMoves.append("B"+numToFile(self.file-i)+str(self.rank-i))
            elif(not self.isFriendly(board.pieceContained(self.rank-i, self.file-i))):
                validMoves.append("Bx"+numToFile(self.file-i)+str(self.rank-i))
                break
            else:
                break
        return validMoves

    def draw(self,t):
        if(self.isWhite):
            t.color("black","old lace")
        else:
            t.color("black","saddle brown")
        t.up()
        t.goto((self.file-1)*100 - 400, (self.rank-1)*100 - 400)
        t.goto(t.xcor()+50, t.ycor()+10)
        t.seth(90+60)
        t.down()
        t.begin_fill()
        for i in range(120):
            if(i==100):
                t.rt(90)
                t.fd(10)
                t.backward(10)
                t.lt(90)
            t.fd(.8)
            t.rt(1)
        t.seth(270+60)
        for i in range(120):
            t.fd(.8)
            t.rt(1)
        t.end_fill()
        t.up()
        t.goto(t.xcor()-50,t.ycor()-10)
        t.seth(90)
        t.fd(10)
        t.rt(90)
        t.fd(15)
        t.down()
        t.begin_fill()
        t.fd(70)
        t.lt(90)
        t.fd(15)
        t.lt(90)
        t.fd(70)
        t.lt(90)
        t.fd(15)
        t.end_fill()
        
            

class Knight(Piece):
    def __init__(self, w, rank, file):
        self.isWhite = w
        self.rank = rank
        self.file = file
        self.type = "knight"

    def validMove(self, board):
        validMoves = []
        for i in range(-2,3,1):
            for j in range(-2,3,1):
                if(abs(i)+abs(j)==3):
                    if(0<self.rank+i<9 and 0<self.file+j<9):
                        if(not board.containsPiece(self.rank+i, self.file+j)):
                            validMoves.append("N"+numToFile(self.file+j)+str(self.rank+i))
                        elif(not self.isFriendly(board.pieceContained(self.rank+i, self.file+j))):
                            validMoves.append("Nx"+numToFile(self.file+j)+str(self.rank+i))
                        
        return validMoves

    def draw(self, t):
        if(self.isWhite):
            t.color("black","old lace")
        else:
            t.color("black","saddle brown")
        t.up()
        t.goto((self.file-1)*100 - 400, (self.rank-1)*100 - 400)
        t.goto(t.xcor()+80, t.ycor()+20)
        t.begin_fill()
        t.down()
        t.seth(180)
        t.rt(105)
        for i in range(90):
            t.fd(1.05)
            t.lt(i**.5/5)
            
        t.seth(145)
        t.fd(20)
        t.seth(285)
        t.fd(20)
        t.seth(210)
        t.fd(30)
        t.lt(90)
        t.fd(18)
        t.lt(100)
        t.fd(20)
        t.rt(90)
        while(t.ycor()>(self.rank-1)*100+32 - 400):
            t.fd(.5)
            t.rt(1)
        while(t.ycor()>(self.rank-1)*100+20 - 400):
            t.fd(.5)
            t.lt(1)
        t.goto(t.xcor()+60, t.ycor())
        t.end_fill()
        t.up()
        t.goto(t.xcor()-54, t.ycor()+56)
        t.down()
        t.circle(3)
        t.up()
        t.goto((self.file-1)*100 - 400, (self.rank-1)*100 - 400)
        t.seth(90)
        t.up()
        t.fd(10)
        t.rt(90)
        t.fd(15)
        t.down()
        t.begin_fill()
        t.fd(75)
        t.lt(90)
        t.fd(10)
        t.lt(90)
        t.fd(75)
        t.lt(90)
        t.fd(10)
        t.end_fill()

    

class Rook(Piece):
    def __init__(self, w, rank, file):
        self.isWhite = w
        self.rank = rank
        self.file = file
        self.type = "rook"
        self.moved = False

    def validMove(self, board):
        validMoves = []
        for i in range(1, self.rank):
            if(not board.containsPiece(self.rank-i, self.file)):
                validMoves.append("R"+numToFile(self.file)+str(self.rank-i))
            elif(not self.isFriendly(board.pieceContained(self.rank-i, self.file))):
                validMoves.append("Rx" + numToFile(self.file)+str(self.rank-i))
                break
            else:
                break
        for i in range(1, 8-self.rank+1):
            if(not board.containsPiece(self.rank+i, self.file)):
                validMoves.append("R"+numToFile(self.file)+str(self.rank+i))
            elif(not self.isFriendly(board.pieceContained(self.rank+i, self.file))):
                validMoves.append("Rx" + numToFile(self.file)+str(self.rank+i))
                break
            else:
                break
        for i in range(1, self.file):
            if(not board.containsPiece(self.rank, self.file-i)):
                validMoves.append("R"+numToFile(self.file-i)+str(self.rank))
            elif(not self.isFriendly(board.pieceContained(self.rank, self.file-i))):
                validMoves.append("Rx" + numToFile(self.file-i)+str(self.rank))
                break
            else:
                break
        for i in range(1, 8-self.file+1):
            if(not board.containsPiece(self.rank, self.file+i)):
                validMoves.append("R"+numToFile(self.file+i)+str(self.rank))
            elif(not self.isFriendly(board.pieceContained(self.rank, self.file+i))):
                validMoves.append("Rx" + numToFile(self.file+i)+str(self.rank))
                break
            else:
                break
        return validMoves

    def draw(self, t):
        t.seth(90)
        t.up()
        t.goto((self.file-1)*100 - 400, (self.rank-1)*100 - 400)
        if(self.isWhite):
            t.color("black","old lace")
        else:
            t.color("black","saddle brown")
        t.fd(10)
        t.rt(90)
        t.fd(10)
        t.down()
        t.begin_fill()
        t.fd(80)
        t.lt(90)
        t.fd(10)
        t.lt(90)
        t.fd(80)
        t.lt(90)
        t.fd(10)
        t.end_fill()
        t.back(10)
        t.lt(90)
        t.begin_fill()
        t.fd(5)
        t.lt(90)
        t.fd(10)
        t.rt(90)
        t.fd(70)
        t.rt(90)
        t.fd(10)
        t.rt(90)
        t.fd(70)
        t.rt(90)
        t.end_fill()
        t.up()
        t.rt(90)
        t.fd(5)
        t.lt(90)
        t.fd(10)
        t.down()
        t.begin_fill()
        t.fd(40)
        t.rt(90)
        t.fd(60)
        t.rt(90)
        t.fd(40)
        t.rt(90)
        t.fd(60)
        t.rt(90)
        t.fd(40)
        t.lt(90)
        t.fd(10)
        t.rt(90)
        t.fd(20)
        for i in range(3):
            t.rt(90)
            t.fd(20)
            t.rt(90)
            t.fd(10)
            if i<2:
                t.lt(90)
            t.fd(10)
            if i<2:
                t.lt(90)
            else:
                t.rt(90)
            t.fd(10)
        t.end_fill()
            
                 
                

class Queen(Piece):
    def __init__(self, w, rank, file):
        self.isWhite = w
        self.rank = rank
        self.file = file
        self.type = "queen"

    def validMove(self, board):
        r = Rook(self.isWhite, self.rank, self.file)
        b = Bishop(self.isWhite, self.rank,self.file)
        rMoves = r.validMove(board)
        bMoves = b.validMove(board)
        validMovesUnnamed = rMoves+bMoves
        del r
        del b
        validMoves = []
        for move in validMovesUnnamed:
            validMoves.append("Q"+move[1:])
        return validMoves
    
    def draw(self, t):
        t.seth(90)
        t.up()
        t.goto((self.file-1)*100 - 400, (self.rank-1)*100 - 400)
        if(self.isWhite):
            t.color("black","old lace")
        else:
            t.color("black","saddle brown")
        t.fd(20)
        t.rt(90)
        t.fd(20)
        t.down()
        t.begin_fill()
        t.fd(60)
        t.rt(90)
        t.fd(10)
        t.rt(90)
        t.fd(60)
        t.rt(90)
        t.fd(10)
        t.end_fill()
        t.begin_fill()
        t.goto(t.xcor()-10, t.ycor()+50)
        t.goto(t.xcor()+17.5, t.ycor()-30)
        t.goto(t.xcor()-5, t.ycor()+40)
        t.goto(t.xcor()+17.5, t.ycor()-40)
        t.goto(t.xcor()+10, t.ycor()+50)
        t.goto(t.xcor()+10, t.ycor()-50)
        t.goto(t.xcor()+17.5, t.ycor()+40)
        t.goto(t.xcor()-5, t.ycor()-40)
        t.goto(t.xcor()+17.5, t.ycor()+30)
        t.goto(t.xcor()-10, t.ycor()-50)
        t.end_fill()

class King(Piece):
    def __init__(self, w, rank, file):
        self.isWhite = w
        self.rank = rank
        self.file = file
        self.type = "king"
        self.moved = False

    def inCheck(self, board):
        #check for rook/queen(moving like rook) check
        for i in range(1, self.rank):
            if(board.containsPiece(self.rank-i, self.file)):
                if(not self.isFriendly(board.pieceContained(self.rank-i, self.file))):
                    p = board.pieceContained(self.rank-i,self.file).type
                    if(p == "rook" or p == "queen"):
                        #is this what i want to return
                        return True
                    else:
                        break
                else:
                    break
        for i in range(1, 8-self.rank+1):
            if(board.containsPiece(self.rank+i, self.file)):
                if(not self.isFriendly(board.pieceContained(self.rank+i, self.file))):
                    p = board.pieceContained(self.rank+i,self.file).type
                    if(p == "rook" or p == "queen"):
                        #is this what i want to return
                        return True
                    else:
                        break
                else:
                    break
        for i in range(1, self.file):
            if(board.containsPiece(self.rank, self.file+i)):
                if(not self.isFriendly(board.pieceContained(self.rank, self.file+i))):
                    p = board.pieceContained(self.rank,self.file+i).type
                    if(p == "rook" or p == "queen"):
                        #is this what i want to return
                        return True
                    else:
                        break
                else:
                    break
        for i in range(1, 8-self.file+1):
            if(board.containsPiece(self.rank, self.file+i)):
                if(not self.isFriendly(board.pieceContained(self.rank, self.file+i))):
                    p = board.pieceContained(self.rank,self.file+i).type
                    if(p == "rook" or p == "queen"):
                        #is this what i want to return
                        return True
                    else:
                        break
                else:
                    break
        #checks for bishop, queen(moving like a bishop) or pawn
        for i in range(1, min(8-self.rank, 8-self.file)+1):
            if(board.containsPiece(self.rank+i, self.file+i)):
                if(not self.isFriendly(board.pieceContained(self.rank+i, self.file+i))):
                    p = board.pieceContained(self.rank+i,self.file+i).type
                    if(p == "bishop" or p == "queen" or(i==1 and p == "pawn")):
                        #is this what i want to return
                        return True
                    else:
                        break
                else:
                    break
        for i in range(1, min(8-self.rank+1, self.file)):
            if(board.containsPiece(self.rank+i, self.file-i)):
                if(not self.isFriendly(board.pieceContained(self.rank+i, self.file-i))):
                    p = board.pieceContained(self.rank+i,self.file-i).type
                    if(p == "bishop" or p == "queen" or(i==1 and p == "pawn")):
                        #is this what i want to return
                        return True
                    else:
                        break
                else:
                    break
        for i in range(1, min(self.rank, 8-self.file+1)):
            if(board.containsPiece(self.rank-i, self.file+i)):
                if(not self.isFriendly(board.pieceContained(self.rank-i, self.file+i))):
                    p = board.pieceContained(self.rank-i,self.file+i).type
                    if(p == "bishop" or p == "queen" or(i==1 and p == "pawn")):
                        #is this what i want to return
                        return True
                    else:
                        break
                else:
                    break
        for i in range(1, min(self.rank, self.file)):
            if(board.containsPiece(self.rank-i, self.file-i)):
                if(not self.isFriendly(board.pieceContained(self.rank-i, self.file-i))):
                    p = board.pieceContained(self.rank-i,self.file-i).type
                    if(p == "bishop" or p == "queen" or(i==1 and p == "pawn")):
                        #is this what i want to return
                        return True
                    else:
                        break
                else:
                    break
        #check for knights
        for i in range(-2,3,1):
            for j in range(-2,3,1):
                if(abs(i)+abs(j)==3):
                    if(0<self.rank+i<8 and 0<self.file+j<8):
                        if(board.containsPiece(self.rank+i, self.file+j)):
                            if(not self.isFriendly(board.pieceContained(self.rank+i, self.file+j))):
                                p = board.pieceContained(self.rank+i, self.file+j).type
                                if(p=="knight"):
                                    return True
        return False

    def validMove(self, board):
        tiles = [[-1,1],[-1,0],[-1,-1],[0,1],[0,-1],[1,1],[1,0],[1,-1]]
        validMoves = []
        for tile in tiles:
            if(9>self.rank+tile[0]>0 and 9>self.file+tile[1]>0):
                if(not board.containsPiece(self.rank+tile[0], self.file+tile[1])):
                    validMoves.append("K"+numToFile(self.file+tile[1])+str(self.rank+tile[0]))
                elif(not self.isFriendly(board.pieceContained(self.rank+tile[0], self.file+tile[1]))):
                    validMoves.append("Kx" + numToFile(self.file+tile[1])+str(self.rank+tile[0]))
        if(not self.moved):
            if(board.containsPiece(self.rank,8) and board.pieceContained(self.rank,8).type == "rook"):
                if(board.pieceContained(self.rank,8).moved == False):
                    if (not board.containsPiece(self.rank,7) and not board.containsPiece(self.rank,6)):
                        validMoves.append("O-O")
            if(board.containsPiece(self.rank,1) and board.pieceContained(self.rank,1).type == "rook"):
                if(board.pieceContained(self.rank,1).moved == False):
                    if (not board.containsPiece(self.rank,4) and not board.containsPiece(self.rank,3) and not board.containsPiece(self.rank,2)):
                        validMoves.append("O-O-O")
                    
            
        return validMoves

    def draw(self, t):
        t.up()
        t.goto((self.file-1)*100 - 400, (self.rank-1)*100 - 400)
        if(self.isWhite):
            t.color("black","old lace")
        else:
            t.color("black","saddle brown")
        for i in range(4):
            t.forward(100)
            t.rt(90)
        t.up()
        t.goto(t.xcor()+10, t.ycor()+10)
        t.down()
        t.begin_fill()
        t.goto(t.xcor()+80, t.ycor())
        t.goto(t.xcor(), t.ycor()+10)
        t.goto(t.xcor()-80, t.ycor())
        t.goto(t.xcor(), t.ycor()-10)
        t.end_fill()
        t.seth(90)
        t.fd(10)
        t.begin_fill()
        t.goto(t.xcor()+30, t.ycor()+35)
        t.goto(t.xcor()+20, t.ycor())
        t.goto(t.xcor()+30, t.ycor()-35)
        t.end_fill()
        t.up()
        t.goto(t.xcor()-50, t.ycor()+35)
        t.down()
        t.begin_fill()
        t.goto(t.xcor()-15, t.ycor()+15)
        t.goto(t.xcor()+50, t.ycor())
        t.goto(t.xcor()-15, t.ycor()-15)
        t.end_fill()
        t.up()
        t.goto(t.xcor()-14, t.ycor()+15)
        t.down()
        t.begin_fill()
        for i in range(4):
            t.fd(8)
            t.lt(90)
            t.fd(8)
            t.rt(90)
            t.fd(8)
            t.rt(90)
        t.end_fill()
    
def changeColor(t,i,j):
    if(i%2 == 0):
        if (j%2 == 0):
            t.color("dim gray")
        else:
            t.color("gainsboro")
    else:
        if (j%2 == 0):
            t.color("gainsboro")
        else:
            t.color("dim gray")

def drawSquare(t,size):
    for i in range(4):
        t.forward(size)
        t.rt(90)
    
def drawBoard(t):
    for i in range(8):
        for j in range(8):
            changeColor(t,i,j)
            t.goto(i*100 - 400,j*100 - 400)
            t.seth(90)
            t.begin_fill()
            drawSquare(t,100)
            t.end_fill()

def numToFile(z):
    numDict = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h"}
    if z in numDict:
        return numDict[z]
    return "invalid file"

def fileToNum(z):
    fileDict = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
    if z in fileDict:
        return fileDict[z]
    return "invalid file"

    


def tryMove(event):
    global cb
    global initial
    global t
    global whTurn
    global movingPiece
    global square
    global square2
    global initial
    x = event.x
    y = event.y
    if(initial):
        square = numToFile((x//100)+1) + str(((800-y)//100)+1)
    else:
        square2 = numToFile((x//100)+1) + str(((800-y)//100)+1)
    if(initial):
        r = (800-y)//100+1
        f = (x//100)+1
        if cb.containsPiece(r, f) and cb.pieceContained(r,f).isWhite==whTurn:
            movingPiece = cb.pieceContained(r,f)
            initial = False
        else:
            print("Pick one of your pieces to move")
    else:
        moves = movingPiece.validMove(cb)
        canMoveS2 = False
        castling = False
        tracker = None
        for move in moves:
            if move[-2:] == square2:
                canMoveS2 = True
                tracker = move
                break
            elif(movingPiece.type == "king" and not movingPiece.moved):
                if(move == "O-O"):
                    if square2 == ("g"+str(movingPiece.rank)):
                        if(movingPiece.inCheck(cb)):
                            print("You cannot castle out of check")
                        else:
                            canMoveS2 = True
                            castling = True
                            tracker = move
                        break
                elif(move == "O-O-O"):
                    if square2 == ("c"+str(movingPiece.rank)):
                        if(movingPiece.inCheck(cb)):
                            print("You cannot castle out of check")
                        else:
                            canMoveS2 = True
                            castling = True
                            tracker = move
                        break
        #checks to make sure you are not putting the king in check
        if(canMoveS2):
            newBoard = Chessboard()
            #creates a fresh board with the state of the next potential move
            for piece in cb.pieces:
                if piece == movingPiece:
                    #if the piece is moving - needs a different initialize
                    continue
                if piece.rank == int(square2[1]) and piece.file == fileToNum(square2[0]):
                    # if the piece is being captured ignore it
                    continue
                if(piece.type=="pawn"):
                    newBoard.addPiece(Pawn(piece.isWhite, piece.rank, piece.file))
                elif(piece.type=="knight"):
                    newBoard.addPiece(Knight(piece.isWhite, piece.rank, piece.file))
                elif(piece.type=="bishop"):
                    newBoard.addPiece(Bishop(piece.isWhite, piece.rank, piece.file))
                elif(piece.type=="rook"):
                    newBoard.addPiece(Rook(piece.isWhite, piece.rank, piece.file))
                elif(piece.type=="queen"):
                    newBoard.addPiece(Queen(piece.isWhite, piece.rank, piece.file))
                elif(piece.type=="king"):
                    newBoard.addPiece(King(piece.isWhite, piece.rank, piece.file))
            if(movingPiece.type=="pawn"):
                newBoard.addPiece(Pawn(movingPiece.isWhite, int(square2[1]), fileToNum(square2[0])))
            elif(movingPiece.type=="knight"):
                newBoard.addPiece(Knight(movingPiece.isWhite,int(square2[1]), fileToNum(square2[0])))
            elif(movingPiece.type=="bishop"):
                newBoard.addPiece(Bishop(movingPiece.isWhite, int(square2[1]), fileToNum(square2[0])))
            elif(movingPiece.type=="rook"):
                newBoard.addPiece(Rook(movingPiece.isWhite, int(square2[1]), fileToNum(square2[0])))
            elif(movingPiece.type=="queen"):
                newBoard.addPiece(Queen(movingPiece.isWhite, int(square2[1]), fileToNum(square2[0])))
            elif(movingPiece.type=="king"):
                newBoard.addPiece(King(movingPiece.isWhite, int(square2[1]), fileToNum(square2[0])))
                if(castling):
                    if move=="O-O":
                        newBoard.addPiece(King(movingPiece.isWhite, int(square2[1]), 6))
                    else:
                        newBoard.addPiece(King(movingPiece.isWhite, int(square2[1]), 4))
            for piece in newBoard.pieces:
                if piece.type == "king" and piece.isWhite == whTurn:
                    if piece.inCheck(newBoard):
                        canMoveS2 = False
                        print("This move would put your king in check")
                        if(castling):
                            print("Your king also cannot castle through check")
                            break
                    if(not castling):
                        break
            for piece in newBoard.pieces:
                del piece
            del newBoard
                    
        #actually moves the piece
        if(canMoveS2):
            global turnCounter
            turnCounter += 1
            global moveList
            moveList.append(tracker)
            r1 = int(square[1])
            f1 = int(fileToNum(square[0]))
            r2 = int(square2[1])
            f2 = int(fileToNum(square2[0]))
            if cb.containsPiece(r2, f2) and (not cb.pieceContained(r2,f2).isWhite==whTurn):
                cb.capture(cb.pieceContained(r2,f2))
                changeColor(t,f2,r2)
                t.goto((f2-1)*100 - 400,(r2-1)*100 - 400)
                t.seth(90)
                t.begin_fill()
                drawSquare(t,100)
                t.end_fill()
            changeColor(t,f1,r1)
            t.goto((f1-1)*100 - 400,(r1-1)*100 - 400)
            t.seth(90)
            t.begin_fill()
            drawSquare(t,100)
            t.end_fill()
            movingPiece.setRank(int(square2[1]))
            movingPiece.setFile(fileToNum(square2[0]))
            movingPiece.draw(t)
            if(castling):
                if (movingPiece.file == 3):
                    for piece in cb.pieces:
                        if piece.type == "rook" and piece.isWhite == movingPiece.isWhite and piece.file == 1:
                            rook = piece
                            rook.file = 4
                            changeColor(t,1,rook.rank)
                            t.up()
                            t.goto((1-1)*100 - 400,(rook.rank-1)*100 - 400)
                            t.seth(90)
                            t.begin_fill()
                            drawSquare(t,100)
                            t.end_fill()
                            t.up()
                            rook.draw(t)
                else:
                    for piece in cb.pieces:
                        if piece.type == "rook" and piece.isWhite == movingPiece.isWhite and piece.file == 1:
                            rook = piece
                            rook.file = 6
                            changeColor(t,8,rook.rank)
                            t.up()
                            t.goto((8-1)*100 - 400,(rook.rank-1)*100 - 400)
                            t.seth(90)
                            t.begin_fill()
                            drawSquare(t,100)
                            t.end_fill()
                            t.up()
                            rook.draw(t)
                            
                    
            t.up()
            t.goto(0,0)
            if(whTurn):
                whTurn = False
            else:
                whTurn = True
            if movingPiece.type == "pawn" or movingPiece.type == "rook" or movingPiece.type == "king":
                movingPiece.moved = True
        else:
            print("The", movingPiece.type, "on", square, "cannot move to", square2, ".")

        movingPiece = None    
        initial = True
        if(whTurn):
            print("It is White's Turn")
            for piece in cb.pieces:
                if piece.isWhite and piece.type == "king":
                    if piece.inCheck(cb):
                        print("White is in check")
        else:
            print("It is Black's Turn")
            for piece in cb.pieces:
                if not piece.isWhite and piece.type == "king":
                    if piece.inCheck(cb):
                        print("Black is in check")
        


    
    



# setup
root = Tk()
root.title('Chess')
root.geometry("800x800")
frame = ttk.Frame(root)
frame.pack()
canvas = Canvas(frame, bg = 'blue', width = 800, height = 800)
canvas.pack()
tScreen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(tScreen)
t.ht()
t.up()
t.speed(0)
t._tracer(0,0)
drawBoard(t)
cb = Chessboard()
for i in range(1,9):
    wpawn = Pawn(True, 2, i)
    bpawn = Pawn(False, 7, i)
    cb.addPiece(wpawn)
    cb.addPiece(bpawn)
for i in range(1,9,7):
    rk1 = Rook(i%2==1, i, 1)
    cb.addPiece(rk1)
    kn1 = Knight(i%2==1, i, 2)
    cb.addPiece(kn1)
    bsh1 = Bishop(i%2==1, i, 3)
    cb.addPiece(bsh1)
    qn = Queen(i%2==1, i, 4)
    cb.addPiece(qn)
    kng = King(i%2==1, i, 5)
    cb.addPiece(kng)
    bsh2 = Bishop(i%2==1, i, 6)
    cb.addPiece(bsh2)
    kn2 = Knight(i%2==1, i, 7)
    cb.addPiece(kn2)
    rk2 = Rook(i%2==1, i, 8)
    cb.addPiece(rk2)
cb.drawPieces(t)
t.up()
t._update()
whTurn = True
initial = True
square = ""
square2 = ""
movingPiece = None
moveList = []
turnCounter = 0
print("It is White's Turn")
canvas.bind("<Button>", tryMove)
canvas.mainloop()
print()
print("Game Log:")
turn = ""
for i in range(turnCounter):
    if i%2 == 0:
        turn += str(i//2 + 1) + "."
        turn += moveList[i]
        for j in range(12 - len(turn)):
            turn+= " "
        if i==(turnCounter-1):
            print(turn)
    else:
        turn += str(i//2 + 1) + "..."
        turn += moveList[i]
        print(turn)
        turn = ""
    
    





