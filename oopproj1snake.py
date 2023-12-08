import random
class snake: 
    def __init__(self,width,height):
        self.snake = [((height-1)//2,(width-1)//2),((height-1)//2,(width-1)//2 + 1)]
        self.direction = "right"
        self.fruit = self.generatefruit(width,height)
        self.width = width
        self.height = height
        self.count = 0 
    def get_head(self):
        return self.snake[-1]
    def get_body(self):
        return self.snake
    def checkvalid(self,newposition):
        if newposition in self.snake[:-1]:
            return False
        return True
    def generatefruit(self,width,height):
        y = random.randint(0,width-1)
        x = random.randint(0,height-1)
        pos = (x,y)
        while pos in self.snake:
            y = random.randint(0,width)
            x = random.randint(0,height)
            pos = (x,y)
        return pos
    def getfruit(self):
        return self.fruit
    def getcount(self):
        return self.count
    def move(self,newposition):
        self.snake.append(newposition)
        if not self.checkvalid(newposition):
            return False
        if not self.fruit == newposition:
            self.snake.pop(0)
        else:
            self.fruit = self.generatefruit(self.width,self.height)
            self.count += 1 
        return True

class game: 
    def __init__(self,height,width):
        assert type(width) == int and type(height) == int
        self.board = []
        self.width = width 
        self.height = height
        self.player = snake(width,height)
        for x in range(height):
            self.board.append([])
            for _ in range(width):
                self.board[x].append(None)
    def displayboard(self):
        display_board = [row[:] for row in self.board]
        slicelist = self.player.get_body()
        i, j = self.player.getfruit()
        display_board[i][j] = "@" 
        for slice in slicelist[:-1]:
            x, y = slice
            display_board[x][y] = "o"
        x, y = slicelist[-1]
        display_board[x][y] = "x"
        topedge = "+" + "-" * self.width + "+"
        print(f"Score: {self.player.getcount()}")
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
    def play(self):
        self.displayboard()
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

testgame = game(11,50)
testgame.play()
