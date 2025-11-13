# What is the output
def main():
    try:
        num = int("3.14")
        
        print("Try block executed successfully!")
    except ValueError:
        print("Error!")
    except Exception:
        print("Catastrophic Error!")
    

if __name__ == "__main__":
    main()