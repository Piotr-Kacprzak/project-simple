#komentarz
import pgzrun
from random import randint, choice

WIDTH = 1280
HEIGHT = 853

class Paletka:
    def __init__(self, Paletka, pozycja):
        self.Paletka = Paletka
        self.Paletka.x = pozycja[0]
        self.Paletka.y = pozycja[1]
    def drawing(self):
        self.Paletka.draw()
    def move(self, direction):
        if direction == "left":
            self.Paletka.x -= 5
        if direction == "right":
            self.Paletka.x += 5
    def bounce(self):
        return self.Paletka.distance_to(ball) < 60

def check_for_bounce():
    if Paletka_a.bounce():
        ball.direction_y  = "down"
    if Paletka_b.bounce():
        ball.direction_y  = "up"

def update_palette_position():
    if keyboard.a:
        Paletka_a.move("left")
    if keyboard.s:
        Paletka_a.move("right")
    if keyboard.k:
        Paletka_b.move("left")
    if keyboard.l:
        Paletka_b.move("right")

def update_ball_position():
    if ball.direction_x == "left":
        ball.x -= ball.speed
    elif ball.direction_x == "right":
        ball.x += ball.speed

    if ball.direction_y == "up":
        ball.y -= ball.speed
    elif ball.direction_y == "down":
        ball.y += ball.speed

    if ball.x < 5:
        ball.direction_x = "right"
    elif ball.x > WIDTH - 5:
        ball.direction_x = "left"

    if ball.y < 5:
        ball.winner = "gracz B"
        ball.stop = True
        ball.game_run = False
    elif ball.y > HEIGHT - 5:
        ball.winner = "gracz A"
        ball.stop = True
        ball.game_run = False

Paletka_a = Paletka(Actor("palette.png"), (100, 20))
Paletka_b = Paletka(Actor("palette.png"), (100, 833))

ball = Actor("ball.png")
ball.x = randint(40, WIDTH - 40)
ball.y = HEIGHT // 2
ball.start = False
ball.game_run = False
ball.stop = False
ball.winner = None
ball.direction_x = choice(("left","right"))
ball.direction_y = choice(("up","down"))
ball.speed = 2

def draw():
    screen.blit("desert-1654439_1280.jpg", (0,0))
    if not ball.start:
        screen.draw.text("press SPACE to start", (40, 150), fontsize=40, color=(0, 0, 0))
    Paletka_a.drawing()
    Paletka_b.drawing()
    ball.draw()

def update():
    if not ball.start and keyboard.space:
        ball.game_run = True
        ball.start = True
    if ball.game_run:
        update_ball_position()
        update_palette_position()
        check_for_bounce()

pgzrun.go()
