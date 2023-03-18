from pygame import *


window = display.set_mode((600, 500))
clock = time.Clock()
FPS = 60
game = True
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('P1 LOSES', True, (180, 0, 0))  
font2 = font.Font(None, 35)
lose2 = font2.render('P2 LOSES', True, (180, 0, 0))  
class GameSprite(sprite.Sprite):
    def __init__(self, filename, speed, x, y, size_x = 65, size_y = 65):
        super().__init__ ()
        self.image = transform.scale(image.load(filename),(size_x,size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update2(self):  
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
ball = GameSprite('doto.png', 10, 250, 250, 65, 65)
speed_x = 3
speed_y = 3
finish = False
player2 = Player('line.png', 10, 535, 250, 65, 65)
player = Player('line.png', 10, 0, 250, 65, 65)
while game:
    for e in event.get():
        if e.type==QUIT:
            game = False
    if finish != True: 
        ball.rect.x += speed_x
        window.fill((0,255,255))
        ball.reset()
        ball.rect.y += speed_y
        player.reset()
        player.update()
        player2.reset()
        player2.update2()
    if ball.rect.y > 500 - 50 or ball.rect.y < 0:
        speed_y *=-1
    if sprite.collide_rect(player, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
    if ball.rect.x < -15:
        finish = True
        window.blit(lose1, (200,200))
    if ball.rect.x > 550:
        finish = True
        window.blit(lose2, (200,200))
    display.update()
    clock.tick(FPS)