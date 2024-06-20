from mapa import laberinto
import os
from copy import deepcopy
from readchar import readkey, key

# Bienvenida al juego con inspiracion en Pirlo artista compositor Colombiano.

class DataGamers:
    def __init__(self):
        self.name_player = None

    def welcome_player(self):
        print('Bienvenido al juego Rata')
        self.name_player = input(str(' Ingresa tu nombre '))
        print(f'Chee!{self.name_player}, deja la cartilla y metete en la pelicula que la calle esta llena de gatos y vos sos mera Rata.')

    def play_game(self):
        self.welcome_player()
        return (self.welcome_player)


class Read_map:
    def __init__(self):
        self.position_x = None
        self.position_y = None
        self.position_end_x = None
        self.position_end_y = None
        self.laberinto = self.laberinto
        
# convierte a mapa 2D
    def map_matrix(self):
        mapa_matriz = []
        for fila in laberinto.split("\n"):
            fila_caracteres = []
        for caracter in fila:
            fila_caracteres.append(caracter)
        mapa_matriz.append(fila_caracteres)
        return mapa_matriz
# posiciones del jugador

    def find_start_and_end(self):
        for y in range(len(self.map_matrix)):
            for x in range(len(self.map_matrix[y])):
                if self.map_matrix[y][x] == 'P':
                    self.position_x = x
                    self.position_y = y
                elif self.map_matrix[y][x] == 'S':
                    self.position_end_x = x
                    self.position_end_y = y
# movimientos del jugador

    def movements(self):
        self.position_x = 0
        self.position_y = 0
        self.final_position = (-1, -1)
        while self.position_x != self.final_position[0] or self.position_y != self.final_position[1]:
            # movimiento hacia derecha
            if self.position_x + 1 < len(self.map_matrix) and self.map_matrix[self.position_y][self.position_x + 1] != '#':
                self.position_x += 1
        # movimiento hacia abajo
            elif self.position_y + 1 < len(self.map_matrix) and self.map_matrix[self.position_y + 1][self.position_x] != '#':
                self.position_y += 1
        # movimiento hacia izquierda
            elif self.position_x - 1 >= 0 and self.map_matrix[self.position_y][self.position_x - 1] != '#':
                self.position_x -= 1
        # movimiento hacia arriba
            elif self.position_y - 1 >= 0 and self.map_matrix[self.position_y - 1][self.position_x] != '#':
                self.position_x -= 1
            else:
                # retroceder movimiento
                if self.position_x + 1 < len(self.map_matrix) and self.map_matrix[self.position_y][self.position_x + 1] != '#':
                    self.position_x += 1
                elif self.position_y + 1 < len(self.map_matrix) and self.map_matrix[self.position_y + 1][self.position_x] != '#':
                    self.position_y += 1
                elif self.position_x - 1 >= 0 and self.map_matrix[self.position_y][self.position_x - 1] != '#':
                    self.position_x -= 1
                elif self.position_y - 1 >= 0 and self.map_matrix[self.position_y - 1][self.position_x] != '#':
                    self.position_x -= 1
# actualiza el mapa

    def date_map(self):
        self.movements()
        return (self.position_x,
                self.position_y,
                self.position_end_x,
                self.position_end_y,
                self.laberinto,
                )


class Clear_screen:

    @staticmethod
    def delete_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def print_tablero(tablero):
        Clear_screen().delete_terminal()
        for fila in tablero:
            string = ' '.join(fila)
            print(string)


class Logic_and_limit:
    pared = '#'

    def __init__(
        self,
        find_start_and_end,
        position_x,
        position_y,
        position_end_x,
        position_end_y,
        map,
        movements,
    ):
        self.map = map
        self.position_end_y = position_end_y
        self.position_end_x = position_end_x
        self.position_x = position_x
        self.position_y = position_y
        self.find_start_and_end = self.find_start_and_end
        self.movements = self.movements

    def poner_ficha_inicial_tablero(self):
        new_laberinto = deepcopy(self.map)
        new_laberinto[self.position_x][self.position_x] = self.find_start_and_end
        return new_laberinto

    def limite_pared(self, x: int, y: int):
        return self.map[x][y] != self.pared

    def limites_coordenadas(self, x: int, y: int):
        if x < 0 or y < 0:
            return False
        elif x <= self.position_x and y <= self.position_y:
            return self.limite_pared(x, y)
        elif x > self.position_x or y > self.position_y:
            return False

    def update(self, tecla: str):
        move = {
            key.DOWN: (1, 0),
            key.UP: (-1, 0),
            key.LEFT: (0, -1),
            key.RIGHT: (0, 1)
        }

        if tecla in move:
            dx, dy = move[tecla]
            if self.limites_coordenadas(self.x + dx, self.y + dy):
                new_laberinto = deepcopy(self.map)
                new_laberinto[self.x + dx][self.y +
                                           dy] = self.find_start_and_end
                self.position_x += dx
                self.position_y += dy
                return new_laberinto

            new_laberinto = deepcopy(self.map)
            new_laberinto[self.x][self.y] = self.find_start_and_end
            return new_laberinto

    def start_game(self):
        nuevo_laberinto = self.poner_ficha_inicial_tablero()
        Clear_screen().print_tablero(nuevo_laberinto)
        while (self.x, self.y) != (self.position_end_x,
                                   self.position_end_y):
            update = readkey()
            tablero_actualizado = self.update(update)
            Clear_screen().print_tablero(tablero_actualizado)


class Juego:
    def __init__(self):
        self.nombre_jugador = None
        self.logica_juego_instancia = None
        self.informacion_jugador()
        self.cargar_datos_mapa()

    def informacion_jugador(self):
        (
            self.nombre_jugador,
        ) = DataGamers().play_game()

    def cargar_datos_mapa(self):
        (
            coordenada_inicial_x,
            coordenada_inicial_y,
            coordenada_x_final_juego,
            coordenada_y_final_juego,
            map_matrix,
            coordenada_final_x,
            coordenada_final_y
        ) = Read_map().date_map()

        self.logica_juego_instancia = Logic_and_limit(
            map_matrix,
            coordenada_final_x,
            coordenada_final_y,
            coordenada_x_final_juego,
            coordenada_y_final_juego,
            coordenada_inicial_x,
            coordenada_inicial_y
        )

    def start(self):
        self.logica_juego_instancia.start_game()
        print(f"felicidades {self.nombre_jugador} has ganado")


game1 = Juego()
game1.start()
