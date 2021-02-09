from tkinter import *
from client import Client
#anytimes u want want to use something from a class you need to make an object for it
class Buttons():

    def __int__(self, master):
        frame = Frame(master)
        frame.pack()
        self.printButton = Button(frame, text= "Print Message", command =self.printMessage)
        self.printButton.pack(side = LEFT)

        self.quitButton = Button(frame, text= "Quit", command =frame.quit) # breaks the mainloop and closes gui
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow, this actually worked")
###################################################### Lobby class finished ################################
class Lobby():
    def __init__(self, master, w, h): #Master is the tk() container/program that canvas will be placed on
        self.width = w #width of canvas
        self.height = h #height of canvas
        self.screen = Canvas(master, width= self.width, height= self.height, bg="black") #self.screen will be canvas creation itself
        self.screen.pack() #packing canvas onto root


    def getLobby(self):
        return self.screen


    def drawLobbyBackground(self):
        # Place background image for lobby
        self.bg_img = PhotoImage(file = "Images/starz.png")
        self.screen.create_image(0, 0, anchor= NW, image = self.bg_img)



####################################    Player class completed  #######################################
class Player():
    def __init__(self, x, y, screen, file):
        self.startingx = x #starting x coordinate
        self.startingy = y #starting y coordinate
        self.screen = screen #What canvas player will be placed on
        self.color = file #File path that will determine color of player
        self.rate = 10 ##coordinate points


    def draw(self):#returns img used for moving
        self.bg_img = PhotoImage(file = self.color)
        return (self.screen.getLobby()).create_image(0, 0, anchor=NW, image=self.bg_img) #this will now take the canvas object from the lobby instance and allow u to paint on it

    def moveCoord(self, img, directKey):
        if directKey == 0:  # right
            x = 10
            y = 0
            self.startingx = self.startingx + self.rate  # keeping track of corrdinates to send to server and keep track
            (self.screen.getLobby()).move(img, x, y)# what actually makes the move on the canvas
        elif directKey == 1:  # left
            x = -10
            y = 0

            self.startingx = self.startingx - self.rate  # keeping track of corrdinates to send to server and keep track
            (self.screen.getLobby()).move(img, x, y)
        elif directKey == 2:  # up
            x = 0
            y = -10
            self.startingy = self.startingy - self.rate  # keeping track of corrdinates to send to server and keep track
            (self.screen.getLobby()).move(img, x, y)
        else:  # down
            x = 0
            y = 10
            self.startingy = self.startingy + self.rate  # keeping track of corrdinates to send to server and keep track
            (self.screen.getLobby()).move(img, x, y)

########################################## Enemy Bot class  ##################
class Enemy():

    def __init__(self, x, y, screen, file, end):
        self.startingx = x  # starting x coordinate
        self.startingy = y  # starting y coordinate
        self.screen = screen  # What canvas player will be placed on
        self.color = file  # File path that will determine color of player
        self.rate = 10  ##coordinate points
        self.endCoord = end
        self.path = [self.startingx, self.endCoord]  # represents where we are starting and where we are ending
        self.walkCount = 0

    def draw(self):#returns img used for moving
        self.bg_img = PhotoImage(file = self.color)
        return (self.screen.getLobby()).create_image(0, 0, anchor=NW, image=self.bg_img) #this will now take the canvas object from the lobby instance and allow u to paint on it

    #Still need to implement
    def movex(self, img):
        if self.rate > 0:
            if self.startingx + self.rate < self.path[1]:
                x = 10
                y = 0
                self.startingx = self.startingx + self.rate
                (self.screen.getLobby()).move(img, x, y)  # what actually makes the move on the canvas
            else:
                self.rate = self.rate * -1
                self.walkCount = 0

        else:
            if self.startingx - self.rate > self.path[0]:
                x = 10
                y = 0
                self.startingx = self.startingx + self.rate
                (self.screen.getLobby()).move(img, x, y)  # what actually makes the move on the canvas
            else:
                self.rate = self.rate * -1
                self.walkCount = 0


######### GUI CLASS        GUI CLASS           GUI CLASS            GUI CLASS #########################

class Gui():
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.network = Client()
        self.root = Tk()
        self.my_canvas = Lobby(self.root, w, h)
        self.player1 = Player(0, 0, self.my_canvas, "Images/cyan.png")
        self.img1 = self.player1.draw()
        self.player2 = Player(50, 50, self.my_canvas, "Images/orange.png")
        self.img2 = self.player2.draw()

    # will get info from server in a form we can understand so we can then draw the other character
    @staticmethod
    def parseData(data):
        try:
            arr = data.split(":")[1].split(",")
            return int(arr[0]), int(arr[1])
        except:
            return -1, -1

    # this is what will send ur current position in certain form to the server
    def sendData(self):
        data = str(self.network.id) + ":" + str(self.player1.startingx) + "," + str(self.player1.startingy)
        reply = self.network.sendData(data)
        return reply
    #Player 1 keyboard movements use regular up, down, left, right keys
    def left(self, event):
        self.player1.moveCoord(self.img1, 1)
    def right(self, event):
        self.player1.moveCoord(self.img1, 0)
    def up(self, event):
        self.player1.moveCoord(self.img1, 2)
    def down(self, event):
        self.player1.moveCoord(self.img1, 3)

    # Player 2 keyboard movements use W,A,S,D keys
    def left2(self, event):
        self.player2.moveCoord(self.img2, 1)
    def right2(self, event):
        self.player2.moveCoord(self.img2, 0)
    def up2(self, event):
        self.player2.moveCoord(self.img2, 2)
    def down2(self, event):
        self.player2.moveCoord(self.img2, 3)

    def run(self):
        running = True
        while running:
            # This is the key event in tkinter version for player 1
            self.root.bind("<Right>", self.right)  # if -> arrow key pressed activate
            self.root.bind("<Left>", self.left)  # if <- arrow key pressed activate
            self.root.bind("<Up>", self.up)
            self.root.bind("<Down>", self.down)

            # This is the key event in tkinter version for player 2
            self.root.bind("<d>", self.right2)  # if -> arrow key pressed activate
            self.root.bind("<a>", self.left2)  # if <- arrow key pressed activate
            self.root.bind("<w>", self.up2)
            self.root.bind("<s>", self.down2)



            # Send Network data
            self.player2.startingx, self.player2.startingy = self.parseData(self.sendData())

            self.root.mainloop()


root = Tk()
network = Client()
my_canvas = Lobby(root, 695, 530)
my_canvas.drawLobbyBackground()#remeber my_canvas is not a canvas object it is a Lobby object
#Creating player 1
player1 = Player(0, 0, my_canvas, "Images/cyan.png")
img = player1.draw()
#Creating player 2
player2 = Player(50, 50, my_canvas, "Images/orange.png")
img2 = player2.draw()

def left(event):
    player1.moveCoord(img, 1)
def right(event):
    player1.moveCoord(img, 0)
def up(event):
    player1.moveCoord(img, 2)
def down(event):
    player1.moveCoord(img, 3)

# Player 2 keyboard movements use W,A,S,D keys
def left2(event):
    player2.moveCoord(img2, 1)
def right2(event):
   player2.moveCoord(img2, 0)
def up2(event):
    player2.moveCoord(img2, 2)
def down2(event):
    player2.moveCoord(img2, 3)





#This is the key event in tkinter version
root.bind("<Right>", right) # if -> arrow key pressed activate
root.bind("<Left>", left) # if <- arrow key pressed activate
root.bind("<Up>", up)
root.bind("<Down>", down)

# This is the key event in tkinter version for player 2
root.bind("<d>", right2)  # if -> arrow key pressed activate
root.bind("<a>", left2)  # if <- arrow key pressed activate
root.bind("<w>", up2)
root.bind("<s>", down2)

root.mainloop()

