import random

class Game: # 게임 클래스
    def __init__(self, boardSize, mineCount):
        if mineCount > boardSize * boardSize:
            return
        mineList = set()
        self.boardSize = boardSize
        self.board = []

        # 폭탄의 위치를 선정합니다.
        while len(mineList) < mineCount:
            mineList.add((random.randrange(0, boardSize), random.randrange(0, boardSize)))

        # 보드를 만듭니다.
        
    
    def startGame(self):
        self.printBoard()
#        while len(mineList) > 0: # 지뢰가 0개 이하가 될때까지 무한루프
#            pass
    
    def printBoard(self):
        for i in self.board:
            for j in self.board[i]:
                print(self.board[i][j].toString(), end = ' ')
            print('')

class Field: # 필드 하나 클래스
    MINE = -1

    def __init__(self, fieldType):
        self.fieldType = fieldType # fieldType : 해당 위치에 보여줄 숫자.
        self.flag = False
        self.open = False
    
    def toString(self):
        if self.open:
            return self.fieldType
        else:
            if self.flag:
                return 'F'
            else:
                return '.'

game = Game(9, 10)
game.startGame()