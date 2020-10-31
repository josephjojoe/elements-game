import random

with open("elements.txt", "r") as file:
    elementsList = file.readlines()
    for i in range(0, len(elementsList)):
        elementsList[i] = elementsList[i].strip() # removes newline chars


def humanElementGuess(char): # character the element should begin with
    validElements = 0 # count of elements beginning with char
    for i in range(0, len(elementsList)):
        if elementsList[i][0] == char.upper():
            validElements += 1
        else:
            continue

    if validElements == 0:
        print(f"You lose! There are no more elements beginning with '{char}'")
        break

    inputElement = input(f"Enter an element beginning with '{char}': ")
    while inputElement[0].lower() != char:
        humanElementGuess(char)
    try:
        elementsList.remove(inputElement.title())
        computerElementGuess(inputElement[-1])
    except ValueError:
        print("Not a valid element" )
        humanElementGuess(char)
    


def computerElementGuess(char):
    nextElements = []
    for i in range(0, len(elementsList)):
        if elementsList[i][0] == char.upper():
            nextElements.append(elementsList[i])
    try:
        computerChoice = random.choice(nextElements)
        print(f"I choose: {computerChoice}")
        elementsList.remove(computerChoice)
        humanElementGuess(computerChoice[-1])
    except IndexError: # no elements in list, no more elements
        print(f"You win! There are no more elements beginning with '{char}'! ")


def main():
    inputElement = input("Element: ") # starting element

    try:
        elementsList.remove(inputElement.title())      
    except ValueError:
        print("Invalid element, try again: ")
        game()

    computerElementGuess(inputElement[-1])

if __name__ == '__main__':
    main()
