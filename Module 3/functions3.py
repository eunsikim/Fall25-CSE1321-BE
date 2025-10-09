def main():
    message = "Hello World"

    for e in enumerate(message):
        print(e)

    print("Hello World".upper())

    print(message.replace("ell", "#"))

if __name__ == "__main__":
    main()