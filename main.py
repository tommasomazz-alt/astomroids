import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_TURN_SPEED
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Creo i gruppi di sprite pygame su cui poi chiamerò i metodi per draw e update
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    #Aggiungo la classe Player ai due gruppi
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    #Creo AsteroidField
    Asteroid_Field = AsteroidField()

    #Creo Giocatore
    Player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Game Loop
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)

        Player_1.draw(screen)
       

        pygame.display.flip()    
        dt = clock.tick(60) / 1000

	
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}" )
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")	




if __name__ == "__main__":
    main()
