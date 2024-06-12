import os

def delete_terminal(numero):
  os.system('cls' if os.name == 'nt' else 'clear')

  print(numero)

numero = 0
while True:
  caracter = input()

  if caracter ==  "\x00\x48":
    numero += 1

  if numero == 50:
    break