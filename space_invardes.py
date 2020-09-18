# python 3 - space invaders game
# Art by Kenney.nl / (www.kenney.nl)
import pygame, random, time
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
font_dir = path.join(path.dirname(__file__), 'fonts')
sound_dir = path.join(path.dirname(__file__), 'sounds')
WIDTH = 480
HEIGHT = 600
FPS = 60
POWER_TIME = 5000

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255);
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
LIGHTSLATEGRAY = (119,136,153)
DARKGRAY = (169,169,169)
LIGHTSTEELBLUE = (176, 196, 222)
LIGHTSEAGREEN = (32,178,170)
CADETBLUE = (95,158,160)
MORON = (128, 0, 0)
DARKRED = (139, 0, 0)

#draw text on the abritary position on the screen
def draw_text(text, size, color, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (round(x), round(y))
    game_display.blit(text_surface, text_rect)

def display_text_arbitraryfont(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (round(x), round(y))
    game_display.blit(text_surface, text_rect)


def button(text, a_color, ina_color, bx_pos, by_pos, b_wid, b_hig,
           textx_pos, texty_pos, text_size, text_color):

    pygame.draw.rect(game_display, ina_color, (bx_pos, by_pos, b_wid, b_hig))
    display_text_arbitraryfont(text, yoster_font, text_color, textx_pos, texty_pos)
    # draw_text(text, text_size, text_color, textx_pos, texty_pos)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    if mouse_x > bx_pos and mouse_x < bx_pos + b_wid and mouse_y > by_pos and mouse_y < by_pos + b_hig:
        pygame.draw.rect(game_display, a_color, (bx_pos, by_pos, b_wid, b_hig))
        # draw_text(text, text_size, text_color, textx_pos, texty_pos)
        display_text_arbitraryfont(text, yoster_font, text_color, textx_pos, texty_pos)

# intro will be displayed at the start of the game
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        game_display.fill(WHITE)
        game_display.blit(newblackbackground, blackbackground_rect)
      
        # draw_text('Astrodrive', 85, DARKGRAY, WIDTH / 2, 140)
        display_text_arbitraryfont('ASTRODRIVE', kevnectorfut_font ,DARKGRAY, WIDTH / 2, 140)

        button('START SHOOTING', DARKGRAY, BLACK, WIDTH / 2 - 137, 220, 280, 50, 241, 243, 30, WHITE)
        
        button('QUIT GAME', DARKGRAY, BLACK, WIDTH /2 - 95, 320, 195, 50, WIDTH / 2 + 3, 345, 30, WHITE)


        help = 'Controls are ARROW KEYS and SPACE for shooting'
        draw_text(help, 15, LIGHTSTEELBLUE, WIDTH /2 , 500)

        mouse_clicked = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        #if button is pressed some action will happen
        if mouse_x > (WIDTH / 2 - 137) and mouse_x < (WIDTH / 2 - 137) + 280 and mouse_y > 220 and mouse_y < 270:
            if mouse_clicked[0]:
                intro = False        

        if mouse_x > (WIDTH / 2 - 95) and mouse_x < (WIDTH / 2 - 95) + 195 and mouse_y > 320 and mouse_y < 370:
            if mouse_clicked[0]:
                pygame.quit()    
        
        pygame.display.flip()

def game_outro(score):
    global game_over
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        game_display.fill(WHITE)
        game_display.blit(newblackbackground, blackbackground_rect)
        # draw_text('YOU CRASHED', 50, DARKRED, WIDTH / 2, 140)
        display_text_arbitraryfont('SCORE:' + str(score), kevnectorfut_font, WHITE, WIDTH / 2, 250)
        # draw_text('SCORE: ' + str(score), 30, WHITE, WIDTH /2, 200)
        button('START SHOOTING AGAIN', DARKGRAY, MORON, WIDTH / 2 - 200, 350, 400, 50, 241, 373, 24, WHITE)
        button('QUIT GAME', DARKGRAY, MORON, WIDTH /2 - 95, 450, 195, 50, WIDTH / 2 + 3, 475, 30, WHITE)


        mouse_clicked = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        #if button is pressed some action will happen
        if mouse_x > (WIDTH / 2 - 200) and mouse_x < (WIDTH / 2 - 200) + 400 and mouse_y > 350 and mouse_y < 400:
            if mouse_clicked[0]:
                game_over = False        

        if mouse_x > (WIDTH / 2 - 95) and mouse_x < (WIDTH / 2 - 95) + 195 and mouse_y > 450 and mouse_y < 520:
            if mouse_clicked[0]:
                pygame.quit()    
        
        pygame.display.flip()


class Player(pygame.sprite.Sprite):
    #sprite for the player / sprite is 2D image that is drawn on the screen
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerspaceship
        self.image = pygame.transform.scale(playerspaceship, (60, 47))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = 580
        self.speedx = 0
        self.power = 1
        

    def update(self):
        self.speedx = 0
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_LEFT]:
            self.speedx = -6
        if keypressed[pygame.K_RIGHT]:
            self.speedx = 7
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        self.rect.x += self.speedx
        
        if self.power >= 2 and pygame.time.get_ticks() - self.powerup_start > POWER_TIME:
            self.power = 1

    def shoot(self):
        if self.power == 1:
            bullet = Bullet(self.rect.centerx, self.rect.y)
            all_sprites.add(bullet)
            bullets.add(bullet)
            laser_sound.play()
        if self.power == 2:
            bullet1 = Bullet(self.rect.left, self.rect.y + 35)
            bullet2 = Bullet(self.rect.right, self.rect.y + 35)
            bullets.add(bullet1)
            bullets.add(bullet2)
            all_sprites.add(bullet1)
            all_sprites.add(bullet2)
            laser_sound.play()
        if self.power >= 3:
            bullet1 = Bullet(self.rect.left, self.rect.y + 35)
            bullet2 = Bullet(self.rect.right, self.rect.y + 35)
            bullet3 = Bullet(self.rect.centerx, self.rect.y)
            bullets.add(bullet1)
            bullets.add(bullet2)
            bullets.add(bullet3)
            all_sprites.add(bullet1)
            all_sprites.add(bullet2)
            all_sprites.add(bullet3)
            laser_sound.play()
    
    def powerup(self):
        self.powerup_start = pygame.time.get_ticks()
        self.power += 1
            
class Mob(pygame.sprite.Sprite):
    #sprites for the enemies
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(meteors_imgs)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.y > HEIGHT:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-150, -100)
            self.speedy = random.randrange(1, 8)
            self.speex = random.randrange(-3, 3)
        if self.rect.x > WIDTH:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-150, -100)
            self.speedy = random.randrange(1, 8)
            self.speex = random.randrange(-3, 3)
        if self.rect.x + self.rect.width < 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-150, -100)
            self.speedy = random.randrange(1 , 8)
            self.speex = random.randrange(-3, 3)

class Bullet(pygame.sprite.Sprite):
    # sprite for the bullets
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = laser
        self.image = pygame.transform.scale(laser, (10, 20))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill bullet if it comes of screen
        if self.rect.bottom < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 30

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
        else:
            center = self.rect.center
            self.image = explosion_anim[self.size][self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = center

class Powerup(pygame.sprite.Sprite):
    
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = powerup
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.center = center
        self.speedy = 3
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom > HEIGHT:
            self.kill()

# initialize pygame and create window
pygame.init()
pygame.font.init()
pygame.mixer.init()
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Astrodrive')
running = True
game_over = False

#load all graphics
background = pygame.image.load(path.join(img_dir, 'space.png')).convert()
background_rect = background.get_rect()
blackbackground = pygame.image.load(path.join(img_dir, 'black.png')).convert()
newblackbackground = pygame.transform.scale(blackbackground, (480, 600))
blackbackground_rect = newblackbackground.get_rect()
playerspaceship = pygame.image.load(path.join(img_dir, 'playerShip2_red.png')).convert()
laser = pygame.image.load(path.join(img_dir, 'laserRed16.png')).convert()
powerup = pygame.image.load(path.join(img_dir, 'star_bronze.png')).convert()
# button = pygame.image.load(path.join(img_dir, 'buttonRed.png')).convert()
meteors_imgs = []
meteors_types = ['meteorBrown_big1.png', 'meteorBrown_big2.png', 'meteorBrown_big3.png',
                 'meteorBrown_big4.png', 'meteorBrown_med1.png', 'meteorBrown_med3.png',
                 'meteorBrown_small1.png', 'meteorBrown_small2.png', 'meteorBrown_tiny1.png',
                 'meteorBrown_tiny2.png']
for met in meteors_types:
    meteors_imgs.append(pygame.image.load(path.join(img_dir, met)).convert())

explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
for i in range(8):
    filename = 'regularExplosion0{}.png'.format(i)
    player_exp = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
    img_pl = pygame.image.load(path.join(img_dir, player_exp)).convert()
    img_pl.set_colorkey(BLACK)
    explosion_anim['player'].append(img_pl)


#initialize fonts
# pygame will search for font closest to arial if you dont have it on your computer 
font_name = pygame.font.match_font('arial')
arcade_font = pygame.font.Font(path.join(font_dir, 'arcade.ttf'), 85)
yoster_font = pygame.font.Font(path.join(font_dir, 'yoster.ttf'), 30)
kevnectorfut_font = pygame.font.Font(path.join(font_dir, 'kenvector_future.ttf'), 55)
#initialize sounds
laser_sound = pygame.mixer.Sound(path.join(sound_dir, 'sfx_laser1.ogg'))
lose_sound = pygame.mixer.Sound(path.join(sound_dir, 'sfx_lose.ogg'))
intro_sound = pygame.mixer.Sound(path.join(sound_dir, 'intro.ogg'))
pygame.mixer.music.load(path.join(sound_dir, 'intro.ogg'))
# pygame.mixer.music.load(path.join(sound_dir, 'stanko.ogg'))
pygame.mixer.music.set_volume(0.3)
# Game intro will start first
game_intro()

# All sprites are added to group so they can be easily updated
all_sprites = pygame.sprite.Group()
player = Player()
enemies = pygame.sprite.Group() 
bullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()
for i in range(0,8):
    enemies.add(Mob())
all_sprites.add(player)
all_sprites.add(enemies)
# score
score = 0
# start game music
pygame.mixer.music.play(loops = -1)  
while running:
    # if player died go to game_outro 
    # when we go out of game_outro initialize everything to the start agains
    
    if game_over:
        # pygame.mixer.music.pause()
        game_outro(score)
        game_over = False
        all_sprites = pygame.sprite.Group()
        player = Player()
        enemies = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        for i in range(0,8):
            enemies.add(Mob())
        all_sprites.add(player)
        all_sprites.add(enemies)
        # pygame.mixer.music.unpause()
        # score
        score = 0

    # do this loop 60 times in a second
    clock.tick(FPS)
    # proccesing events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    #main sounds
    
    #update
    all_sprites.update()
    #check if player hit the enemies
    # Third parametar tells us if sprite dissapears if it hit player
    hits = pygame.sprite.spritecollide(player, enemies, False, pygame.sprite.collide_circle)
    if hits:
        exp = Explosion(player.rect.center, 'player')
        all_sprites.add(exp)
        lose_sound.play()
        game_over = True
        
    #check if bullets hit enemies
    # Last two parametars are to say what will happen to the gropus if collide
    # True is for dissapearing if collide, two parametars for two groups
    bullet_hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in bullet_hits:
        score += 55 - hit.radius
        exp = Explosion(hit.rect.center, 'lg')
        m = Mob()
        enemies.add(m)
        all_sprites.add(m)
        all_sprites.add(exp)
        # spawn powerup if you generate random number above 0.98
        if random.random() > 0.98:
            powup = Powerup(hit.rect.center)
            all_sprites.add(powup)
            powerups.add(powup)
    #check if player hit powerup
    hits = pygame.sprite.spritecollide(player, powerups, True)
    for hit in hits:
        player.powerup()
    #draw/render seciton
    game_display.fill(GREEN)
    game_display.blit(background, background_rect)
    all_sprites.draw(game_display)
    draw_text('Score:' + str(score), 20, DARKGRAY ,WIDTH / 2, 10)
    # after everything is drawn flip the screen
    pygame.display.flip()



pygame.quit()
