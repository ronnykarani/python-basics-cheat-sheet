command = ""
while True:
    command = input(">").lower()
    if command == "start":
        print("Car started")
    elif command == "stop":
        print("Car stopped")
    elif command == "help":
        print("""
start - starts the car
stop - stops the car
quit - to quit
help - for help
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand you")
    
    