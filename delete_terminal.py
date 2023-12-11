import os

def imprimir_numero(numero):
  os.system('cls' if os.name == 'nt' else 'clear')

  print(numero)

numero = 0
while True:
  tecla = input()

  if tecla == 'n':
    numero += 1

  if numero == 50:
    break