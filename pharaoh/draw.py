import pygame

from pharaoh.constants import WIDTH, HEIGHT

pygame.init()
images_dict = {}


def Upload_Img():
    images = ["hieroglyph", "scarab", "eye", "eagle", "tablet", "cartouche"]
    for i in range( len( images ) ):
        file_path = "Images/" + images[i] + ".png"
        images_dict[images[i]] = pygame.image.load( file_path )


def To_Pixels(x):
    return x * TILE_LENGTH


def Screen(width, height, tile_length):
    global TILE_LENGTH, screen
    TILE_LENGTH = tile_length

    Upload_Img()
    pygame.display.set_icon( images_dict["hieroglyph"] )
    pygame.display.set_caption( "Stones of the Pharaoh" )

    screen = pygame.display.set_mode( (TILE_LENGTH * (width + 2), TILE_LENGTH * height ))

    return screen


def Window(board, score, health):
    screen.fill( (255, 255, 255) )
    Draw_Bar( score, health )
    Draw_Board( board )


def Draw_Bar(score, health):
    font = pygame.font.SysFont( "impact", 30 )

    text = font.render( "SCORE:", True, (0, 255, 255) )
    screen.blit( text, (To_Pixels( 7.5 ), To_Pixels( 0 )) )
    pygame.draw.line( screen, (0, 255, 255), (To_Pixels( 7.25 ), To_Pixels( 0.6 )),
                      (To_Pixels( 8.9 ), To_Pixels( 0.6 )), 1 )
    offset = 0
    if score >= 10000:
        offset = -0.60
    elif score >= 1000:
        offset = -0.45
    elif score >= 100:
        offset = -0.3
    elif score >= 10:
        offset = -0.15
    text = font.render( str( score ), True, (0, 255, 255) )
    screen.blit( text, (To_Pixels( 8 + offset ), To_Pixels( 0.6 )) )

    text = font.render( "HEALTH:", True, (255, 0, 0) )
    screen.blit( text, (To_Pixels( 7.5 ), To_Pixels( 1.5 )) )
    pygame.draw.line( screen, (255, 0, 0), (To_Pixels( 7.25 ), To_Pixels( 2.1 )),
                      (To_Pixels( 8.9 ), To_Pixels( 2.1 )), 1 )
    text = font.render( str( health ), True, (255, 0, 0) )
    screen.blit( text, (To_Pixels( 8 ), To_Pixels( 2.1 )) )


def Draw_Board(board):
    for y in range( len( board ) ):
        for x in range( len( board[y] ) ):
            Draw_Tile( board[y][x], x, y )


def Draw_Tile(number, x, y):
    img = None
    x = To_Pixels( x ) + 3
    y = To_Pixels( y ) + 3

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
    pygame.draw.rect( screen, (255, 0, 0), border, 2 )


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