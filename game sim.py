# Example file showing a basic pg "game loop"
import pygame as pg

# game setup
board = [[None]*5 for _ in range(6)]

def rgb(r,g,b):
    # returns a tuple (this is a function so that I can see the colors with an extension)
    return r,g,b


COLORS = {
    2: rgb(247, 114, 115),
    4: rgb(169, 119, 244),
    8: rgb(255, 199, 2),
    16: rgb(129, 204, 99),
    32: rgb(100, 199, 255),
    64: rgb(255, 177, 120),
    128: rgb(88, 139, 218),
    256: rgb(170, 131, 100),
    512: rgb(0, 221, 170),
    1024: rgb(135, 135, 247),
    2048: rgb(119, 251, 255),
    4096: rgb(129, 143, 170),
    8192: rgb(251, 123, 171),
}

# pg setup
pg.init()
screen = pg.display.set_mode((440, 700))
clock = pg.time.Clock()
running = True




def render_board(board,screen):
    for r,row in enumerate(board):
        for c,block in enumerate(row):
            if block != None:
                color = COLORS[block]
                pg.draw.rect(screen,color,(80*c+22,204+80*r,76,76),0,12)
    





board[5][0] = 2048
board[5][1] = 256
board[5][2] = 4096
board[5][3] = 512
board[5][4] = 2048
board[4][0] = 64
board[4][1] = 128
board[4][2] = 512
board[4][3] = 2048
board[4][4] = 16
board[3][0] = 16
board[3][2] = 1024
board[2][0] = 8
board[1][0] = 4

for b in board:
    print(b)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(rgb(23, 24, 26))


    pg.draw.rect(screen, rgb(53, 56, 61), (15,195,410,490),3,3,3,3)
    
    for i in range(5):
        color = rgb(28, 29, 31) if i % 2 == 0 else rgb(30, 34, 37)
        # small bars showing where the block is from
        pg.draw.rect(screen,color,(80*i+20,110,80,80))
        
        # larger bars showing the current board
        pg.draw.rect(screen,color,(80*i+20,200,80,480))

    render_board(board,screen)

    pg.display.flip()
    clock.tick(60)

pg.quit()

