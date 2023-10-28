import pygame
# se definene las clases y funciones del juego
class Figura:
    def __init__(self, x, y, forma):
        self.x = x
        self.y = y
        self.forma = forma

    def mover_izquierda(self):
        self.x += 1

    def mover_derecha(self):
        self.x -= 1

    def rotar(self):
        self.forma = (self.forma[1],self.forma[0])

    def dibujar(self,pantalla):
        for i in range(len(self.forma)):
            for j in range(len(self.forma[i])):
                if self.forma[i][j] == 1:
                    pygame.draw.rect(pantalla,(255,0,0)),
                    (self.x + j * 20, self.y + i * 20, 20, 20)

class Juego:
    def __init__(self):
        self.pantalla = pygame.display.set_mode((400, 600))
        self.figuras = []
        self.figura_actual = Figura(100, 200, [(1, 1), (1, 0), (0, 0), (0, 1)])

    def actualizar(self):
        self.figura_actual.mover_abajo()

    def dibujar(self):
        self.pantalla.fill((0, 0, 0))
        for figura in self.figuras:
            figura.dibujar(self.pantalla)
        self.figura_actual.dibujar(self.pantalla)

    def ejecutar(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.actualizar()
            self.dibujar()
            pygame.display.update()

# Inicia el juego

juego = Juego()
juego.ejecutar()