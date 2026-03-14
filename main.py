import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #Creo Giocatore
    Player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Game Loop
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        Player_1.draw(screen)
        pygame.display.flip()    
        dt = clock.tick(60) / 1000

	
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}" )
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")	




if __name__ == "__main__":
    main()
