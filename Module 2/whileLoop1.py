import time

def checker(number):
    time.sleep(2)
    print(f"Is {number} < 3? => {number < 3}")
    return True

def main():
    number = 0
    print(f"The value of `number` is {0}")
    print()

    time.sleep(2)

    while checker(number) and number < 3:
        print(f"Iteration #{number}")

        time.sleep(2)
        print(f"Increasing number from {number} to {number + 1}")
        number += 1 # number = number + 1
        print()
    
    print("Program terminated")

if __name__ == "__main__":
    main()