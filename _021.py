import random

class Game: # 게임 클래스
    def __init__(self, boardSize, mineCount):
        if mineCount > boardSize * boardSize:
            return
        mineList = set()
        self.boardSize = boardSize
        self.board = []
        self.correctMineSelectCount = 0
        self.mineCount = mineCount

        # 폭탄의 위치를 선정합니다.
        while len(mineList) < mineCount:
            mineList.add((random.randrange(0, boardSize), random.randrange(0, boardSize)))

        # 보드를 만듭니다.
        for _ in range(boardSize):
            rowList = []
            for __ in range(boardSize):
                rowList.append(Field())
            self.board.append(rowList)

        # 지뢰의 위치를 보드에 적용합니다.
        for minePoint in mineList:
            x = minePoint[0]
            y = minePoint[1]
            self.board[x][y].setFieldType(Field.MINE)
        
        self.printBoard()
    
    def startGame(self):
        self.printBoard()
        while self.correctMineSelectCount < self.mineCount: # 지뢰가 0개 이하가 될때까지 무한루프
            pass
    
    def printBoard(self):
        print('  ', end = '')
        for i in range(self.boardSize):
            print(i, end = ' ')
        print('')
        for i in range(self.boardSize):
            print(i, end = ' ')
            for j in range(self.boardSize):
                print(self.board[i][j].toString(), end = ' ')
            print('')

class Field: # 필드 하나 클래스
    MINE = 9

    def __init__(self):
        self.fieldType = 0 # fieldType : 해당 위치에 보여줄 숫자.
        self.flag = False
        self.open = True
    
    def setFieldType(self, fieldType):
        self.fieldType = fieldType
    
    def toString(self):
        if self.open:
            return self.fieldType
        else:
            if self.flag:
                return 'F'
            else:
                return '.'

game = Game(9, 10)
#game.startGame()