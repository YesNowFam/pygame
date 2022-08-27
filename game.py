#The Legendary Speedy Snake of India codename:snake xensia pygame port (unofficial)
#In-game Music Composed by Hemant Kumar (Musical Keyboard) and High Defitonised and Game Over Music (Used FamiStudio NES Composer) by Ibrahim Aayan
#Game Made by Ibrahim Aayan A359543
print("The Legendary Speedy Snake of India Unofficial Pygame Port")
print("Made by Ibrahim Aayan A359543")
print("In-game Music Composed by Hemant Kumar (Musical Keyboard) and High Defitonised and Game Over Music (Used FamiStudio NES Composer) by Ibrahim Aayan")
print("Dedicated to Our Game Development group teacher: Sir Zayan")
print("Importing Python File...")
print("Importing Pygame Module...")
print("Loading in-game Music...")
print("Importing System Database...")
print("Loading Game...")
print("Arrow Keys and W A S D movement supported")
#essential game imports
import pygame, sys, random, time
pygame.mixer.pre_init(44100,-16,1,512)
pygame.init()


check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, existing...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) Pygame successfully initialized!")

 # Play surface
playSurface = pygame.display.set_mode((360, 120)) #setting display size
pygame.display.set_caption('==> The Legendary Speedy Snake Of India <==')
# time.sleep(5) #screen will sleep for 5 seconds



#Play background music
pygame.mixer.music.load("Nagin Been Music HD.mp3")
pygame.mixer.music.get_volume()
pygame.mixer.music.play(-1)
# colours
#gameover and food
red = pygame.Color(255,0,0)
#snake
blue = pygame.Color(0, 0, 255)
#background  
green = pygame.Color(0,255,0)
#score
black = pygame.Color(0,0,0)
#background
white = pygame.Color(255,255,255)
#unused color
brown = pygame.Color(165, 42, 42)   
# frames per second controller
fpsController = pygame.time.Clock()
#title screen


 	
    
snakePos = [100,50]  # it works like x and y axis [x,y]
snakeBody = [[100,50],[90,50],[80,50]]

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]  # food position, its also like placing coordinate randomly
foodSpawn = True

score = 0

direction = 'RIGHT'
changeto = direction

# game over function
def gameOver():
    myFont = pygame.font.SysFont('noto sans',72)
    GOsurf = myFont.render('Game Over!',True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOsurf,GOrect)
    #Gameover Music
    pygame.mixer.music.load("Gameover.wav")
    pygame.mixer.music.get_volume()
    pygame.mixer.music.play(0)
    #Continues Function
    pygame.display.set_caption('Thank You For Playing!')
    print("Thank You For Playing!")
    showScore(0)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()   #pygame exit
    sys.exit()  #console exit

def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco',24)
    Ssurf = sFont.render('Total Score : {0}'.format(score), True, red)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (360,120)
    playSurface.blit(Ssurf,Srect)
    

# main logic of the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:    #cheking if type of event is equal to event present in pygame i.e. QUIT
            pygame.quit()  #exit pygame
            sys.exit()  #exit console
        elif event.type == pygame.KEYDOWN:  # if user hit an button of keyboard
            if event.key == pygame.K_RIGHT or event.key == ord('d'): # and if that button would be right arrow key
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'DOWN'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'UP'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # validation of direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # changing direction of the snake by incrementing and decrementing x and y coordinate
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] += 10
    if direction == 'DOWN':
        snakePos[1] -= 10

    # snake body mechanism
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()
    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn = True

    # Background
    playSurface.fill(green)

    #Draw Snake
    for pos in snakeBody:
        pygame.draw.rect(playSurface, blue,
        pygame.Rect(pos[0],pos[1],10,10))

    pygame.draw.rect(playSurface, red,
    pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    if snakePos[0] > 710 or snakePos[0] <0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()

    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()

    showScore()
    pygame.display.flip()  
    fpsController.tick(12)