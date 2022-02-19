
def main():

    result = '"'
 
    with open('abi.json', 'r') as f:
        lines = f.readlines()

    for line in lines:

        new_line = ""
        for char in line:
            if char == '"':
                new_line += "\\" + char
            else:
                new_line += char

        result += new_line.strip()

    result += '"'

    file = open("abi_converted.cs", "w")
    file.close()

    with open("abi_converted.cs", "w") as f:
        f.write(result)


if __name__ == "__main__":
    main()