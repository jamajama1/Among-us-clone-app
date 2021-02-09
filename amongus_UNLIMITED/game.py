# small network game that has differnt blobs
# moving around the screen

import sys
import contextlib
from time import sleep

with contextlib.redirect_stdout(None):
    import pygame
from client import Network
import random
import os
pygame.font.init()

# Constants
PLAYER_RADIUS = 20
START_VEL = 9
BALL_RADIUS = 5

W, H = 1600, 830

NAME_FONT = pygame.font.SysFont("comicsans", 20)
TIME_FONT = pygame.font.SysFont("comicsans", 30)
SCORE_FONT = pygame.font.SysFont("comicsans", 26)

COLORS = [(255,0,0), (255, 128, 0), (255,255,0), (128,255,0),(0,255,0),(0,255,128),(0,255,255),(0, 128, 255), (0,0,255), (0,0,255), (128,0,255),(255,0,255), (255,0,128),(128,128,128), (0,0,0)]
PICTURES = ["Images/blue.png", "Images/red.png", "Images/orange.png", "Images/cyan.png"]
# Dynamic Variables
players = {}
balls = []


global redStatusImg
global cyanStatusImg
global orangeStatusImg
global blueStatusImg
redImg = [pygame.image.load('Images/red.png'), pygame.image.load('Images/redDead.png')]  # load red image
redStatusImg = redImg[0]
cyanImg = [pygame.image.load('Images/cyan.png'), pygame.image.load('Images/cyanDead.png')]  # load red image
cyanStatusImg = cyanImg[0]
orangeImg = [pygame.image.load('Images/orange.png'), pygame.image.load('Images/orangeDead.png')]  # load red image
orangeStatusImg = orangeImg[0]
blueImg = [pygame.image.load('Images/blue.png'), pygame.image.load('Images/blueDead.png')] # load blue image
blueStatusImg = blueImg[0]
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
        self.screen.fill((0, 0, 1))

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

    def __init__(self, startx, starty, w, h, obstacle, destroyed, map):
        pygame.sprite.Sprite.__init__(self)
        self.x = startx
        self.y = starty
        self.height = h  # 29pixels
        self.width = w  # 40pixels
        self.screen = map.screen
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


















# FUNCTIONS
def convert_time(t):
    """
    converts a time given in seconds to a time in
    minutes
    :param t: int
    :return: string
    """
    if type(t) == str:
        return t

    if int(t) < 60:
        return str(t) + "s"
    else:
        minutes = str(t // 60)
        seconds = str(t % 60)

        if int(seconds) < 10:
            seconds = "0" + seconds

        return minutes + ":" + seconds


def redraw_LOBBY(players, balls, game_time, score, current_id):
    """
    draws each frame
    :return: None
    """
    lobby = Lobby(1700, 850, "Version 1.0")  # Creating
    lobby.drawLobbyBackground()
    #WIN.fill((255,255,255)) # fill screen white, to clear old frames
    '''
    # draw all the orbs/balls
    for ball in balls:
        pygame.draw.circle(WIN, ball[2], (ball[0], ball[1]), BALL_RADIUS)
    '''
    # draw each player in the list
    for player in sorted(players, key=lambda x: players[x]["score"]):
        p = players[player]
        #print(current_id) # printing the player info
        # pygame.draw.circle(WIN, p["color"], (p["x"], p["y"] + 30), PLAYER_RADIUS + round(p["score"]))
        # WIN.blit(redImg, (p["x"], p["y"] + 30))
        why = p["y"] + 5
        drawPlayer(p["x"], why, p["pid"])
        # render and draw name for each player
        text = NAME_FONT.render(p["name"], 1, (255,255,255))
        lobby.screen.blit(text, (p["x"] - text.get_width()/2, p["y"] - text.get_height()/2))

    # draw scoreboard
    sort_players = list(reversed(sorted(players, key=lambda x: players[x]["score"])))
    title = TIME_FONT.render("Players", 1, (255,255,255))
    start_y = 25
    x = W - title.get_width() - 10
    lobby.screen.blit(title, (x, 5))

    ran = min(len(players), 8)
    for count, i in enumerate(sort_players[:ran]):
        text = SCORE_FONT.render(str(count+1) + ". " + str(players[i]["name"]), 1, (255,255,255))
        lobby.screen.blit(text, (x, start_y + count * 20))

    # draw time
    text = TIME_FONT.render("Time: " + convert_time(game_time), 1, (255,255,255))
    lobby.screen.blit(text,(10,10))
    # draw score
    # text = TIME_FONT.render("Score: " + str(round(score)),1,(0,0,0))
    # WIN.blit(text,(10,15 + text.get_height()))





global mission
mission = 1

def redraw_MAP(players, balls, game_time, score, current_id, map):
    global mission_prompt
    global mission
    """
    draws each frame
    :return: None
    """
    #map = Map(1700, 850, "Version 1.0")
    #map.drawMapBackground()
#############
    """""
    boulder = Boulder(550, 200, 72, 72, 'Images/boulder.png', 'Images/gone.png')
    jewel = Jewel(50, 375, 50, 50, 'Images/jewel.png', 'Images/gone.png')
    alien = Alien(1000, 25, 40, 29, 'Images/alien.png', 'Images/gone.png')
    alien2 = Alien(1060, 25, 40, 29, 'Images/alien.png', 'Images/gone.png')
    alien3 = Alien(1120, 25, 40, 29, 'Images/alien.png', 'Images/gone.png')
    jewel.draw(map.screen)
    boulder.draw(map.screen)
    alien.draw(map.screen)
    alien2.draw(map.screen)
    alien3.draw(map.screen)
    """""
    #########
    missionSurface = pygame.Surface([1700, 850])

    #bg_img1 = pygame.image.load('Images/boulder.png').convert_alpha()
    #map.screen.blit(bg_img1, (550, 200))


#################
    '''
    # draw all the orbs/balls
    for ball in balls:
        pygame.draw.circle(WIN, ball[2], (ball[0], ball[1]), BALL_RADIUS)
    '''
    players[0]["role"] = "imposter"
    # draw each player in the list
    global playersAlive
    for player in sorted(players, key=lambda x: players[x]["score"]):
        p = players[player]


        print(p["role"])
        #print(current_id) # printing the player info
        # pygame.draw.circle(WIN, p["color"], (p["x"], p["y"] + 30), PLAYER_RADIUS + round(p["score"]))
        # WIN.blit(redImg, (p["x"], p["y"] + 30))
        why = p["y"] + 5
        drawPlayer(p["x"], why, p["pid"])
        # render and draw name for each player
        text = NAME_FONT.render(p["name"], 1, (255,255,255))
        map.screen.blit(text, (p["x"] - text.get_width()/2, p["y"] - text.get_height()/2))


        if p["role"] == "crewmate":
            # Full List of missions on side of screen
            font = pygame.font.Font(None, 30)
            missions_word = font.render("Missions:", 1, (255, 255, 255))
            map.getMap().blit(missions_word, (1470, 500))
            mission_write_y = 550  # 1380 for x

            map.getMap().blit(font.render("Exterminate all aliens on board", 1, (255, 255, 255)), (1380, mission_write_y))
            if (mission > 1):
                map.getMap().blit(font.render("Exterminate all aliens on board", 1, (0, 255, 0)), (1380, mission_write_y))
            mission_write_y = mission_write_y + 40
            map.getMap().blit(font.render("Acquire Jewel", 1, (255, 255, 255)), (1380, mission_write_y))
            if(mission > 2):
                map.getMap().blit(font.render("Acquire Jewel", 1, (0, 255, 0)), (1380, mission_write_y))
            mission_write_y = mission_write_y + 40
            map.getMap().blit(font.render("Destroy Obstacle Covering Front Entrance of Main Room", 1, (255, 255, 255)), (1380, mission_write_y))
            if(mission > 3):
                map.getMap().blit(font.render("Destroy Obstacle Covering Front Entrance of Main Room", 1, (0, 255, 0)),(1380, mission_write_y))
            mission_write_y = mission_write_y + 40
            map.getMap().blit(font.render("Simon says", 1, (255, 255, 255)), (1380, mission_write_y))
            if (mission > 4):
                map.getMap().blit(font.render("Simon says", 1, (0, 255, 0)), (1380, mission_write_y))
            mission_write_y = mission_write_y + 40
            map.getMap().blit(font.render("Move to your colored circle", 1, (255, 255, 255)),
                                   (1380, mission_write_y))
            if (mission > 5):
                map.getMap().blit(font.render("Move to your colored circle", 1, (0, 255, 0)),(1380, mission_write_y))
            # Code for Displaying the mission prompts

            keys = pygame.key.get_pressed()
            mision_prompt = 'mission: '
            mission_text = ''
            random_num = 1  # for simon says assignment
            if (mission == 1):
                # print("mission: 1")
                mission_prompt = "Exterminate all aliens on board"
                bg_img1 = pygame.image.load('Images/alien.png').convert_alpha()
                map.screen.blit(bg_img1, (1000,25))
                map.screen.blit(bg_img1, (1060, 25))
                map.screen.blit(bg_img1, (1120, 25))
                if keys[pygame.K_SPACE]:
                    map.getMap().blit(font.render("Exterminate all aliens on board", 1, (0, 255, 0)), (1380, 550))
                    mission += 1

            if (mission == 2):
                print("mission: 2")
                mission_prompt = "Acquire Jewel"
                #keys = pygame.key.get_pressed()
                bg_img1 = pygame.image.load('Images/jewel.png').convert_alpha()
                map.screen.blit(bg_img1, (50, 375))

                if keys[pygame.K_z]:
                    bg_img1 = pygame.image.load('Images/gone.png').convert_alpha()
                    map.screen.blit(bg_img1, (50, 375))
                    map.getMap().blit(font.render("Acquire Jewel", 1, (0, 255, 0)), (1380, mission_write_y))
                    mission += 1

            if (mission == 3):
                boulderGone = False
                print("mission: 3")
                mission_prompt = "Destroy Obstacle Covering Front Entrance of Main Room"
                bg_img1 = pygame.image.load('Images/boulder.png').convert_alpha()
                map.screen.blit(bg_img1, (550, 200))
                # Destroy boulder obstacle
                #keys = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if keys[pygame.K_x]:
                        bg_img1 = pygame.image.load('Images/gone.png').convert_alpha()
                        map.screen.blit(bg_img1, (550, 200))
                        mission +=1

                        # Increment mission to move onto to next mission

                        map.getMap().blit(
                            font.render("Destroy Obstacle Covering Front Entrance of Main Room", 1, (0, 255, 0)),
                            (1380, 600))
                    if(boulderGone):
                        break
                    #mission += 1

            if (mission == 4):
                print("mission: 4")
                called =0
                simon = ""
                #print("called = " + str(called))
                if called == 0:
                    random_num = random.randint(1, 2)
                    print(random_num)
                    number_of_players = len(players)
                    alive_players = 0
                    i = 0
                    while (i < number_of_players):
                        if (players[i]["alive"] == 0 and players[i]["role"] == "crewmate"):
                            alive_players = alive_players + 1
                            #print(self.player_list[i].color)
                            if (players[i]["pid"] == 1 and random_num == 1):
                                simon = "Cyan is the simon"
                                break
                            elif (players[i]["pid"] == "Images/orange.png" and random_num == 2):
                                simon = "Orange is the simon"
                                break
                        i = i + 1
                    mission_prompt = "Simon says, Type commands in chat, others follow when simon says; " + simon
                    called = 1

                if(players[1]["x"] < 30):
                    mission += 1
                    break

            if (mission == 5):
                print("mission: 5")
                mission_prompt = "Move to your colored circle"


                bg_img1 = pygame.image.load('Images/red_circle.png').convert_alpha()
                bg_img1 = pygame.transform.scale(bg_img1, (40,40))
                map.screen.blit(bg_img1, (700, 300))

                bg_img1 = pygame.image.load('Images/blue_circle.png').convert_alpha()
                bg_img1 = pygame.transform.scale(bg_img1, (60, 40))
                map.screen.blit(bg_img1, (700, 400))
                bg_img1 = pygame.image.load('Images/orange_circle.png').convert_alpha()
                bg_img1 = pygame.transform.scale(bg_img1, (60, 40))
                map.screen.blit(bg_img1, (800, 300))
                bg_img1 = pygame.image.load('Images/cyan_circle.png').convert_alpha()
                bg_img1 = pygame.transform.scale(bg_img1, (60, 40))
                map.screen.blit(bg_img1, (800, 400))

                if ((players[1]["x"] > 800 and players[1]["y"] > 400) or (players[0]["x"] > 700 and players[0]["y"] > 300) ):
                    mission += 1
                    break
                """
                pygame.draw.circle(missionSurface, (255, 0, 0), (700, 300), 25)  # Red circle
                pygame.draw.circle(missionSurface, (0, 0, 255), (700, 400), 25)  # Blue circle
                pygame.draw.circle(missionSurface, (255, 140, 0), (800, 300), 25)  # Orange circle
                pygame.draw.circle(missionSurface, (0, 255, 255), (800, 400), 25)  # cyan circle
                """
                """
                if player1.rect.x > 790 and self.player1.rect.x < 810:
                    if self.player1.rect.y > 390 and self.player1.rect.y < 410:
                        self.map.getMap().blit(font.render("Move to your colored circle", 1, (0, 255, 0)), (1380, 680))
                        mission += 1
                """
            if (mission == 6):
                print("mission: 6")
                mission_prompt = "CREWMATE WINS!"
                crewmate_win(map)
                #mission_prompt = "Type your favorite beverage in the chat"
            if (mission == 7):
                print("mission: 7")


            if (mission == 8):
                print("mission: 8")
                mission_prompt = "Stand in a line"
            if (mission == 9):
                print("mission: 9")
                mission_prompt = "Go to the left of the screen and race to the right of the screen"
            print(playersAlive)


            mission_text = font.render(mission_prompt, 1, (255, 255, 255))  # player 1 text
            map.getMap().blit(mission_text, (625, 790))
        ############################################
    font = pygame.font.Font(None, 30)
    mission_prompt = ""
    if (playersAlive <= 2):  # Imposter wins message
        mission_prompt = "Imposter wins!!!"
        impostor_win(map)
    mission_text = font.render(mission_prompt, 1, (255, 255, 255))  # player 1 text
    map.getMap().blit(mission_text, (625, 50))
    # draw scoreboard
    sort_players = list(reversed(sorted(players, key=lambda x: players[x]["score"])))
    title = TIME_FONT.render("Players", 1, (255,255,255))
    start_y = 25
    x = W - title.get_width() - 10
    map.screen.blit(title, (x, 5))

    ran = min(len(players), 8)
    for count, i in enumerate(sort_players[:ran]):
        text = SCORE_FONT.render(str(count+1) + ". " + str(players[i]["name"]), 1, (255,255,255))
        map.screen.blit(text, (x, start_y + count * 20))

    # draw time
    #text = TIME_FONT.render("Time: " + convert_time(game_time), 1, (255,255,255))
    #map.screen.blit(text,(10,10))
    # draw score
    # text = TIME_FONT.render("Score: " + str(round(score)),1,(0,0,0))
    # WIN.blit(text,(10,15 + text.get_height()))


global playersAlive
playersAlive =4
def drawPlayer(ex, ey, player_id):
    global redStatusImg
    global cyanStatusImg
    global orangeStatusImg
    global blueStatusImg
    global playersAlive
    keys = pygame.key.get_pressed()
    if(player_id == 0):
        WIN.blit(redStatusImg, (ex, ey))
        if keys[pygame.K_r]:
            redStatusImg = redImg[1]
            players[0]["alive"] = 1
            playersAlive -=1
            #print(players[0]["alive"])

    elif(player_id == 1):
        WIN.blit(cyanStatusImg, (ex, ey))
        if keys[pygame.K_c]:
            cyanStatusImg = cyanImg[1]
            players[1]["alive"] = 1
            playersAlive -= 1

    elif (player_id == 2):
        WIN.blit(orangeStatusImg, (ex, ey))
        if keys[pygame.K_o]:
            orangeStatusImg = orangeImg[1]
            players[2]["alive"] = 1
            playersAlive -= 1
    else:
        WIN.blit(blueStatusImg, (ex, ey))
        if keys[pygame.K_b]:
            blueStatusImg = blueImg[1]
            players[3]["alive"] = 1
            playersAlive -= 1
    # pygame.draw.circle(WIN, p["color"], (p["x"], p["y"]), PLAYER_RADIUS + round(p["score"]))



def impostor_win(map):
    map.getMap().fill((0, 0, 1))
    font = pygame.font.Font(None, 100)
    win_text = font.render("Impostor wins!", 1, (255, 0, 0))
    map.getMap().blit(win_text, (600, 350))

#crewmate winning screen
def crewmate_win(map):
    map.getMap().fill((0, 0, 1))
    font = pygame.font.Font(None, 100)
    win_text = font.render("Crewmate wins!", 1, (0, 255, 255))
    map.getMap().blit(win_text, (600, 350))





def assignImposter():
    x = random.randint(0,len(players)-1)
    p = players[x]
    p["role"] = "imposter"
    print(p)







global playername
playername = ''
def playerInput():
    global playername
    lobby = Lobby(1700, 850, "Version 1.0")
    clock = pygame.time.Clock()
    pygame.init()
    base_font = pygame.font.Font(None, 32)

    input_rect1 = pygame.Rect(500, 200, 140, 32)
    active1 = False


    color_active = (0, 255, 0)
    color_passive = (255, 255, 255)
    color1 = color_passive

    running = True
    while running:
        pygame.init()
        clock.tick(60)  # once per frame, the program will never running at more than 60 fps.self.started = True
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


            # Check if any keys are pressed
            if event.type == pygame.KEYDOWN:
                # If 1ST rectangle is clicked on and green/active then take in user input from keyboard
                if active1 == True:
                    if event.key == pygame.K_BACKSPACE:
                        playername = playername[0:-1]
                    else:
                        playername += event.unicode
                # If 2ND rectangle is clicked on and green/active then take in user input from keyboard


                # If key pressed is ESC key, quit program
                if event.key == pygame.K_ESCAPE:
                    running = False
                # If enter is pressed, lobby will close and game will start
                if event.key == pygame.K_RETURN:
                    started = True
                    running = False

        # Draw lobby
        lobby.drawPlayerInputLobby()
        # Title for game
        font = pygame.font.Font(None, 50)
        title = font.render("ENTER PLAYER INFO", 1, (255, 255, 255))
        lobby.getLobby().blit(title, (600, 50))
        # Label to enter the lobby
        enterLabel = font.render("Press the Enter key to continue", 1, (255, 255, 255))
        lobby.getLobby().blit(enterLabel, (400, 500))
        # Player labels
        font = pygame.font.Font(None, 50)
        player1 = font.render("PLAYER NAME: ", 1, (255, 255, 255))
        lobby.getLobby().blit(player1, (200, 200))


        #######################################Adding user input#################################
        # Depending on if rectangle is active or not change color of input rectangle
        if active1:
            color1 = color_active
        else:
            color1 = color_passive



        # Draw input rectangle 1
        pygame.draw.rect(lobby.getLobby(), color1, input_rect1, 2)
        text_surface = base_font.render(playername, True, (255, 255, 255))
        lobby.getLobby().blit(text_surface, (input_rect1.x + 5, input_rect1.y + 5))  # Blit text into rect
        input_rect1.w = max(100, text_surface.get_width() + 10)

        pygame.display.update()

    if not started:
        pygame.quit()
    else:
        return(str(playername))























global p1_input
p1_input = ''
def rungame(name):
    #CHAT BOX REQUIREMENTS#
    global p1_input
    pygame.init()
    base_font = pygame.font.Font(None, 32)
    input_rect = pygame.Rect(90, 805, 140, 32)
    active = False
    color_active = (0, 255, 0)
    color_passive = (255, 255, 255)
    color = color_passive
    font = pygame.font.Font(None, 30)
    chatText = font.render('', 1, (255, 255, 255))  # player 1 text


    start_ticks = pygame.time.get_ticks()  # start timer
    max_time = 30  # set max time
    vote = 2
# CHAT BOX REQUIREMENTS END#
    global players
    # start by connecting to the network
    server = Network()
    current_id = server.connect(name)
    balls, players, game_time = server.send("get")
    # setup the clock, limit to 30fps
    clock = pygame.time.Clock()
    assignImposter()

    # Declaring array storing bullets
    bullets = []
    shotLoop = 0  # bullet cool down

    # start killing timer
    startKILL = pygame.time.get_ticks()
    maxKILL = 30  # set overall kill interval time

    started = False
    run = True
    while run:
        clock.tick(30) # 30 fps max
        player = players[current_id]

        # setting basic timer for projectiles
        if shotLoop > 0:
            shotLoop += 1
        if shotLoop > 3:
            shotLoop = 0
        #print(players[current_id]) # print player id
        #print(current_id)
        # print(player["x"]) # player x
        # print("draw player")
        #drawPlayer(200,100, player)
        #drawPlayer(player["x"], player["y"])

        if(current_id == 4):
            # WIN.blit("red.png", (player["x"], player["x"]))
            print('')
        vel = START_VEL - round(player["score"]/14)
        if vel <= 1:
            vel = 1

        # get key presses
        keys = pygame.key.get_pressed()

        data = ""
        # movement based on key presses
        if keys[pygame.K_LEFT]:
            if player["x"] - vel - PLAYER_RADIUS - player["score"] >= 0:
                player["x"] = player["x"] - vel

        if keys[pygame.K_RIGHT]:
            if player["x"] + vel + PLAYER_RADIUS + player["score"] <= W:
                player["x"] = player["x"] + vel

        if keys[pygame.K_UP]:
            if player["y"] - vel - PLAYER_RADIUS - player["score"] >= 0:
                player["y"] = player["y"] - vel

        if keys[pygame.K_DOWN]:
            if player["y"] + vel + PLAYER_RADIUS + player["score"] <= H:
                player["y"] = player["y"] + vel

        data = "move " + str(player["x"]) + " " + str(player["y"])

        # allow user to shoot projectile if bullet cooldown is met
        if keys[pygame.K_SPACE] and shotLoop == 0:
            if len(bullets) < 5:
                bullets.append(projectile(player["x"], player["y"], 6, (255, 0, 0), 1, map.screen))
            shotLoop = 1

        # send data to server and recieve back all players information
        balls, players, game_time = server.send(data)

        for event in pygame.event.get():
            # if user hits red x button close window
            if event.type == pygame.QUIT:
                run = False

            # Check if mouse is clicked into rectangles to take in input
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if mouse is clicked into 1ST rectangle to take in input for player 1
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                # if user hits a escape key close program
                if event.key == pygame.K_ESCAPE:
                    run = False
                # If enter is pressed, lobby will close and game will start
                if event.key == pygame.K_RETURN:
                    started = True
                    #run = False

                # If 1ST rectangle is clicked on and green/active then take in user input from keyboard
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        p1_input = p1_input[0:-1]
                    else:
                        p1_input += event.unicode


        # redraw window then update the frame
        if started:
            map = Map(1700, 850, "Version 1.0")
            map.drawMapBackground()
            #DRAW IN ALL OBSTACLES AND TASKS FOR GAME WITH redraw_MAP
            redraw_MAP(players, balls, game_time, player["score"], current_id, map)
            ##Player Input text chat###
            if active:
                color = color_active
            else:
                color = color_passive
            font = pygame.font.Font(None, 30)
            p1_text = font.render("player: ", 1, (255, 255, 255))  # player 1 text
            map.screen.blit(p1_text, (15, 810))
            pygame.draw.rect(map.screen, color, input_rect, 2)
            text_surface = base_font.render(p1_input, True, (255, 255, 255))
            map.screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))  # Blit text into rect
            input_rect.w = max(100, text_surface.get_width() + 10)
            if keys[pygame.K_RETURN]:
                chatText = font.render(p1_input, 1, (255, 255, 255))  # player 1 text
            map.screen.blit(chatText, (90, 780))
            ##Player Input text chat END###







            # Imposter Mission Cover UP
            if player["role"] == "imposter":
                # Imposter label
                font = pygame.font.Font(None, 30)
                eLabel = font.render(player["role"], 1, (255, 255, 255))
                map.getMap().blit(eLabel, (550, 15))

                #Cover up aliens for imposter
                bg_img1 = pygame.image.load('Images/gone.png')
                map.getMap().blit(bg_img1, (1000, 25))
                map.getMap().blit(bg_img1, (1060, 25))
                map.getMap().blit(bg_img1, (1120, 25))

                # coverup mission prompt
                mission_text = font.render("Exterminate all aliens on board", 1, (0, 0, 0))  # player 1 text
                map.getMap().blit(mission_text, (625, 790))

                #Cover up mission list
                coverUP_rect = pygame.Rect(90, 805, 140, 32)

                mission_write_y = 550  # 1380 for x
                map.getMap().blit(font.render("Exterminate all aliens on board", 1, (0, 0, 0)), (1380, mission_write_y))
                mission_write_y = mission_write_y + 40
                map.getMap().blit(font.render("Acquire Jewel", 1, (0, 0, 0)), (1380, mission_write_y))
                mission_write_y = mission_write_y + 40
                map.getMap().blit(font.render("Destroy Obstacle Covering Front Entrance of Main Room", 1, (0, 0, 0)), (1380, mission_write_y))
                mission_write_y = mission_write_y + 40
                map.getMap().blit(font.render("Simon says", 1, (0, 0, 0)), (1380, mission_write_y))
                mission_write_y = mission_write_y + 40
                map.getMap().blit(font.render("Move to your colored circle", 1, (0, 0, 0)), (1380, mission_write_y))

                #Kill Cooldown Timer
                secs = (pygame.time.get_ticks() - startKILL) / 1000  # calculate how many seconds
                dif = int(maxKILL - secs)
                if (dif < 0):
                    maxKILL += 30
                if (dif > 15 and dif < 31):
                    time = "ALLOWED TO KILL!"
                    timer_txt = font.render(time, 1, (0, 255, 0))  # player 1 text
                    map.getMap().blit(timer_txt, (640, 790))
                    # KILLING CHARACTERS#
                    # USE 2 KEY TO KILL PLAYER 2
                    #if keys[pygame.K_2]:

                if (dif > -1 and dif < 16):
                    time = "Kill Cooldown: " + str(dif)
                    timer_txt = font.render(time, 1, (255, 0, 0))  # player 1 text
                    map.getMap().blit(timer_txt, (640, 790))






            #####ALIEN TASk
            alien = Alien(1000, 25, 40, 29, 'Images/alien.png', 'Images/gone.png', map)
            alien2 = Alien(1060, 25, 40, 29, 'Images/alien.png', 'Images/gone.png', map)
            alien3 = Alien(1120, 25, 40, 29, 'Images/alien.png', 'Images/gone.png', map)

            # DRAWING BULLETS TO APPEAR IN GAME
            for bullet in bullets:
                # bg_img = pygame.image.load('Images/gone.png').convert_alpha()
                bullet.draw()

            for bullet in bullets:
                # ADDING COLLISON DETECTION FOR THE 3 ALIENS
                if alien.current_image == alien.images[0]:
                    if bullet.y - bullet.radius < alien.hitbox[1] + alien.hitbox[3] and bullet.y + bullet.radius > \
                            alien.hitbox[1]:  # checks if we are above the bottom and below the top of the rectangle
                        if bullet.x + bullet.radius > alien.hitbox[0] and bullet.x - bullet.radius < alien.hitbox[0] + \
                                alien.hitbox[2]:
                            alien.current_image = alien.images[1]  # Change alien image to alienGone image
                            bg_img1 = pygame.image.load('Images/gone.png').convert_alpha()
                            map.screen.blit(bg_img1, (1000, 25))
                            map.screen.blit(bg_img1, (1060, 25))
                            map.screen.blit(bg_img1, (1120, 25))
                            bullets.pop(bullets.index(bullet))

                if alien2.current_image == alien2.images[0]:
                    if bullet.y - bullet.radius < alien2.hitbox[1] + alien2.hitbox[3] and bullet.y + bullet.radius > \
                            alien2.hitbox[1]:  # checks if we are above the bottom and below the top of the rectangle
                        if bullet.x + bullet.radius > alien2.hitbox[0] and bullet.x - bullet.radius < alien2.hitbox[0] + \
                                alien2.hitbox[2]:
                            alien2.current_image = alien2.images[1]  # Change alien image to alienGone image
                            bullets.pop(bullets.index(bullet))

                if alien3.current_image == alien3.images[0]:
                    if bullet.y - bullet.radius < alien3.hitbox[1] + alien3.hitbox[3] and bullet.y + bullet.radius > \
                            alien3.hitbox[1]:  # checks if we are above the bottom and below the top of the rectangle
                        if bullet.x + bullet.radius > alien3.hitbox[0] and bullet.x - bullet.radius < alien3.hitbox[0] + \
                                alien3.hitbox[2]:
                            alien3.current_image = alien3.images[1]  # Change alien image to alienGone image
                            bg_img1 = pygame.image.load('Images/gone.png').convert_alpha()
                            bullets.pop(bullets.index(bullet))
                if bullet.x < 1700 and bullet.x > 0:
                    bullet.x += bullet.vel
                else:
                    bullets.pop(bullets.index(bullet))

                alien.draw(map.screen)
                alien2.draw(map.screen)
                alien3.draw(map.screen)
            #####ALIEN TASk END



            # Voting labels
            red_text = font.render("red", 1, (255, 255, 255))  # player 1 text
            map.screen.blit(red_text, (1530, 260))
            blue_text = font.render("blue", 1, (255, 255, 255))  # player 1 text
            map.screen.blit(blue_text, (1530, 310))
            cyan_text = font.render("cyan", 1, (255, 255, 255))  # player 1 text
            map.screen.blit(cyan_text, (1530, 360))
            orange_text = font.render("orange", 1, (255, 255, 255))  # player 1 text
            map.screen.blit(orange_text, (1530, 410))
            if ((vote % 2) == 0):
                vote_text = font.render("vote", 1, (255, 255, 255))  # player 1 text
                map.screen.blit(vote_text, (1530, 200))

            else:
                vote_text = font.render("vote", 1, (0, 255, 0))  # set vote text to green
                map.screen.blit(vote_text, (1530, 200))
                number_of_players = len(players)
                alive_players = 0

                i = 0
                while (i < number_of_players):
                    if (players[i]["alive"] == 0):
                        alive_players = alive_players + 1
                        #print(players[i].color)
                        if (players[i]["pid"] == 1): # red, cyan, orange, blue
                            cyan_text = font.render("cyan", 1, (0, 255, 255))  # player 1 text
                            map.screen.blit(cyan_text, (1530, 360))
                        elif (players[i]["pid"] == 2):
                            orange_text = font.render("orange", 1, (255, 160, 0))  # player 1 text
                            map.screen.blit(orange_text, (1530, 410))
                        elif (players[i]["pid"] == 0):
                            red_text = font.render("red", 1, (255, 0, 0))  # player 1 text
                            map.screen.blit(red_text, (1530, 260))
                        elif (players[i]["pid"] == 3):
                            blue_text = font.render("blue", 1, (0, 0, 255))  # player 1 text
                            map.screen.blit(blue_text, (1530, 310))


                    i = i + 1

            # Timer
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
            # print(seconds) #print how many seconds
            # print(int(max_time - seconds))  # debug
            diff = int(max_time - seconds)
            if (diff < 0):
                # start_ticks = 0
                max_time += 30
                vote += 1
            time_diff = "timer: " + str(diff)
            timer_text = font.render(time_diff, 1, (255, 255, 255))  # player 1 text
            map.screen.blit(timer_text, (1500, 475))

        else:
            redraw_LOBBY(players, balls, game_time, player["score"], current_id)



        pygame.display.update()

        #redraw_gameWindow(players, balls, game_time, player["score"], current_id)


    server.disconnect()
    pygame.quit()
    quit()


# get users name
while True:

    name = playerInput()
    #name = input("Please enter your name: ")
    if  0 < len(name) < 20:
        break
    else:
        print("Error, this name is not allowed (must be between 1 and 19 characters [inclusive])")


# make window start in top left hand corner
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,30)

# setup pygame window
WIN = pygame.display.set_mode((W,H))
pygame.display.set_caption("Blobs")

# start game
rungame(name)