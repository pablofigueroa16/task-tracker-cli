from ast import arg
import sys

def main():
    args = sys.argv[1:]
    if not args:
        print("Please provide a command.")
        return
    
    command = args[0]

    if command == "add":
        print("Add a task:",args[1:])
    else:
        print("Invalid command.", command)

if __name__ == "__main__":
    main()
