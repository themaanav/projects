import random
class snake: 
    def __init__(self):
        self.snake = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0)]
        self.direction = "right"
    def get_head(self):
        return self.snake[-1]
    def get_body(self):
        return self.snake
    def checkvalid(self,newposition):
        if newposition in self.snake[:-1]:
            return False
        return True
    def move(self,newposition):
        self.snake.append(newposition)
        print(self.snake)
        if not self.checkvalid(newposition):
            return False
        self.snake.pop(0)
        return True

class game: 
    def __init__(self,width,height):
        assert type(width) == int and type(height) == int
        self.board = []
        self.width = width 
        self.height = height
        self.player = snake()
        for x in range(height):
            self.board.append([])
            for _ in range(width):
                self.board[x].append(None)
        self.count = 0 
    def displayboard(self):
        display_board = [row[:] for row in self.board]
        slicelist = self.player.get_body()
        print(slicelist)
        for slice in slicelist[:-1]:
            x, y = slice
            display_board[x][y] = "o"
        x, y = slicelist[-1]
        display_board[x][y] = "x"
        topedge = "+" + "-" * self.width + "+"
        print(topedge)
        for row in display_board:
            row_str = "|"
            for col in row:
                if col is None:
                    row_str += " " 
                else:
                    row_str += col 
            row_str += "|"
            print(row_str)
        print(topedge)
    def move_is_valid(self):
        x,y = self.player.get_head()
        self.displayboard()
        return True 
    def play(self):
        while True:
            x,y = self.player.get_head()
            userinput = input("w/a/s/d")
            if userinput == "w":
                newposition = (x - 1) % self.height, y 
                if not self.player.move(newposition):
                    break
            if userinput == "a":
                newposition = x, (y - 1) % self.width
                if not self.player.move(newposition):
                    break
            if userinput == "s":
                newposition = (x + 1) % self.height, y 
                if not self.player.move(newposition):
                    break
            if userinput == "d":
                newposition = x, (y + 1) % self.width
                if not self.player.move(newposition):
                    break
            self.displayboard()
        print("you lose!")
            
testgame = game(10,6)
testgame.displayboard()
testgame.play()
print(testgame.board)