

def create_and_write_file():
    try:
        # Create a new text file and write initial content
        with open("my_file.txt", 'w') as file:
            file.write("Hello, this is line 1.\n")
            file.write("This is line 2 with a number: 42.\n")
            file.write("Another line: line 3.\n")
        print("File created and initial content written successfully.")
    except PermissionError:
        print("Permission denied: unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("create_and_write_file() completed.\n")


def read_file():
    try:
        # Read and display the contents of the file
        with open("my_file.txt", 'r') as file:
            content = file.read()
        print("File content:")
        print(content)
    except FileNotFoundError:
        print("File not found: cannot read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("read_file() completed.\n")


def append_to_file():
    try:
        # Open the file in append mode and add more content
        with open("my_file.txt", 'a') as file:
            file.write("Appending line 4.\n")
            file.write("Appending line 5 with a number: 99.\n")
            file.write("Final line: line 6.\n")
        print("Additional content appended successfully.")
    except PermissionError:
        print("Permission denied: unable to append to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("append_to_file() completed.\n")


# Main execution
create_and_write_file()
read_file()
append_to_file()
read_file()
