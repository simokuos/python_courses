import pygame

#sligthly modified borrowed spritesheet code 
#at https://www.pygame.org/wiki/Spritesheet
class spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except (pygame.error, message):
            print ('Unable to load spritesheet image:', filename)
            raise (SystemExit, message)
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)


#initialising pygame
pygame.init()

#defining size of game window
display_game = pygame.display.set_mode((800,600)) 
pygame.display.set_caption("justus_kavelee")

#color1 = pygame.Color(0, 0, 0)     

#getting visuals from spritesheet
sprite_one = spritesheet("sprites.png")
sprite_images = [] 
sprite_images = sprite_one.images_at(((1,0,11,14),(13,0,11,14),(25,0,11,14),(37,0,11,14)))
tile = sprite_one.image_at((0,17,16,15))


FPS = pygame.time.Clock()
FPS.tick(60)

i = 0
for images in sprite_images:
    sprite_images[i] = pygame.transform.scale(images, (36, 42))
    i = i + 1

tile = pygame.transform.scale(tile, (64, 64))

temp_img = sprite_images[0]
player_x = 400
player_y = 300
moveDown = False
moveUP = False
moveLeft = False
moveRight = False

while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT: 
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                moveDown = True
            if event.key == pygame.K_UP:
                moveUP = True
            if event.key == pygame.K_LEFT:
                moveLeft = True
            if event.key == pygame.K_RIGHT:
                moveRight = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                moveDown = False
            if event.key == pygame.K_UP:
                moveUP = False
            if event.key == pygame.K_LEFT:
                moveLeft = False
            if event.key == pygame.K_RIGHT:
                moveRight = False
    
    if(moveDown):
        temp_img = sprite_images[0]
        player_y = player_y + 10
    
    if(moveUP):
        temp_img = sprite_images[1]
        player_y = player_y - 10

    if(moveLeft):
        temp_img = sprite_images[3]
        player_x = player_x - 10

    if(moveRight):
        temp_img = sprite_images[2]
        player_x = player_x + 10
    #windowsSize.blit(helloWorld, (0, 0))
    for y in range(10):
        for x in range(13):
            display_game.blit(tile, (64*x, (64*y - 5)))
    FPS.tick(60)
    display_game.blit(temp_img, (player_x ,player_y))

    pygame.display.update()