import pygame
import random
import sys

pygame.init()

NARANJA = (255, 128, 0)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)

ANCHO_PANTALLA = 400
ALTO_PANTALLA = 600
FPS = 60
TAMAÑO_METEORITO = 50
VELOCIDAD_METEORITOS = 3

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((TAMAÑO_METEORITO, TAMAÑO_METEORITO))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO_PANTALLA // 2
        self.rect.bottom = ALTO_PANTALLA - 10
        self.velocidad_x = 0

    def update(self):
        self.velocidad_x = 0
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.velocidad_x = -5
        if teclas[pygame.K_RIGHT]:
            self.velocidad_x = 5
        self.rect.x += self.velocidad_x
        if self.rect.right > ANCHO_PANTALLA:
            self.rect.right = ANCHO_PANTALLA
        if self.rect.left < 0:
            self.rect.left = 0

class Meteorito(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((TAMAÑO_METEORITO, TAMAÑO_METEORITO))
        self.image.fill(NARANJA)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO_PANTALLA - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.velocidad_y = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.top > ALTO_PANTALLA + 10:
            self.rect.x = random.randrange(ANCHO_PANTALLA - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.velocidad_y = random.randrange(1, 8)

# Función principal
def main():
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
    reloj = pygame.time.Clock()
    jugadores = pygame.sprite.Group()
    meteoritos = pygame.sprite.Group()

    jugador = Jugador()
    jugadores.add(jugador)

    for _ in range(8):
        meteorito = Meteorito()
        meteoritos.add(meteorito)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        jugadores.update()
        meteoritos.update()

        colisiones = pygame.sprite.spritecollide(jugador, meteoritos, False)
        if colisiones:
            pygame.quit()
            sys.exit()

        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        meteoritos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(FPS)

if __name__ == "__main__":
    main()
