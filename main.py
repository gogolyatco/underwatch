from pygame import *
mixer.init()
mixer.music.load("")
mixer.music.play()
fire_sound = mixer.Sound("")

img_back = "images.jpg"
img_hero = "хз хто.jpg"

img_bullet = "bullet.jpg"
img_enemy = "хз хто.png"

score = 0
lost = 0
max_lost = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x,size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(
            image.loa(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, self.rect.x, self.rect.y))
class Player(GameSprite):
        def update(self):
            keys = key.get_pressed()
            if keys[K_LEFT] and self.rect.x > 5:
                self.rect.x -= self.speed
            if keys[K_RIGHT] and self.rect.x < win_width - 80:
                self.rect.x += self.speed
        def fire(self):
            bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top,15,20,-15)
                bullets.add(bullet)
            pass

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = -10
            lost += 1

win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back),(win_width, win_height))
    ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)\

bullets = sprite.Group

    finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()
    if not finish:
        window.blit(background, (0, 0))
        ship.update()
        bullets.update()
        ship.reset()
        bullets.draw(window)
        display.update()
    time.delay(50)
