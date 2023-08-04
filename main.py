from settings import *
from sys import exit
from game import Game
from score import Score
from preview import Preview

class Main:
    def __init__(self):

        # setup :initialize pygame
        pygame.init()

        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tetris')

        # components
        # for the main game screen
        self.game = Game()
        self.score = Score()
        self.preview = Preview()

    def run(self):
        while(True):
            # get all the user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # exit everything ig quit
                    exit()

            # display
            self.display_surface.fill(GRAY)
            self.game.run()
            self.score.run()
            self.preview.run()

            # update the game
            pygame.display.update()

            # run the clock
            self.clock.tick()
            pass

if __name__ == '__main__':
    main = Main()
    main.run()