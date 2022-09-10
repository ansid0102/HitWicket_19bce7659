import pygame 
from chess.constants import WIDTH,HEIGHT
from chess.board import *
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('CHESS-5/5')
FPS = 60
def main():
    run = True
    board = Board()
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        board.draw(WINDOW)
        pygame.display.update()
    pygame.quit()
main()