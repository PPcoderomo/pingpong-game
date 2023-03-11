from pygame import *

window = display.set_mode((600, 500))
clock = time.Clock()
FPS = 60
game = True
while game:
    for e in event.get():
        if e.type==QUIT:
            game = False
    display.update()
    clock.tick(FPS)
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
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    