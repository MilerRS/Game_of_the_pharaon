import pygame
from pharaoh import draw, sounds
from pharaoh.game import Game
from pharaoh.constants import FPS, WIDTH, HEIGHT, TILE_LENGTH

pygame.init()
screen = draw.Screen( TILE_LENGTH )


def get_row_col_from_mouse(pos):
    x, y = pos
    print( y, x )
    row = y // TILE_LENGTH - 1
    col = x // TILE_LENGTH - 2
    print( row + 1, col + 2 )
    print( row, col )
    return row, col


if __name__ == '__main__':
    run = True
    clock = pygame.time.Clock()
    difficulty = 2
    score = 0
    health = 5
    game = Game( screen, difficulty, score, health )

    selected = False
    selected_row = None
    selected_col = None
    game_over = False

    pygame.mixer.init()
    music = sounds.load_sound( "music" )
    music.play( -1 )
    sounds.load()

    while run:
        clock.tick( FPS )

        if game.health == 0:
            draw.GameOver( game.score )
            sounds.play_effect( "win" )
            game_over = True
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and game_over == True:
                        difficulty = 2
                        score = 0
                        health = 5
                        game = Game( screen, difficulty, score, health )

                        selected = False
                        selected_row = None
                        selected_col = None
                        game_over = False

        if game.tiles == 0:
            if difficulty < 5:
                difficulty += 1
            game = Game( screen, difficulty, game.score, game.health )



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # tuple from the left-click
                row, col = get_row_col_from_mouse( mouse_pos )
                if col < WIDTH and row < HEIGHT and game_over == False:
                    if not selected:
                        game.counter = 0
                        game.floodFill( row, col, -game.board[row][col] )
                        selected = True
                        selected_row = row
                        selected_col = col

                    elif selected:
                        if game.check_pos( selected_row, selected_col, row, col ):
                            game.drop_tile()
                            game.check_health()
                            draw.Window( game.board, game.score, game.health )
                            sounds.play_effect( "pop" )

                        else:
                            game.reset()

                        selected = False
                        selected_row = None
                        selected_col = None
        pygame.display.update()

    pygame.quit()
