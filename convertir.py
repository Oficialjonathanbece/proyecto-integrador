def convertir_mapa_a_matriz(laberinto):

  mapa_matriz = []
  for fila in laberinto.split("\n"):
    fila_caracteres = []
    for caracter in fila:
      fila_caracteres.append(caracter)
    mapa_matriz.append(fila_caracteres)
  return mapa_matriz

simbolo_inicial = "@"
simbolo_final = "@"
mapa_matriz = convertir_mapa_a_matriz

mapa_matriz[0][0] = simbolo_inicial

ultima_fila = len(mapa_matriz) - 1
ultima_columna = len(mapa_matriz[0]) - 1
mapa_matriz[ultima_fila][ultima_columna] = simbolo_final

laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

mapa_matriz = convertir_mapa_a_matriz(laberinto)
print(mapa_matriz)
