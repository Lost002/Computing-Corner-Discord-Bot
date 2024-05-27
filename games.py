from random import randint

def games(command):
    command = command.lower().split()

    if command[0] == "dice":
        roll = ""
        for _ in range(int(command[1])):
            roll += f" | {str(randint(1,6))} | "
        
        return roll

        