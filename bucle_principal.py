from mapa import laberinto
from delete_terminal import delete_terminal
import msvcrt
from convertir import convertir_mapa_a_matriz


def marcar_posicion_jugador(laberinto, posicion_inicial, posicion_final):

    # Extraer las coordenadas del jugador
    px, py = posicion_inicial
    terminado = False
    posicion_inicial = (0, 0)  # Posición inicial del jugador (fila, columna)
    posicion_inicial = (-1, -1)

    while not terminado:
            # Limpiar la pantalla y mostrar el mapa del laberinto
            delete_terminal(laberinto)

            # Verificar si la posición inicial es válida dentro del mapa
            if (
                0 <= px < len(laberinto[0]) and
                0 <= py < len(laberinto) and
                laberinto[py][px] != "#"
            ):
                # Marcar la posición del jugador en el mapa
                laberinto[py][px] = "@"  # Símbolo del jugador
                return laberinto  # Devolver el mapa actualizado
            else:
                # Error si la posición es inválida
                raise ValueError("Posición inicial inválida")

    mapa_laberinto_actualizado = marcar_posicion_jugador()
    # Imprimir el mapa del laberinto con la posición del jugador marcada
    for fila in mapa_laberinto_actualizado:
            print("".join(fila))

    tecla = input("Presiona una tecla (WASD o q para salir): ").lower()

    # Mover al jugador según la tecla presionada
    if tecla == "w":
            py -= 1  # Mover hacia arriba
    elif tecla == "s":
            py += 1  # Mover hacia abajo
    elif tecla == "a":
            px -= 1  # Mover hacia la izquierda
    elif tecla == "d":
            px += 1  # Mover hacia la derecha
    elif tecla == "q":
            terminado = True  # Salir del juego

    # Verificar si el jugador ha llegado a la posición final
    if px == posicion_final[0] and py == posicion_final[1]:
            terminado = True  # El jugador ha ganado
            print("¡Felicidades! Has encontrado la salida.")

    # Verificar si el jugador choca con una pared
    if laberinto[py][px] == "#":
            print("¡Ouch! Has chocado con una pared.")

    if terminado:
            delete_terminal(laberinto)
            print("Juego terminado.")
            
def obtener_la_tecla_de_flecha():
    if msvcrt.kbhit():
        key = msvcrt.getch()

        if key == b'\x80':
            key = msvcrt.getch()

            if key == b'\x3C':
                return 'w'  # Mover hacia arriba
            elif key == b'\x3E':
                return 's'  # Mover hacia abajo 
            elif key == b'\x3A':
                return 'a'  # Mover hacia la izquierda
            elif key == b'\x3B':
                return 'd'  # Mover hacia la derecha
        elif key == b'q':
            return 'q'  # Salir del juego

        else:
            return None 

    return None  

def actualizar_posición_jugador(posición_actual, letra):
    if letra == 'w':
        posición_tentativa = (posición_actual[0] - 1, posición_actual[1])
    elif letra == 's':
        posición_tentativa = (posición_actual[0] + 1, posición_actual[1])
    elif letra == 'a':
        posición_tentativa = (posición_actual[0], posición_actual[1] - 1)
    elif letra == 'd':
        posición_tentativa = (posición_actual[0], posición_actual[1] + 1)
    else:
        return posición_actual  # No valido

# Comprobar si la posición tentativa está dentro de los límites del laberinto
    if 0 <= posición_tentativa[0] < len(convertir_mapa_a_matriz) and 0 <= posición_tentativa[1] < len(convertir_mapa_a_matriz[0]):
    # Comprobar si la posición tentativa no es una pared   
     if convertir_mapa_a_matriz[posición_tentativa[0]][posición_tentativa[1]] != "#":
            return posición_tentativa
    else:
        return posición_actual 

    return posición_actual  


