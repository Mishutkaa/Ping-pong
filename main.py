from pygame import *
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #разом 55,55 - параметри
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
 
back = (200, 255, 255)
win_width = 750
win_height = 600
window = display.set_mode((win_width, win_height))
window.fill(back)
 
run = True
finish = False
clock = time.Clock()
FPS = 60
 
speed_x = 4
speed_y = 4

ball = GameSprite("tennis_ball.png", 300, 250,  15, 50, 50)
raketa = Player("racket.png", 20, 200, 3, 50, 150)
raketa2 = Player("racket.png", 680, 200, 3, 50, 150)
while run:
    window.fill(back)
    for e in event.get():
        if e.type == QUIT:
           run = False
    ball.reset()
    ball.update()
    raketa.update_l()
    raketa2.reset()
    raketa2.update_r()
    raketa.reset()


    if sprite.collide_rect(raketa, ball) or sprite.collide_rect(raketa2, ball):
        speed_x *= -1
        speed_y *= 1
    if ball.rect.colliderect(raketa.rect):
        speed_y *= -1
    if ball.rect.y > 550:
        speed_y *= -1
    if ball.rect.y < 0:
        speed_y *= -1
    if ball.rect.x > 700:
        run = False
    if ball.rect.x < 0:
        run = False




    ball.rect.x += speed_x
    ball.rect.y += speed_y
    display.update()
    clock.tick(FPS)