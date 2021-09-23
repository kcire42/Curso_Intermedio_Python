


def write():
    names = ["Erick", "Nayeli", "Carlos", "Juan"]
    with open("./archivos/numbers.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
    

    


def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(line)
    print(numbers)

def main():
    read()
    write()
    read()

if __name__ == '__main__':
    main()