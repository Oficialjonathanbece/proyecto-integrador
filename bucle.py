import readchar

#Bucle infinito hasta presionar el UP

while True:
    caracter = readchar.readkey()
    print(caracter)
    if ord(caracter) == "UP":
        break


