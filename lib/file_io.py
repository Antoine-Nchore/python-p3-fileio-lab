
def write_file(file_name, file_content):
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)

def append_to_file(file_name, append_content):
    with open(f"{file_name}.txt", "a") as file:
        file.write(f"\n{append_content}")

def read_file(file_name):
    try:
        with open(f"{file_name}.txt", "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found"

# Example usage
write_file(file_name="logfile", file_content="Log 1: 5 bananas added")
append_to_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

content = read_file(file_name="logfile")
print(content)

