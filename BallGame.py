# Importing the pygame module
import pygame as pyg

# Game initialisation
pyg.init()
screen = pyg.display.set_mode((590,400))
pyg.display.set_caption("BALL GAME")
game_over = False
done = False
winner = ''
colours = ["red", 'blue', 'cyan', 'magenta', 'violet', 'pink', 'purple', 'white']
shifter = 0
colour = 'red'
colour_board = "yellow"
x1, y1 = 20, 90
x2, y2 = 550, 90
x_ball, y_ball = (285, 135)
x_speed, y_speed = (4, 0.7)
clock = pyg.time.Clock()

# Game name
font = pyg.font.Font('freesansbold.ttf', 40)
text = font.render('BALL GAME', True, 'green', 'black')
text_frame = text.get_rect()
text_frame.center = (300, 350)

# Player names
font_names = pyg.font.Font('freesansbold.ttf', 30)
player_names = font_names.render('PLAYER 1                       PLAYER 2', True, 'red', 'black')
names_frame = player_names.get_rect()
names_frame.center = (300, 300)

while not done:
    clock.tick(50)
    print("cycle no. :")
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            done = True
        if event.type == pyg.KEYDOWN and event.key == pyg.K_SPACE:
            try:
                colour = colours[shifter+1]
                shifter += 1
            except:
                shifter = 0
                colour = colours[shifter]
    screen.fill([0, 0, 0])

# Setting up text
    screen.blit(text, text_frame)
    screen.blit(player_names, names_frame)

# Setting frame
    pyg.draw.rect(screen, colour, pyg.Rect(9, 10, 560, 5))
    pyg.draw.rect(screen, colour, pyg.Rect(9, 275, 560, 5))
    pyg.draw.rect(screen, colour, pyg.Rect(9, 10, 5, 270))
    pyg.draw.rect(screen, colour, pyg.Rect(569, 10, 5, 270))

# Creating ball logic
    pyg.draw.circle(screen, "yellow", (x_ball, y_ball), 6, 4)
    if x_ball >= 550 and (y_ball > y2) and (y_ball < y2+70):
        x_speed = -(x_speed + 0.1)
    elif x_ball <= 35 and (y_ball > y1) and (y_ball < y1+70):
        x_speed = -(x_speed - 0.1)
    elif y_ball <= 20:
        y_speed = -y_speed
    elif y_ball >= 268:
        y_speed = -y_speed
    elif x_ball <= 9:
        game_over = True
        winner = "PLAYER 2"
        x_speed, y_speed = 0, 0
    elif x_ball >= 569:
        game_over = True
        winner = "PLAYER 1"
        x_speed, y_speed = 0, 0

# Declaring winner
    if winner:
        winner_name = font_names.render('GAME OVER!!! The winner is: ' + winner, True, 'green', 'black')
        win_frame = winner_name.get_rect()
        win_frame.center = (300, 200)
        screen.blit(winner_name, win_frame)

    x_ball += x_speed
    y_ball += y_speed

# Handling event
    pressed = pyg.key.get_pressed()
    if pressed[pyg.K_w] and y1 > 20:
        y1 -= 5
    if pressed[pyg.K_s] and y1 < 200:
        y1 += 5
    pyg.draw.rect(screen, colour_board, pyg.Rect(x1, y1, 15, 70))

    if pressed[pyg.K_UP] and y2 > 20:
        y2 -= 5
    if pressed[pyg.K_DOWN] and y2 < 200:
        y2 += 5
    pyg.draw.rect(screen, colour_board, pyg.Rect(x2, y2, 15, 70))
    pyg.display.flip()
    
# This game looks worse than the save drops one, but in my own view works better.
# This was the very first game i ever created.
