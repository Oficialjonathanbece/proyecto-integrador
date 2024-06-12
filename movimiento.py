import readchar  # Import the 'readchar' library

while True:
    # Read a single character without waiting for Enter
    tecla = readchar.readkey()

    # Check if the pressed key is one of WASD
    if tecla.name in ["w", "a", "s", "d"]:
        print(f"You pressed: {tecla.name}")  # Display the pressed key (WASD)

    # Check if the user wants to quit (press 'q')
    if tecla.name == "q":
        break  # Exit the loop
