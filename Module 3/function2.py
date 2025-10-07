def someFunction1():
    print("Hello World")

def someFunction2():
    print("Hello World")

    return

    print("This print statement is unreachable")

def someFunction3():
    print("Hello World")

    return 10

def main():

    someFunction1()
    print()
    someFunction2()
    print()
    someFunction3()
    print()

    print(type(someFunction1()))
    print(someFunction1())
    print()

    print(type(someFunction2()))
    print(someFunction2())
    print()

    print(type(someFunction3()))
    print(someFunction3())
    print()
    

if __name__ == "__main__":
    main()