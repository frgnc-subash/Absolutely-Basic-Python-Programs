# Initialize car position
position = 0
running = True

print("Welcome to the Car Game!")
print("Commands: 'forward', 'backward', 'stop'")

while running:
    # Get user input
    command = input("Enter command: ").strip().lower()
    
    if command == "forward":
        position += 1
        print(f"Your car is at position {position}.")
    elif command == "backward":
        position -= 1
        print(f"Your car is at position {position}.")
    elif command == "stop":
        print("Stopping the car. Goodbye!")
        running = False
    else:
        print("Invalid command. Please use 'forward', 'backward', or 'stop'.")
