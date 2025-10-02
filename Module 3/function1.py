def printMenu():
    print("1 -> Print Hello World")
    print("2 -> Calculate force")
    print("X -> To stop")

    return input("> ") #1

def printHelloWorld():
    print("Hello World")

def forceHandler():
    mass = float(input("Enter mass: "))
    acceleration = float(input("Enter acceleration: "))
    print(f"Force is {forceCalc(mass, acceleration)}")

def forceCalc(mass, acceleration):
    force = mass * acceleration

    return force

def main():
    while True:
        option = printMenu() #1
        if option == "1":
            printHelloWorld()
        elif option == "2":
            forceHandler()
        elif option == "X":
            break

if __name__ == "__main__":
    main()