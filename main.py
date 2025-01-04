import pygame
import sys
import math

def spiral_pixel_transition(screen, width, height, tile_size=20, speed=6):
    """Realiza una transición en espiral pixelada."""
    # Dividir la pantalla en una cuadrícula de tiles
    rows = math.ceil(height / tile_size)
    cols = math.ceil(width / tile_size)

    # Crear una lista con las posiciones de todos los tiles
    tiles = [(x * tile_size, y * tile_size) for y in range(rows) for x in range(cols)]

    # Ordenar los tiles en forma de espiral
    center_x, center_y = width // 2, height // 2
    tiles.sort(key=lambda pos: math.atan2(pos[1] - center_y, pos[0] - center_x))

    clock = pygame.time.Clock()
    revealed_tiles = 0
    total_tiles = len(tiles)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fondo negro para cubrir la pantalla
        screen.fill((0, 0, 0))

        # Dibujar los tiles revelados en cada frame
        for i in range(revealed_tiles):
            x, y = tiles[i]
            pygame.draw.rect(screen, (0, 255, 0), (x, y, tile_size, tile_size))

        pygame.display.flip()
        clock.tick(120)  # Aumentar la tasa de cuadros para mayor fluidez

        # Incrementar la cantidad de tiles revelados
        revealed_tiles += speed
        if revealed_tiles >= total_tiles:
            running = False


def main():
    pygame.init()

    # Tamaño de la ventana
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Transición en Espiral Pixelada")

    # Loop principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Ejecutar la transición al presionar la barra espaciadora
                spiral_pixel_transition(screen, WIDTH, HEIGHT)

        # Fondo verde (representando el mapa o pantalla base)
        screen.fill((0, 255, 0))
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
