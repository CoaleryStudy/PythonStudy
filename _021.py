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
        
        # 각 칸의 숫자를 적용합니다.
        for i in range(boardSize):
            for j in range(boardSize):
                if not self.board[i][j].isMine():
                    self.board[i][j].setFieldType(self.calculateLoc(i, j))
    
    def startGame(self):
        try:
            while self.correctMineSelectCount < self.mineCount: # 지뢰가 0개 이하가 될때까지 무한루프
                self.printBoard()
                selX, selY = self.inputPosition()
                self.selectPosition(selX, selY)
        except KeyboardInterrupt:
            print("게임 강제 종료")
    
    def inputPosition(self):
        while True: # 제대로 된 값이 입력될 때 까지 무한루프
            try:
                x, y = map(int, input('움직이려는 위치 입력 : ').split())
                break
            except ValueError:
                pass
        return x, y

    def selectPosition(self, x, y):
        if self.board[x][y].isOpen(): # 이미 다녀간 위치라면 리턴
            return
        self.board[x][y].openField() # 해당 필드를 연다
        if self.board[x][y].getFieldType() != 0: # 해당 필드 주위에 폭탄이 없다면 리턴 (더 이상 전진할 필요가 없다.)
            return
        
        if x + 1 < self.boardSize:
            self.selectPosition(x+1, y)
        if x - 1 >= 0:
            self.selectPosition(x-1, y)
        if y + 1 < self.boardSize:
            self.selectPosition(x, y+1)
        if y - 1 >= 0:
            self.selectPosition(x, y-1)

    def printBoard(self): # 보드 출력
        print('\n' * 10)
        print('  │', end = '')
        for i in range(self.boardSize):
            print(i, end = ' ')
        print('')
        print('──┼' + '──' * self.boardSize)
        for i in range(self.boardSize):
            print(i, '│', end = '')
            for j in range(self.boardSize):
                print(self.board[i][j].toString(), end = ' ')
            print('')

    def calculateLoc(self, x, y):
        target = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        result = 0

        for calTarget in target:
            dx = calTarget[0]
            dy = calTarget[1]
            if (0 <= x + dx < self.boardSize) and (0 <= y + dy < self.boardSize):
                if self.board[x + dx][y + dy].isMine():
                    result += 1

        return result

class Field: # 필드 하나 클래스
    MINE = 9

    def __init__(self):
        self.fieldType = 0 # fieldType : 해당 위치에 보여줄 숫자.
        self.flag = False
        self.open = False
    
    def setFieldType(self, fieldType):
        self.fieldType = fieldType
    
    def getFieldType(self):
        return self.fieldType

    def openField(self):
        self.open = True
    
    def flagFieldToggle(self):
        if not self.open:
            self.flag = not self.flag
    
    def isOpen(self):
        return self.open

    def isMine(self):
        return (self.fieldType == Field.MINE)
    
    def toString(self):
        if self.open:
            if self.fieldType == Field.MINE:
                return '*'
            else:
                return self.fieldType
        else:
            if self.flag:
                return 'F'
            else:
                return '.'

game = Game(9, 10)
game.startGame()