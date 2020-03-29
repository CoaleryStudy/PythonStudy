import random

class Game: # 게임 클래스
    def __init__(self, boardSize, mineCount):
        if mineCount > boardSize * boardSize:
            return
        self.mineList = set()
        self.boardSize = boardSize
        self.board = []

        while len(self.mineList) < mineCount:
            self.mineList.add((random.randrange(0, boardSize), random.randrange(0, boardSize)))
    
    def startGame(self):
        self.printBoard()
        while len(self.mineList) > 0: # 지뢰가 0개 이하가 될때까지 무한루프
            pass
    
    def printBoard(self):
        for i in self.board:
            for j in self.board[i]:
                print(self.board[i][j], end = ' ')
            print('')

game = Game(9, 10)
game.startGame()