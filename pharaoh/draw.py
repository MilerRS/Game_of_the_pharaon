import pygame

from pharaoh.constants import WIDTH, HEIGHT

pygame.init()
images_dict = {}


def Upload_Img():
    images = ["hieroglyph", "scarab", "eye", "eagle", "tablet", "cartouche","bgimage"]
    for i in range( len( images ) ):
        file_path = "Images/" + images[i] + ".png"
        images_dict[images[i]] = pygame.image.load( file_path )


def To_Pixels(x):
    return x * TILE_LENGTH


def Screen(tile_length):
    global TILE_LENGTH, screen
    TILE_LENGTH = tile_length

    Upload_Img()
    pygame.display.set_icon( images_dict["hieroglyph"] )
    pygame.display.set_caption( "Stones of the Pharaoh" )

    screen = pygame.display.set_mode( (800, 800 ))
    screen.blit( images_dict["bgimage"], (0, 0) )
    return screen


def Window(board, score, health):
    Draw_Bar( score, health )
    Draw_Board( board )

_circle_cache = {}
def _circlepoints(r):
    r = int(round(r))
    if r in _circle_cache:
        return _circle_cache[r]
    x, y, e = r, 0, 1 - r
    _circle_cache[r] = points = []
    while x >= y:
        points.append((x, y))
        y += 1
        if e < 0:
            e += 2 * y - 1
        else:
            x -= 1
            e += 2 * (y - x) - 1
    points += [(y, x) for x, y in points if x > y]
    points += [(-x, y) for x, y in points if x]
    points += [(x, -y) for x, y in points if y]
    points.sort()
    return points

def render(text, font, gfcolor=pygame.Color(253,193,78), ocolor=(38,28,3), opx=2):
    textsurface = font.render(text, True, gfcolor).convert_alpha()
    w = textsurface.get_width() + 2 * opx
    h = font.get_height()

    osurf = pygame.Surface((w, h + 2 * opx)).convert_alpha()
    osurf.fill((0, 0, 0, 0))

    surf = osurf.copy()

    osurf.blit(font.render(text, True, ocolor).convert_alpha(), (0, 0))

    for dx, dy in _circlepoints(opx):
        surf.blit(osurf, (dx + opx, dy + opx))

    surf.blit(textsurface, (opx, opx))
    return surf

def Draw_Bar(score, health):
    font = pygame.font.SysFont( "pegypta ", 48 )

    screen.blit( render( str( score ), font ), (To_Pixels( 4.5 ), To_Pixels( 10.65)) )
    screen.blit( render( str( health ), font ), (To_Pixels( 9.5 ), To_Pixels( 10.65 )) )


def Draw_Board(board):
    for y in range( len( board ) ):
        for x in range( len( board[y] ) ):
            Draw_Tile( board[y][x], x, y )


def Draw_Tile(number, x, y):
    img = None
    x = To_Pixels( x ) + 160
    y = To_Pixels( y ) + 45

    if number == 1:
        img = images_dict["scarab"]
    elif number == 2:
        img = images_dict["eye"]
    elif number == 3:
        img = images_dict["eagle"]
    elif number == 4:
        img = images_dict["tablet"]
    elif number == 5:
        img = images_dict["cartouche"]
    if number != 0:
        screen.blit( img, (x , y) )


def Border(x, y):
    x = To_Pixels( x )
    y = To_Pixels( y )
    border = pygame.Rect( x, y, TILE_LENGTH, TILE_LENGTH )
    pygame.draw.rect( screen, (0,255,252), border, 2 )


def GameOver(score):
    rect = pygame.Rect( To_Pixels( 0 ), To_Pixels( 2 ),
                        To_Pixels( 7 ), To_Pixels( 4 ) )
    pygame.draw.rect( screen, (255, 255, 255), rect, 0 )
    pygame.draw.rect( screen, (0, 255, 0), rect, 4 )
    font = pygame.font.SysFont( "impact", 100 )
    text = font.render( "SCORE", True, (0, 255, 0) )
    screen.blit( text, (To_Pixels( 2 ), To_Pixels( 2.6 )) )
    text = font.render( str(score), True, (0, 255, 0) )
    screen.blit( text, (To_Pixels( 2 ), To_Pixels( 4 )) )

    rect = pygame.Rect( To_Pixels( 7.25 ), To_Pixels( 6 ),
                        To_Pixels( 1.5 ), To_Pixels( 1 ) )
    pygame.draw.rect( screen, (255, 255, 255), rect, 0 )
    pygame.draw.rect( screen, (0, 255, 0), rect, 4 )
    font = pygame.font.SysFont( "impact", 30 )
    text = font.render( "PLAY AGAIN", True, (0, 255, 0) )
    screen.blit( text, (To_Pixels( 0.5 ), To_Pixels( 6 )) )