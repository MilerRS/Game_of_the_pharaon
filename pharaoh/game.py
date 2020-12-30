import random
import numpy as np
from pharaoh import draw
from pharaoh.constants import WIDTH, HEIGHT, TILES


class Game:
    def __init__(self, screen, number, score, health):
        self.tiles = TILES
        self.counter = 0
        self.health = health
        self.screen = screen
        self.score = score
        if number == 2:
            self.board = self.init_array2()
        elif number == 3:
            self.board = self.init_array3()
        elif number == 4:
            self.board = self.init_array4()
        else:
            self.board = self.init_array5()
        draw.Window( self.board, self.score, self.health )

    def init_array2(self):
        board = np.random.randint( 1, 3, size=(HEIGHT, WIDTH) )
        return board
        # return [[random.randrange( 1, 3 ) for x in range( WIDTH )] for y in range( HEIGHT )]

    def init_array3(self):
        board = np.random.randint( 1, 4, size=(HEIGHT, WIDTH) )
        return board
        # return [[random.randrange( 1, 4 ) for x in range( WIDTH )] for y in range( HEIGHT )]

    def init_array4(self):
        board = np.random.randint( 1, 5, size=(HEIGHT, WIDTH) )
        return board
        # return [[random.randrange( 1, 5 ) for x in range( WIDTH )] for y in range( HEIGHT )]

    def init_array5(self):
        board = np.random.randint( 1, 5, size=(HEIGHT, WIDTH) )
        return board
        # return [[random.randrange( 1, 6 ) for x in range( WIDTH )] for y in range( HEIGHT )]

    def check_pos(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            return True
        return False

    def search_adj(self, row, col, value1, value2):

        if (row < 0 or row >= HEIGHT or col < 0 or
                col >= WIDTH or self.board[row][col] != value1 or
                self.board[row][col] == value2):
            return

        self.board[row][col] = value2
        draw.Border( col, row )
        self.counter += 1

        self.search_adj( row + 1, col, value1, value2 )
        self.search_adj( row - 1, col, value1, value2 )
        self.search_adj( row, col + 1, value1, value2 )
        self.search_adj( row, col - 1, value1, value2 )

    def floodFill(self, x, y, value2):
        value1 = self.board[x][y]
        self.search_adj( x, y, value1, value2 )

    def drop_tile(self):
        for j in range( WIDTH ):
            anker_i = HEIGHT - 1
            for i in range( HEIGHT - 1, -1, -1 ):
                if self.board[i][j] > 0:
                    self.board[anker_i][j] = self.board[i][j]
                    anker_i -= 1
            for i in range( anker_i + 1 ):
                self.board[i][j] = 0

        for j in range( WIDTH - 1, -1, -1 ):
            if self.board[HEIGHT - 1][j] == 0:
                for i in range( HEIGHT - 1,-1,-1):
                    for k in range( j-1,-1,-1):
                        self.board = self.shift( i, k, 1 )

    def shift_vector(self, v, i, n, empty=0):
        if n < 0:
            return self.shift_vector( v[::-1], len( v ) - i - 1, -n )[::-1]
        if n < len( v ) - i:
            # Find n empty places after i
            idx = np.where( np.cumsum( v[i + 1:] == empty ) == n )[0]
            last_zero_idx = idx[0] if len( idx ) > 0 else len( v ) - i - 1
            # Get non-empty values
            v_slice = v[i + 1:i + last_zero_idx + 1]
            values = v_slice[np.where( v_slice != empty )[0]]
            # Copy to vector
            v[i + n] = v[i]
            r = range( i + n + 1, min( i + last_zero_idx + 2, len( v ) ) )
            v[r] = values[:len( r )]
        v[i:i + n] = empty
        return v

    def shift(self, i, j, n, empty=0, inplace=False):
        out = self.board
        if not inplace:
            out = self.board.copy()

        out[i, :] = self.shift_vector( out[i, :], j, n, empty=empty )

        return out

    def check_health(self):
        if self.counter == 1:
            self.health -= 1
        self.score += self.counter * 100
        self.tiles -= self.counter

    def reset(self):
        for x in range( HEIGHT ):
            for y in range( WIDTH ):
                self.board[x][y] = abs( self.board[x][y] )
        draw.Window( self.board, self.score, self.health )
