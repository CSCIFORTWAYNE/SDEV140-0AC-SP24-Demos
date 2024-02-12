import random

colorOut = {"RED":"\033[38;5;196m\033[48;5;88m", "PURPLE":"\033[38;5;135m\033[48;5;53m", "YELLOW":"\033[38;5;226m\033[48;5;178m", "GREEN":"\033[38;5;118m\033[48;5;2m", "BLUE":"\033[38;5;81m\033[48;5;4m", "ORANGE":"\033[38;5;214m\033[48;5;166m"}
numColor = {1:"RED", 2:"PURPLE",3:"YELLOW", 4:"GREEN", 5:"BLUE", 6:"PURPLE"}
STARTCOLOR = "\033[1m"
RESETCOLOR = "\033[0m"
gameBoard = []

def main():
    generateGameboard()
    for space in gameBoard:
        print(printConsoleColor(space) + "[ ]")
        print(RESETCOLOR," ")


def printConsoleColor(color):
    out = STARTCOLOR
    out += colorOut[color.upper()]
    return out
def generateGameboard():
    for i in range(115):
        gameBoard.append(numColor[random.randint(1,6)])


if __name__ == "__main__":
    main()

