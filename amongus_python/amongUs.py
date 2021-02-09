import sys
import pygame
from client import Client
from pygame import mixer
import random
import os

TIMEOUT = 4  # number of seconds until timeout
clock = pygame.time.Clock()

# timer
current_time = 0

current_time = pygame.time.get_ticks()
print(current_time)
#########################################################################################################################################

class Lobby():

    def __init__(self, w, h, name="None"):
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption(name)
        self.width = w
        self.height = h
        self.walls = []

    def getLobby(self):
        return self.screen

    def drawLobbyBackground(self):
        #Place background image for lobby
        self.screen.fill((0, 0, 1))
        self.bg_img = pygame.image.load('Images/lobbyShip.png').convert() #653x584
        self.screen.blit(self.bg_img, (375,0), self.bg_img.get_rect())
        #draw walls for lobby
        wall = Wall(365, 0, 10, 584) #left wall
        self.walls.append(wall)
        wall = Wall(1038, 0, 10, 584) #right wall
        self.walls.append(wall)
        wall = Wall(375, 584, 653, 10) #bottom wall
        self.walls.append(wall)
        for wall in self.walls:
            pygame.draw.rect(self.screen, ((0, 0, 1)), wall.rect)
        #myfont = pygame.font.SysFont("monspace", 20)
        #self.screen.blit(self.button, self.button.get_rect())

    def drawLobbyBackground2(self):
        self.bg_img = pygame.image.load('Images/serverEntry.png')
        self.screen.blit(self.bg_img, self.bg_img.get_rect())

    def drawPlayerInputLobby(self):
        self.bg_img = pygame.image.load('Images/homeScreen.png').convert_alpha()
        self.screen.blit(self.bg_img, self.bg_img.get_rect())
        # self.screen.fill((0,0,0))

########################################################################################################################################

class Map():

    def __init__(self, w, h, name="None"):
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption(name)
        self.width = w
        self.height = h
        self.walls = []


    def getMap(self):
        return self.screen

    #makes window black and then draws the map walls
    def drawMapBackground(self):
        #fills window with black
        #walls holds every wall instance
        #self.screen.fill((0, 0, 1))

        #walls at borders of window
        wall = Wall(1356, 0, 10, 768)
        self.walls.append(wall)
        wall = Wall(0, 758, 1366, 10)
        self.walls.append(wall)
        wall = Wall(0, 0, 10, 768)
        self.walls.append(wall)
        wall = Wall(0, 0, 1366, 10)
        self.walls.append(wall)
        #top left room (spawn)
        wall = Wall(0, 192, 80, 10)
        self.walls.append(wall)
        wall = Wall(145, 192, 80, 10)
        self.walls.append(wall)
        wall = Wall(225, 0, 10, 202)
        self.walls.append(wall)
        #top right room
        wall = Wall(960, 160, 406, 10)
        self.walls.append(wall)
        wall = Wall(960, 60, 10, 110)
        self.walls.append(wall)
        #middle room
        wall = Wall(350, 250, 200, 10)
        self.walls.append(wall)
        wall = Wall(620, 250, 390, 10)
        self.walls.append(wall)
        wall = Wall(350, 250, 10, 350)
        self.walls.append(wall)
        wall = Wall(350, 590, 590, 10)
        self.walls.append(wall)
        wall = Wall(1000, 250, 10, 350)
        self.walls.append(wall)
        #bottom right room
        wall = Wall(1100, 590, 140, 10)
        self.walls.append(wall)
        wall = Wall(1310, 590, 56, 10)
        self.walls.append(wall)
        wall = Wall(1100, 590, 10, 178)
        self.walls.append(wall)
        #bottom left room
        wall = Wall(0, 330, 120, 10)
        self.walls.append(wall)
        wall = Wall(110, 330, 10, 348)
        self.walls.append(wall)
        wall = Wall(110, 670, 700, 10)
        self.walls.append(wall)
        wall = Wall(800, 670, 10, 30)

        self.walls.append(wall)

        """
        self.button1 = Button(100, 100, 950, 350, Game.map, "red")  # voting buttons
        self.button2 = Button(100, 100, 950, 400, Game.map, "blue")
        self.button3 = Button(100, 100, 950, 450, Game.map, "cyan")
        self.button4 = Button(100, 100, 950, 500, Game.map, "orange")
        """


        # Voting boxes
        pygame.draw.rect(self.screen, (50, 50, 50), [1500, 250, 140, 40])
        pygame.draw.rect(self.screen, (50, 50, 50), [1500, 300, 140, 40])
        pygame.draw.rect(self.screen, (50, 50, 50), [1500, 350, 140, 40])
        pygame.draw.rect(self.screen, (50, 50, 50), [1500, 400, 140, 40])



        for wall in self.walls:
            pygame.draw.rect(self.screen, ((192, 192, 192)), wall.rect)




########################################################################################################################################

# wall class that takes coordinates, width, and height to make rectangle
class Wall(object):
    def __init__(self, x, y, w, h):
        super(Wall, self).__init__()
        self.image = pygame.Surface([w, h])
        self.image.fill((192, 192, 192))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

########################################################################################################################################

class Player(object):

    def __init__(self, startx, starty, w, h, color, colorDead):
        #pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(w, w, h, h)
        self.rect.x = startx
        self.rect.y = starty
        self.rate = 2
        self.height = h  # 48pixels
        self.width = w  # 36pixels
        self.screen = pygame.display.set_mode((w, h))
        self.color = color  # color is not a string it is a pygame.Surface type containing the .png file that will produce character
        self.dead = colorDead
        self.voted = "no vote"
        self.status = "alive"
        self.username = "player 1"
        self.role = "crewmate"

        self.place = object


        self.images = [pygame.image.load(self.color).convert_alpha(), pygame.image.load(self.dead).convert_alpha()]
        self.current_image = self.images[0]

        self.hitbox = (self.rect.x, self.rect.y, 36, 49)

    # directKey parameter will be used to move player instance in certain direction
    def move(self, directKey):
        if directKey == 0:  # right
            self.rect.x = self.rect.x + self.rate
        elif directKey == 1:  # left
            self.rect.x = self.rect.x - self.rate
        elif directKey == 2:  # up
            self.rect.y = self.rect.y - self.rate
        else:  # down
            self.rect.y = self.rect.y + self.rate

        #checks for wall collision and stops player if necessary
        for wall in self.place.walls:
            if self.rect.colliderect(wall.rect):
                if (directKey == 0):
                    self.rect.right = wall.rect.left
                if (directKey == 1):
                    self.rect.left = wall.rect.right
                if (directKey == 2):
                    self.rect.top = wall.rect.bottom
                if (directKey == 3):
                    self.rect.bottom = wall.rect.top


    def draw(self, player):
        self.screen.blit(self.current_image, (self.rect.x, self.rect.y))  # params converted image, starting positions of characters
        self.hitbox = (self.rect.x, self.rect.y, 36, 49)
        #pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox, 2)



########################################################################################################################################

class Enemy(pygame.sprite.Sprite):

    def __init__(self, startx, starty, w, h, end, color, colorDead):
        pygame.sprite.Sprite.__init__(self)
        self.x = startx
        self.y = starty
        self.height = h  # 48pixels
        self.width = w  # 36pixels
        self.end = end
        self.path = [self.x, self.end]  # represents where we are starting and where we are ending
        self.walkCount = 0
        self.rate = 2
        self.screen = pygame.display.set_mode((w, h))
        self.color = color  # color is not a string it is a pygame.Surface type containing the .png file that will produce character
        self.dead = colorDead

        self.images = [pygame.image.load(self.color).convert_alpha(), pygame.image.load(self.dead).convert_alpha()]
        self.current_image = self.images[0]

    def moveX(self):
        if self.rate > 0:
            if self.x + self.rate < self.path[1]:
                self.x = self.x + self.rate
            else:
                self.rate = self.rate * -1
                self.walkCount = 0
        else:
            if self.x - self.rate > self.path[0]:
                self.x = self.x + self.rate
            else:
                self.rate = self.rate * -1
                self.walkCount = 0

    def draw(self, g):
        if self.current_image == self.images[0]:
            self.moveX()
        self.screen.blit(self.current_image, (self.x, self.y))  # params converted image, starting positions of characters

##############################################################################################################################

class Jewel(pygame.sprite.Sprite):

    def __init__(self, startx, starty, w, h, jewelImg, takenImg):
        pygame.sprite.Sprite.__init__(self)
        self.x = startx
        self.y = starty
        self.height = h  #45pixels
        self.width = w  #45pixels
        self.screen = pygame.display.set_mode((w, h))
        self.gem = jewelImg
        self.collected = takenImg
        self.images = [pygame.image.load(self.gem).convert_alpha(), pygame.image.load(self.collected).convert_alpha()]
        self.current_image = self.images[0]

        self.hitbox = (self.x, self.y, 45, 45)


    def draw(self, player):
        if self.current_image == self.images[0]:
            self.screen.blit(self.current_image, (self.x, self.y))
            #pygame.draw.rect(self.screen, (225, 0, 0), self.hitbox, 2)
        else:
            self.screen.blit(self.current_image, (550, 10))
##############################################################################################################################

class Boulder(pygame.sprite.Sprite):

    def __init__(self, startx, starty, w, h, obstacle, destroyed):
        pygame.sprite.Sprite.__init__(self)
        self.x = startx
        self.y = starty
        self.height = h  #72pixels
        self.width = w  #72pixels
        self.screen = pygame.display.set_mode((w, h))
        self.obstacle = obstacle
        self.destroyed = destroyed
        self.images = [pygame.image.load(self.obstacle).convert_alpha(), pygame.image.load(self.destroyed).convert_alpha()]
        self.current_image = self.images[0]

        self.hitbox = (self.x, self.y, 72, 72)


    def draw(self, player):
        if self.current_image == self.images[0]:
            self.screen.blit(self.current_image, (self.x, self.y))
            #pygame.draw.rect(self.screen, (225, 0, 0), self.hitbox, 2)
        else:
            self.screen.blit(self.current_image, (550, 10))



##############################################################################################################################

class Alien(pygame.sprite.Sprite):

    def __init__(self, startx, starty, w, h, obstacle, destroyed):
        pygame.sprite.Sprite.__init__(self)
        self.x = startx
        self.y = starty
        self.height = h  # 29pixels
        self.width = w  # 40pixels
        self.screen = pygame.display.set_mode((w, h))
        self.obstacle = obstacle
        self.destroyed = destroyed
        self.images = [pygame.image.load(self.obstacle).convert_alpha(), pygame.image.load(self.destroyed).convert_alpha()]
        self.current_image = self.images[0]

        self.hitbox = (self.x, self.y, 40, 30)


    def draw(self, player):
        if self.current_image == self.images[0]:
            self.screen.blit(self.current_image, (self.x, self.y))
            self.hitbox = (self.x, self.y, 40, 30)
            #pygame.draw.rect(self.screen, (0, 0, 0), self.hitbox, 2)
        else:
            self.screen.blit(self.current_image, (550, 10))
            #self.hitbox = (self.x, self.y, 40, 30)
            #pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox, 2)

##############################################################################################################################

class projectile(object):

    def __init__(self, x, y, radius, color, facing, window):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        self.window = window

    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.x,self.y), self.radius)



##############################################################################################################################

class Button():
    def __init__(self, w, h, x, y, Lobby, text=""):
        self.width = w
        self.height = h
        self.posx = x
        self.posy = y
        self.screen = pygame.display.set_mode((w, h))
        self.Lobby = Lobby
        self.text = text

    def draw(self):
        # rect = pygame.draw.rect(self.screen, (0,200,0), (150, 550, 100, 50))
        # self.screen.blit(rect, (self.posx, self.posy))
        pygame.draw.rect(self.Lobby.getLobby(), (0, 200, 0), (150, 500, 100, 50))

##############################################################################################################################

class Label():
    def __init__(self, xCoord, yCoord, text, fontSize, Lobby):
        self.x = xCoord
        self.y = yCoord
        self.text = text
        self.size = fontSize
        self.lobby = Lobby

        self.colors = [ (255, 255, 255), (0, 0, 0)]
        self.current = self.colors[0]


    def draw(self):
        font = pygame.font.Font(None, self.size)
        label = font.render(self.text, 1, self.current)
        self.lobby.getLobby().blit(label, (self.x, self.y))


##############################################################################################################################


class Game():
    clock = pygame.time.Clock()  # create an object to help track time
    #started will be true if enter is pressed to start the game
    started = False


    def __init__(self, w, h, mapw, maph):
        self.width = w
        self.height = h
        self.mapwidth = mapw
        self.mapheight = maph
        self.network = Client()
        self.player1 = Player(435, 75, 36, 48, 'Images/cyan.png', 'Images/cyanDead.png')  # Initializing Player class instance at set point(40,40) in map
        self.player2 = Player(450, 50, 36, 48, 'Images/orange.png', 'Images/orangeDead.png')  # Initializing Player class instance at set point(300,300) in map
        self.enemy1 = Enemy(435, 150, 36, 48, 495, 'Images/blue.png', 'Images/blueDead.png')  # Initializing Player class instance at set point(100,100)
        self.boulder = Boulder(550, 200, 72, 72, 'Images/boulder.png', 'Images/gone.png')
        self.jewel = Jewel(50, 375, 50, 50, 'Images/jewel.png', 'Images/gone.png')
        self.alien = Alien(1000, 25, 40, 29, 'Images/alien.png', 'Images/gone.png')
        self.alien2 = Alien(1060, 25, 40, 29, 'Images/alien.png', 'Images/gone.png')
        self.alien3 = Alien(1120, 25, 40, 29, 'Images/alien.png', 'Images/gone.png')
        self.lobby = Lobby(self.width, self.height, "Version 1.0")  # Creating Lobby class instance
        self.missions = []
        self.player1.place = self.lobby
        self.player2.place = self.lobby
        self.crewmateWin = False
        self.impostorWin = False

        self.player_list = []
        self.vote_tracker = []

        """
        self.button1 = Button(100, 100, 950, 350, self.lobby, "red") #voting buttons
        self.button2 = Button(100, 100, 950, 400, self.lobby, "blue")
        self.button3 = Button(100, 100, 950, 450, self.lobby, "cyan")
        self.button4 = Button(100, 100, 950, 500, self.lobby, "orange")
        """


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
        data = str(self.network.id) + ":" + str(self.player1.rect.x) + "," + str(self.player1.rect.y)
        reply = self.network.sendData(data)
        return reply

    """
    def interrupted(signum, frame):
        # Called when the text input times out
        print("Interrupted")
    signal.signal(signal.SIGALRM, interrupted)
    """
    #adds a player to the player_list
    def add_player(self, player):
        self.player_list.append(player)

    #randomly assings the role of impostor to a random player
    def assign_roles(self):
        random.shuffle(self.player_list)
        self.player_list[0].role = "impostor"

    #makes a player dead and checks to see if their death causes crewmates or impostor to win
    def playerDead(self, username):
        index = self.getPlayerIndex(username)
        self.player_list[index].status = "dead"
        if (self.player_list[index].role == "impostor"):
            self.crewmate_win()
        self.checkDeathWin()

    #resets the vote tracker
    def set_vote_tracker(self):
        if len(self.vote_tracker) == 0:
            self.vote_tracker.clear()
        players = len(self.player_list)
        i = 0
        while (not (i == players)):
            self.vote_tracker.append(0)

    #gets the index of a player in player_list
    def getPlayerIndex (self, username):
        return self.player_list.index(username)

    #adds a players vote to the vote tracker
    def vote(self, voter):
        if (voter.voted == "skip"):
            self.vote_tracker[len(self.player_list) + 1] = self.vote_tracker[len(self.player_list) + 1] + 1
            voter.voted = "no vote"
        elif (voter.voted == "no vote"):
            voter.voted = "no vote"
        else:
            self.vote_tracker[self.getPlayerIndex(voter.voted)] = self.vote_tracker[self.getPlayerIndex(voter.voted)] + 1

    #iterates through alive players and applies their votes
    def applyVotes(self):
        i = 0
        while (not (i == len(self.player_list))):
            if (self.player_list[i].status == "alive"):
                self.vote(self.player_list[i])
            i = i + 1


    #calculates vote results and kills a player if necessary
    def tallyVotes(self):
        tied = True
        current_champ = 0
        current_champ_votes = 0
        i = 0
        while (i < len(self.vote_tracker)):
            if (self.vote_tracker[i] > current_champ_votes):
                current_champ = i
                current_champ_votes = self.vote_tracker[i]
                tied = False
                i= i + 1
            elif (self.vote_tracker[i] == current_champ_votes):
                tied = True
                i = i + 1
            else:
                i = i + 1
        if (not tied and not (current_champ == len(self.player_list))):
            self.playerDead(self.player_list[current_champ].username)


    #checks to see if a death has caused crewmates or impostors to win
    def checkDeathWin(self, username):
        number_of_players = len(self.player_list)
        alive_crewmates = 0
        i = 0
        while (i < number_of_players):
            if (self.player_list[i].status == "alive" and self.player_list[i].role == "crewmate"):
                alive_crewmates = alive_crewmates + 1
            i = i + 1
        if (alive_crewmates == 1):
            self.impostor_win()

    #randomly decides the missions for the game, amount is how many tasks there will be
    def decide_missions(self, amount):
        self.missions = random.sample(range(1, 9), amount)


    #crewmate winning screen
    def crewmate_win(self):
        print("crewmates win")
        self.map.getMap().fill((0, 0, 1))
        font = pygame.font.Font(None, 100)
        win_text = font.render("Crewmates win!", 1, (0, 255, 255))
        self.map.getMap().blit(win_text, (600, 350))

    #impostor winning screen
    def impostor_win(self):
        print("impostor win")
        self.map.getMap().fill((0, 0, 1))
        font = pygame.font.Font(None, 100)
        win_text = font.render("Impostor wins!", 1, (255, 0, 0))
        self.map.getMap().blit(win_text, (600, 350))





########################################################
    # Take in name and use as global variable
    global playername
    playername = ''
    global playername2
    playername2 = ''

    def playerInput(self):
        global playername
        global playername2
        pygame.init()
        base_font = pygame.font.Font(None, 32)

        input_rect1 = pygame.Rect(500, 200, 140, 32)
        active1 = False
        input_rect2 = pygame.Rect(500, 250, 140, 32)
        active2 = False

        color_active = (0, 255, 0)
        color_passive = (255, 255, 255)
        color1 = color_passive
        color2 = color_passive
        running = True
        while running:
            pygame.init()
            self.clock.tick(60)  # once per frame, the program will never running at more than 60 fps.self.started = True
            # Properly quit (pygame will crash without this)
            for event in pygame.event.get():
                # If closed out, quit program
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    sys.exit()

                # Check if mouse is clicked into rectangles to take in input
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if mouse is clicked into 1ST rectangle to take in input for player 1
                    if input_rect1.collidepoint(event.pos):
                        active1 = True
                    else:
                        active1 = False
                    # Check if mouse is clicked into 2ND rectangle to take in input for player 2
                    if input_rect2.collidepoint(event.pos):
                        active2 = True
                    else:
                        active2 = False

                # Check if any keys are pressed
                if event.type == pygame.KEYDOWN:
                    # If 1ST rectangle is clicked on and green/active then take in user input from keyboard
                    if active1 == True:
                        if event.key == pygame.K_BACKSPACE:
                            playername = playername[0:-1]
                        else:
                            playername += event.unicode
                    # If 2ND rectangle is clicked on and green/active then take in user input from keyboard
                    if active2 == True:
                        if event.key == pygame.K_BACKSPACE:
                            playername2 = playername2[0:-1]
                        else:
                            playername2 += event.unicode

                    # If key pressed is ESC key, quit program
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    # If enter is pressed, lobby will close and game will start
                    if event.key == pygame.K_RETURN:
                        self.started = True
                        running = False

            # Draw lobby
            self.lobby.drawPlayerInputLobby()
            # Title for game
            font = pygame.font.Font(None, 50)
            title = font.render("ENTER PLAYER INFO", 1, (255, 255, 255))
            self.lobby.getLobby().blit(title, (600, 50))
            # Label to enter the lobby
            enterLabel = font.render("Press the Enter key to continue", 1, (255, 255, 255))
            self.lobby.getLobby().blit(enterLabel, (400, 500))
            # Player labels
            font = pygame.font.Font(None, 50)
            player1 = font.render("PLAYER 1 NAME: ", 1, (255, 255, 255))
            self.lobby.getLobby().blit(player1, (200, 200))
            player2 = font.render("PLAYER 2 NAME: ", 1, (255, 255, 255))
            self.lobby.getLobby().blit(player2, (200, 250))

            #######################################Adding user input#################################
            # Depending on if rectangle is active or not change color of input rectangle
            if active1:
                color1 = color_active
            else:
                color1 = color_passive

            if active2:
                color2 = color_active
            else:
                color2 = color_passive

            # Draw input rectangle 1
            pygame.draw.rect(self.lobby.getLobby(), color1, input_rect1, 2)
            text_surface = base_font.render(playername, True, (255, 255, 255))
            self.lobby.getLobby().blit(text_surface, (input_rect1.x + 5, input_rect1.y + 5))  # Blit text into rect
            input_rect1.w = max(100, text_surface.get_width() + 10)

            # Draw input rectangle 2
            pygame.draw.rect(self.lobby.getLobby(), color2, input_rect2, 2)
            text_surface2 = base_font.render(playername2, True, (255, 255, 255))
            self.lobby.getLobby().blit(text_surface2, (input_rect2.x + 5, input_rect2.y + 5))  # Blit text into rect
            input_rect2.w = max(100, text_surface2.get_width() + 10)
            ###################################################################################
            pygame.display.update()

        if not self.started:
            pygame.quit()
        else:
            Game.cheshire(self)

###############################

    def cheshire(self):
        running = True
        while running:
            # self.clock.tick(60)  # once per frame, the program will never running at more than 60 fps.self.started = True
            # Properly quit (pygame will crash without this)
            for event in pygame.event.get():
                # If closed out, quit program
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:

                    # If key pressed is ESC key, quit program
                    if event.key == pygame.K_ESCAPE:
                        running = False

            # making character move
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                Game.run(self)

            # Update Lobby
            pygame.init()  # initialize pygame, needed to create fonts, etc.
            self.lobby.drawLobbyBackground2()
            # ENTER LABEL PLACED IN LOBBY TO ENTER GAME#
            font = pygame.font.Font(None, 50)
            enterLabel2 = font.render("Among Us 9.0", 1, (255, 255, 255))
            self.lobby.getLobby().blit(enterLabel2, (600, 50))
            enterLabel = font.render("Press the Up key to connect to server: cheshire.", 1, (255, 255, 255))
            self.lobby.getLobby().blit(enterLabel, (400, 600))


            """
            pygame.mixer.init()
            pygame.mixer.music.load('Images/audio.wav')
            pygame.mixer.music.play(0)
            """
            pygame.display.update()




    def run(self):
        global playername
        global playername2

        running = True
        self.add_player(self.player1)
        self.add_player(self.player2)
        # self.add_player(self.enemy1)
        self.assign_roles()
        msg_bool = False  # boolean for if theres a message
        p1_input = 'type here...'
        p1_bytes = ''

        while running:
            self.clock.tick(60)  # once per frame, the program will never running at more than 60 fps.self.started = True

            # Properly quit (pygame will crash without this)
            for event in pygame.event.get():
                # If closed out, quit program
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:

                    # If key pressed is ESC key, quit program
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    # If enter is pressed, lobby will close and game will start
                    if event.key == pygame.K_RETURN:
                        self.started = True
                        running = False

            # making character move
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                if self.player1.rect.x <= self.width - self.player1.rate:
                    self.player1.move(0)
            if keys[pygame.K_LEFT]:
                if self.player1.rect.x >= self.player1.rate:
                    self.player1.move(1)
            if keys[pygame.K_UP]:
                if self.player1.rect.y >= self.player1.rate:
                    self.player1.move(2)
            if keys[pygame.K_DOWN]:
                if self.player1.rect.y <= self.height - self.player1.rate:
                    self.player1.move(3)

            # Send Network data
            self.player2.rect.x, self.player2.rect.y = self.parseData(self.sendData())

            # Update Lobby
            pygame.init()  # initialize pygame, needed to create fonts, etc.
            self.lobby.drawLobbyBackground()
            self.player1.draw(self.lobby.getLobby())
            self.player2.draw(self.lobby.getLobby())
            self.enemy1.draw(self.lobby.getLobby())


            # Displaying last player joined
            font = pygame.font.Font(None, 20)
            if playername == '':
                playername = 'Nobody'
            if playername2 == '':
                playername2 = 'Nobody'
            text = font.render(playername + " is currently playing as CYAN", 1, (255, 255, 255))  # player 1 text
            self.lobby.getLobby().blit(text, (15, 600))
            text = font.render(playername2 + " is currently playing as ORANGE", 1, (255, 255, 255))  # player 2 text
            self.lobby.getLobby().blit(text, (15, 625))



            #ENTER LABEL PLACED IN LOBBY TO ENTER GAME#
            font = pygame.font.Font(None, 30)
            enterLabel = font.render("Press 'Enter' when all players have joined.", 1, (255, 255, 255))
            self.lobby.getLobby().blit(enterLabel, (495, 457))

            # CHAT BOX SHIT#
            # signal.alarm(TIMEOUT)
            font = pygame.font.Font(None, 30)
            if keys[pygame.K_0]:
                p1_input = input("enter an input :")
            #else:
                #p1_input = ""
            #print(p1_input) # Test, prints current output
            p1_text = font.render("player: " + p1_input, 1, (255, 255, 255)) # player 1 text
            self.lobby.getLobby().blit(p1_text, (15, 20))
            #signal.alarm(0) # Disable alarm after success

            pygame.display.update()

        #started will be true if enter has been pressed
        if not self.started:
            pygame.quit()
        else:
            Game.rungame(self)



###################################


    global isBlueDead
    isBlueDead = False  # Boolean to check if blue is dead
    global p1_input
    p1_input = ''
    #runs the actual game
    def rungame(self):
        global p1_input
        input_rect = pygame.Rect(90, 785, 140, 32)
        active = False
        color_active = (0, 255, 0)
        color_passive = (255, 255, 255)
        color = color_passive
        base_font = pygame.font.Font(None, 30)


        global isBlueDead
        global called
        called = 0 #only call simon says once
        simon = "Error no one left to call the shots" #player who is simon
        #self.decide_missions(4)

        running = True
        #creates the game map
        self.map = Map(self.mapwidth, self.mapheight, "Version 1.0")
        self.map.drawMapBackground()


        #place gets accurate walls
        self.player1.place = self.map
        self.player2.place = self.map
        self.player1.rect.x = 30
        self.player1.rect.y = 30
        """
        self.button1 = Button(100, 100, 950, 350, self.map, "red")  # voting buttons
        self.button2 = Button(100, 100, 950, 400, self.map, "blue")
        self.button3 = Button(100, 100, 950, 450, self.map, "cyan")
        self.button4 = Button(100, 100, 950, 500, self.map, "orange")
        """

        msg_bool = False  # boolean for if theres a message
        self.assign_roles()

        p1_input = 'type here...'

        p1_bytes = ''

        startKILL = pygame.time.get_ticks()  # start killing timer
        maxKILL = 30  # set overall kill interval time

        start_ticks = pygame.time.get_ticks()  # start timer
        max_time = 30 # set max time
        vote = 2

        labelx = 80

        # Declaring array storing bullets
        bullets = []
        shotLoop = 0  # bullet cool down]

        while running:
            self.clock.tick(100)  # once per frame, the program will never running at more than 60 fps.self.started = True
            # setting basic timer for projectiles
            if shotLoop > 0:
                shotLoop += 1
            if shotLoop > 3:
                shotLoop = 0

            #self.map.drawMapBackground()
            # fills window with black
            # walls holds every wall instance
            # self.screen.fill((0, 0, 1))
            # walls at borders of window
            self.map.getMap().fill((0,0,1))
            self.walls = []
            wall = Wall(1356, 0, 10, 768)
            self.walls.append(wall)
            wall = Wall(0, 758, 1366, 10)
            self.walls.append(wall)
            wall = Wall(0, 0, 10, 768)
            self.walls.append(wall)
            wall = Wall(0, 0, 1366, 10)
            self.walls.append(wall)
            # top left room (spawn)
            wall = Wall(0, 192, 80, 10)
            self.walls.append(wall)
            wall = Wall(145, 192, 80, 10)
            self.walls.append(wall)
            wall = Wall(225, 0, 10, 202)
            self.walls.append(wall)
            # top right room
            wall = Wall(960, 160, 406, 10)
            self.walls.append(wall)
            wall = Wall(960, 60, 10, 110)
            self.walls.append(wall)
            # middle room
            wall = Wall(350, 250, 200, 10)
            self.walls.append(wall)
            wall = Wall(620, 250, 390, 10)
            self.walls.append(wall)
            wall = Wall(350, 250, 10, 350)
            self.walls.append(wall)
            wall = Wall(350, 590, 590, 10)
            self.walls.append(wall)
            wall = Wall(1000, 250, 10, 350)
            self.walls.append(wall)
            # bottom right room
            wall = Wall(1100, 590, 140, 10)
            self.walls.append(wall)
            wall = Wall(1310, 590, 56, 10)
            self.walls.append(wall)
            wall = Wall(1100, 590, 10, 178)
            self.walls.append(wall)
            # bottom left room
            wall = Wall(0, 330, 120, 10)
            self.walls.append(wall)
            wall = Wall(110, 330, 10, 348)
            self.walls.append(wall)
            wall = Wall(110, 670, 700, 10)
            self.walls.append(wall)
            wall = Wall(800, 670, 10, 30)
            self.walls.append(wall)

            for wall in self.walls:
                pygame.draw.rect(self.map.getMap(), ((192, 192, 192)), wall.rect)

            # Voting boxes
            pygame.draw.rect(self.map.getMap(), (50, 50, 50), [1500, 250, 140, 40])
            pygame.draw.rect(self.map.getMap(), (50, 50, 50), [1500, 300, 140, 40])
            pygame.draw.rect(self.map.getMap(), (50, 50, 50), [1500, 350, 140, 40])
            pygame.draw.rect(self.map.getMap(), (50, 50, 50), [1500, 400, 140, 40])


            # Properly quit (pygame will crash without this)
            for event in pygame.event.get():
                # If closed out, quit program
                if event.type == pygame.QUIT:
                    running = False
                # Check if mouse is clicked into rectangles to take in input
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if mouse is clicked into 1ST rectangle to take in input for player 1
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False


                if event.type == pygame.KEYDOWN:
                    # If key pressed is ESC key, quit program
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    # If 1ST rectangle is clicked on and green/active then take in user input from keyboard
                    if active == True:
                        if event.key == pygame.K_BACKSPACE:
                            p1_input = p1_input[0:-1]
                        else:
                            p1_input += event.unicode

##############################################CODE FOR CONTROLLING BULLETS#########################################################
            # KEEPING TRACK OF BULLET DISTANCE TRAVELED ALLOWED
            for bullet in bullets:
                # ADDING COLLISON DETECTION FOR THE 3 ALIENS
                if self.alien.current_image == self.alien.images[0]:
                    if bullet.y - bullet.radius < self.alien.hitbox[1] + self.alien.hitbox[3] and bullet.y + bullet.radius > self.alien.hitbox[1]:  # checks if we are above the bottom and below the top of the rectangle
                        if bullet.x + bullet.radius > self.alien.hitbox[0] and bullet.x - bullet.radius < self.alien.hitbox[0] + self.alien.hitbox[2]:
                            self.alien.current_image = self.alien.images[1] #Change alien image to alienGone image
                            bullets.pop(bullets.index(bullet))

                if self.alien2.current_image == self.alien2.images[0]:
                    if bullet.y - bullet.radius < self.alien2.hitbox[1] + self.alien2.hitbox[3] and bullet.y + bullet.radius > self.alien2.hitbox[1]:  # checks if we are above the bottom and below the top of the rectangle
                        if bullet.x + bullet.radius > self.alien2.hitbox[0] and bullet.x - bullet.radius < self.alien2.hitbox[0] + self.alien2.hitbox[2]:
                            self.alien2.current_image = self.alien2.images[1]  # Change alien image to alienGone image
                            bullets.pop(bullets.index(bullet))

                if self.alien3.current_image == self.alien3.images[0]:
                    if bullet.y - bullet.radius < self.alien3.hitbox[1] + self.alien3.hitbox[3] and bullet.y + bullet.radius > self.alien3.hitbox[1]:  # checks if we are above the bottom and below the top of the rectangle
                        if bullet.x + bullet.radius > self.alien3.hitbox[0] and bullet.x - bullet.radius < self.alien3.hitbox[0] + self.alien3.hitbox[2]:
                            self.alien3.current_image = self.alien3.images[1]  # Change alien image to alienGone image
                            bullets.pop(bullets.index(bullet))

                if bullet.x < 1700 and bullet.x > 0:
                    bullet.x += bullet.vel
                else:
                    bullets.pop(bullets.index(bullet))
#########################################BULLET   CODE     END####################################################################

##############################################CODE FOR CONTROLLING BULLETS#########################################################
            # KEEPING TRACK OF BULLET DISTANCE TRAVELED ALLOWED
            for bullet in bullets:
                # ADDING COLLISON DETECTION FOR THE 3 ALIENS
                if self.alien.current_image == self.alien.images[0]:
                    if bullet.y - bullet.radius < self.alien.hitbox[1] + self.alien.hitbox[3] and bullet.y + bullet.radius > self.alien.hitbox[1]:  # checks if we are above the bottom and below the top of the rectangle
                        if bullet.x + bullet.radius > self.alien.hitbox[0] and bullet.x - bullet.radius < self.alien.hitbox[0] + self.alien.hitbox[2]:
                            self.alien.current_image = self.alien.images[1] #Change alien image to alienGone image
                            bullets.pop(bullets.index(bullet))

                if self.alien2.current_image == self.alien2.images[0]:
                    if bullet.y - bullet.radius < self.alien2.hitbox[1] + self.alien2.hitbox[3] and bullet.y + bullet.radius > self.alien2.hitbox[1]:  # checks if we are above the bottom and below the top of the rectangle
                        if bullet.x + bullet.radius > self.alien2.hitbox[0] and bullet.x - bullet.radius < self.alien2.hitbox[0] + self.alien2.hitbox[2]:
                            self.alien2.current_image = self.alien2.images[1]  # Change alien image to alienGone image
                            bullets.pop(bullets.index(bullet))

                if self.alien3.current_image == self.alien3.images[0]:
                    if bullet.y - bullet.radius < self.alien3.hitbox[1] + self.alien3.hitbox[3] and bullet.y + bullet.radius > self.alien3.hitbox[1]:  # checks if we are above the bottom and below the top of the rectangle
                        if bullet.x + bullet.radius > self.alien3.hitbox[0] and bullet.x - bullet.radius < self.alien3.hitbox[0] + self.alien3.hitbox[2]:
                            self.alien3.current_image = self.alien3.images[1]  # Change alien image to alienGone image
                            bullets.pop(bullets.index(bullet))

                if bullet.x < 1700 and bullet.x > 0:
                    bullet.x += bullet.vel
                else:
                    bullets.pop(bullets.index(bullet))
#########################################BULLET   CODE     END####################################################################

            # making character move
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                if self.player1.rect.x <= self.width - self.player1.rate:
                    self.player1.move(0)
            if keys[pygame.K_LEFT]:
                if self.player1.rect.x >= self.player1.rate:
                    self.player1.move(1)
            if keys[pygame.K_UP]:
                if self.player1.rect.y >= self.player1.rate:
                    self.player1.move(2)
            if keys[pygame.K_DOWN]:
                if self.player1.rect.y <= self.height - self.player1.rate:
                    self.player1.move(3)

            # Send Network data
            self.player2.rect.x, self.player2.rect.y = self.parseData(self.sendData())

            # Update map
            self.player1.draw(self.map.getMap())
            self.player2.draw(self.map.getMap())
            self.enemy1.draw(self.map.getMap())


            ###########Player Input text chat#####################################################################
            if active:
                color = color_active
            else:
                color = color_passive

            # CHAT BOX SHIT#
            font = pygame.font.Font(None, 30)
            p1_text = font.render("player: ", 1, (255, 255, 255))  # player 1 text
            self.map.getMap().blit(p1_text, (15, 790))
            # Draw input rectangle 1
            pygame.draw.rect(self.map.getMap(), color, input_rect, 2)
            text_surface = base_font.render(p1_input, True, (255, 255, 255))
            self.lobby.getLobby().blit(text_surface, (input_rect.x + 5, input_rect.y + 5))  # Blit text into rect
            input_rect.w = max(100, text_surface.get_width() + 10)
            ########################################################################################################



            #DRAWING BULLETS TO APPEAR IN GAME
            for bullet in bullets:
                bullet.draw()

            # ENTER LABEL PLACED IN LOBBY TO ENTER GAME#
              # initialize pygame
            font = pygame.font.Font(None, 30)
            enterLabel = font.render("", 1, (255, 255, 255))
            self.map.getMap().blit(enterLabel, (500, 457))

            eLabel = font.render(self.player1.role, 1, (255, 255, 255))
            self.map.getMap().blit(eLabel, (550, labelx))
            labelx = labelx - 1



            # CHAT BOX SHIT#
            #p1_text = font.render("player: ", 1, (255, 255, 255))  # player 1 text
            #self.map.getMap().blit(p1_text, (15, 800))



###########################################   CREWMATE TASKS ################################################################

            ############CODE FOR JEWEL MISSION######################
            # ADDING COLLISON DETECTION w/ player1
            if self.jewel.current_image == self.jewel.images[0]:
                if self.player1.hitbox[1] < self.jewel.hitbox[1] + self.jewel.hitbox[3] and self.player1.hitbox[1] + self.player1.hitbox[3] > self.jewel.hitbox[1]:
                    if self.player1.hitbox[0] + self.player1.hitbox[2] > self.jewel.hitbox[0] and self.player1.hitbox[0] < self.jewel.hitbox[0] + self.jewel.hitbox[2]:
                        self.jewel.current_image = self.jewel.images[1]
            # ADDING COLLISON DETECTION w/ player2
            if self.jewel.current_image == self.jewel.images[0]:
                if self.player2.hitbox[1] < self.jewel.hitbox[1] + self.jewel.hitbox[3] and self.player2.hitbox[1] + self.player2.hitbox[3] > self.jewel.hitbox[1]:
                    if self.player2.hitbox[0] + self.player2.hitbox[2] > self.jewel.hitbox[0] and self.player2.hitbox[0] < self.jewel.hitbox[0] + self.jewel.hitbox[2]:
                        self.jewel.current_image = self.jewel.images[1]
            ###########################################################




            ############CODE FOR BOULDER/OBSTACLE MISSON######################
            # ADDING COLLISON DETECTION w/ player1. Will cause player 1 to move up when colliding with Obstacle. Need to use the X key to destroy obstacle and be able to move
            if self.boulder.current_image == self.boulder.images[0]:
                if self.player1.hitbox[1] < self.boulder.hitbox[1] + self.boulder.hitbox[3] and self.player1.hitbox[1] + self.player1.hitbox[3] > self.boulder.hitbox[1]:
                    if self.player1.hitbox[0] + self.player1.hitbox[2] > self.boulder.hitbox[0] and self.player1.hitbox[0] < self.boulder.hitbox[0] + self.boulder.hitbox[2]:
                        self.player1.move(2)
            # ADDING COLLISON DETECTION w/ player2
            if self.boulder.current_image == self.boulder.images[0]:
                if self.player2.hitbox[1] < self.boulder.hitbox[1] + self.boulder.hitbox[3] and self.player2.hitbox[1] + self.player2.hitbox[3] > self.boulder.hitbox[1]:
                    if self.player2.hitbox[0] + self.player2.hitbox[2] > self.boulder.hitbox[0] and self.player2.hitbox[0] < self.boulder.hitbox[0] + self.boulder.hitbox[2]:
                        self.player2.move(2)
            ###########################################################

            if self.player1.role == "crewmate":
                # Full List of missions on side of screen
                missions_word = font.render("Missions:", 1, (255, 255, 255))
                self.map.getMap().blit(missions_word, (1470, 480))
                self.mission_write_y = 520  # 1380 for x

                self.map.getMap().blit(font.render("Exterminate all aliens on board", 1, (255, 255, 255)), (1380, self.mission_write_y))
                self.mission_write_y = self.mission_write_y + 40
                self.map.getMap().blit(font.render("Acquire Jewel", 1, (255, 255, 255)), (1380, self.mission_write_y))
                self.mission_write_y = self.mission_write_y + 40
                self.map.getMap().blit(font.render("Destroy Obstacle Covering Front Entrance of Main Room", 1, (255, 255, 255)),(1380, self.mission_write_y))
                self.mission_write_y = self.mission_write_y + 40
                self.map.getMap().blit(font.render("Simon says", 1, (255, 255, 255)), (1380, self.mission_write_y))
                self.mission_write_y = self.mission_write_y + 40
                self.map.getMap().blit(font.render("Move to your colored circle", 1, (255, 255, 255)), (1380, self.mission_write_y))
                ############################################

                # Code for Displaying the mission prompts
                global mission
                mission = 1
                global mission_prompt
                mision_prompt = 'mission: '
                mission_text = ''
                random_num = 1  # for simon says assignment
                if (mission == 1):
                    # print("mission: 1")
                    mission_prompt = "Exterminate all aliens on board"
                    self.alien.draw(self.map.getMap())
                    self.alien2.draw(self.map.getMap())
                    self.alien3.draw(self.map.getMap())
                    # Use space action key to shoot bullets and destroy aliens
                    if keys[
                        pygame.K_SPACE] and shotLoop == 0 and mission == 1:  # allow user to shoot projectile if bullet cooldown is met
                        if len(bullets) < 5:
                            bullets.append(projectile(self.player1.rect.x, self.player1.rect.y, 6, (255, 0, 0), 1,
                                                      self.map.getMap()))
                        shotLoop = 1
                    # Increment mission to move onto to next mission
                    if self.alien3.current_image == self.alien3.images[1]:
                        self.map.getMap().blit(font.render("Exterminate all aliens on board", 1, (0, 255, 0)),
                                               (1380, 520))
                        mission += 1

                if (mission == 2):
                    print("mission: 2")
                    mission_prompt = "Acquire Jewel"
                    self.jewel.draw(self.map.getMap())
                    if self.jewel.current_image == self.jewel.images[1]:
                        self.map.getMap().blit(font.render("Acquire Jewel", 1, (0, 255, 0)), (1380, 560))
                        mission += 1

                if (mission == 3):
                    print("mission: 3")
                    mission_prompt = "Destroy Obstacle Covering Front Entrance of Main Room"
                    self.boulder.draw(self.map.getMap())
                    # Destroy boulder obstacle
                    if keys[pygame.K_x]:
                        self.boulder.current_image = self.boulder.images[1]
                    # Increment mission to move onto to next mission
                    if self.boulder.current_image == self.boulder.images[1]:
                        self.map.getMap().blit(font.render("Destroy Obstacle Covering Front Entrance of Main Room", 1, (0, 255, 0)), (1380, 600))
                        mission += 1

                if (mission == 4):
                    print("mission: 4")
                    print("called = " + str(called))
                    if called == 0:
                        random_num = random.randint(1, 2)
                        print(random_num)
                        number_of_players = len(self.player_list)
                        alive_players = 0
                        i = 0
                        while (i < number_of_players):
                            if (self.player_list[i].status == "alive"):
                                alive_players = alive_players + 1
                                print(self.player_list[i].color)
                                if (self.player_list[i].color == "Images/cyan.png" and random_num == 1):
                                    simon = "Cyan is the simon"
                                    break
                                elif (self.player_list[i].color == "Images/orange.png" and random_num == 2):
                                    simon = "Orange is the simon"
                                    break

                            i = i + 1

                    mission_prompt = "Simon says, Type commands in chat, others follow when simon says; " + simon
                    called = 1

                    if p1_input != "":

                        self.map.getMap().blit(font.render("Simon says", 1, (0, 255, 0 )), (1380, 640))
                        mission += 1


                if (mission == 5):
                    print("mission: 5")
                    mission_prompt = "Move to your colored circle"
                    pygame.draw.circle(self.lobby.getLobby(), (255, 0, 0), (700, 300), 25)  # Red circle
                    pygame.draw.circle(self.lobby.getLobby(), (0, 0, 255), (700, 400), 25)  # Blue circle
                    pygame.draw.circle(self.lobby.getLobby(), (255, 140, 0), (800, 300), 25)  # Orange circle
                    pygame.draw.circle(self.lobby.getLobby(), (0, 255, 255), (800, 400), 25)  # cyan circle

                    if self.player1.rect.x > 790 and self.player1.rect.x < 810:
                        if self.player1.rect.y > 390 and self.player1.rect.y < 410:
                            self.map.getMap().blit(font.render("Move to your colored circle", 1, (0, 255, 0)), (1380, 680))

                            #mission += 1


                if (mission == 6):
                    print("mission: 6")
                    mission_prompt = "Type your favorite beverage in the chat"
                if (mission == 7):
                    print("mission: 7")

                if (mission == 8):
                    print("mission: 8")
                    mission_prompt = "Stand in a line"
                if (mission == 9):
                    print("mission: 9")
                    mission_prompt = "Go to the left of the screen and race to the right of the screen"

                mission_text = font.render(mission_prompt, 1, (255, 255, 255))  # player 1 text
                self.map.getMap().blit(mission_text, (625, 790))


            #Kill cooldown
            if self.player1.role != "crewmate":
                secs = (pygame.time.get_ticks() - startKILL) / 1000  # calculate how many seconds
                dif = int(maxKILL - secs)
                if (dif < 0):
                    maxKILL += 30
                if (dif > 15 and dif < 31):
                    time = "ALLOWED TO KILL!"
                    timer_txt = font.render(time, 1, (0, 255, 0))  # player 1 text
                    self.map.getMap().blit(timer_txt, (625, 790))
                    # KILLING CHARACTERS#
                    # USE 2 KEY TO KILL PLAYER 2
                    if keys[pygame.K_2]:

                        if self.player1.rect.x - self.player2.rect.x > -10 and self.player1.rect.x - self.player2.rect.x < 10:
                            self.player2.current_image = self.player2.images[1]
                    # USE 3 KEY TO KILL BLUE BOT
                    if keys[pygame.K_3]:
                        if self.player1.rect.x - self.enemy1.x > -10 and self.player1.rect.x - self.enemy1.x < 10:
                            self.enemy1.current_image = self.enemy1.images[1]

                            isBlueDead = True  # set boolean to true

                if (dif > -1 and dif < 16):
                    time = "Kill Cooldown: " + str(dif)
                    timer_txt = font.render(time, 1, (255, 0, 0))  # player 1 text
                    self.map.getMap().blit(timer_txt, (625, 790))







            # Voting labels
            red_text = font.render("red", 1, (255, 255, 255))  # player 1 text
            self.lobby.getLobby().blit(red_text, (1530, 260))
            blue_text = font.render("blue", 1, (255, 255, 255))  # player 1 text
            self.lobby.getLobby().blit(blue_text, (1530, 310))
            cyan_text = font.render("cyan", 1, (255, 255, 255))  # player 1 text
            self.lobby.getLobby().blit(cyan_text, (1530, 360))
            orange_text = font.render("orange", 1, (255, 255, 255))  # player 1 text
            self.lobby.getLobby().blit(orange_text, (1530, 410))

            if ((vote % 2) == 0):
                vote_text = font.render("vote", 1, (255, 255, 255))  # player 1 text
                self.lobby.getLobby().blit(vote_text, (1530, 200))

            else:
                vote_text = font.render("vote", 1, (0, 255, 0))  # set vote text to green
                self.lobby.getLobby().blit(vote_text, (1530, 200))
                number_of_players = len(self.player_list)
                alive_players = 0
                for event in pygame.event.get():
                    mousecor = pygame.mouse.get_pos()
                    mouseXcor = mousecor[0]
                    mouseYcor = mousecor[1]
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 1500 < mouseXcor < 1640 and 250 < mouseYcor < 290:
                            self.player1.voted = "red"
                        elif 1500 < mouseXcor < 1640 and 300 < mouseYcor < 340:
                            self.player1.voted = "blue"
                        elif 1500 < mouseXcor < 1640 and 350 < mouseYcor < 390:
                            self.player1.voted = "cyan"
                        elif 1500 < mouseXcor < 1640 and 400 < mouseYcor < 440:
                            self.player1.voted = "orange"

                i = 0
                while (i < number_of_players):
                    if (self.player_list[i].status == "alive"):
                        alive_players = alive_players + 1
                        print(self.player_list[i].color)
                        if (self.player_list[i].color == "Images/cyan.png"):
                            cyan_text = font.render("cyan", 1, (0, 255, 255))  # player 1 text
                            self.lobby.getLobby().blit(cyan_text, (1530, 360))
                        elif (self.player_list[i].color == "Images/orange.png"):
                            orange_text = font.render("orange", 1, (255, 160, 0))  # player 1 text
                            self.lobby.getLobby().blit(orange_text, (1530, 410))
                        if not isBlueDead:
                            blue_text = font.render("blue", 1, (0, 0, 255))  # player 1 text
                            self.lobby.getLobby().blit(blue_text, (1530, 310))

                    i = i + 1

            # Timer
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
            # print(seconds) #print how many seconds
            #print(int(max_time - seconds))  # debug
            diff = int(max_time - seconds)
            if (diff < 0):
                # start_ticks = 0
                max_time += 30
                vote += 1
            time_diff = "timer: " + str(diff)
            timer_text = font.render(time_diff, 1, (255, 255, 255))  # player 1 text
            self.lobby.getLobby().blit(timer_text, (1500, 150))

            """
            if msg_bool:
                print(msg_bool)
                print("delivered")
                print(p1_input)
                p1_text = font.render("player 1: ", 1, (255, 255, 255))  # player 1 text
                #self.lobby.getLobby().blit(p1_text, (150, 2)) # Display
                p1_bytes = bytes("wow", 'ascii')
                scoretext = font.render(p1_bytes, 1, (255, 255, 255))
                self.lobby.getLobby().blit(scoretext, (150, 457))
                msg_bool = False
                #print(p1_text)
                #print(msg_bool)
            """

            #just for tests
            #comment out other prints when using this
            #print(self.player1.voted)

            #tests for winning screens
            """
            if keys[pygame.K_i]:
                self.impostor_win()
            if keys[pygame.K_c]:
                self.crewmate_win()
            """

            if not self.crewmateWin and not self.impostorWin:
                pygame.display.update()
            elif self.crewmateWin:
                self.crewmate_win()
            else:
                self.impostor_win()

        pygame.quit()

#############################################################################################################################################
