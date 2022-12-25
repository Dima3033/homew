with open("1file.txt", "w") as file:
    print("Car", file=file)
    print("is", file=file)
    print("faster than", file=file)
    print("human", file=file)

with open("1file.txt", "r") as file1:
    read = file1.readline()
    count = read.count(' ')
    read_1 = file1.readline()
    count_1 = read_1.count(' ')
    read_2 = file1.readline()
    count_2 = read_2.count(' ')
    read_3 = file1.readline()
    count_3 = read_3.count(' ')

    if count == 0:
        with open("1file.txt", "w") as file:
            print(read, file=file)
            print("------------", file=file)
            print(read_1, file=file)
            print(read_2, file=file)
            print(read_3, file=file)

    if count_1 == 0:
        with open("1file.txt", "w") as file:
            print(read, file=file)
            print(read_1, file=file)
            print("------------", file=file)
            print(read_2, file=file)
            print(read_3, file=file)

    if count_2 == 0:
        with open("1file.txt", "w") as file:
            print(read, file=file)
            print(read_1, file=file)
            print(read_2, file=file)
            print("------------", file=file)
            print(read_3, file=file)

    if count_3 == 0:
        with open("1file.txt", "w") as file:
            print(read, file=file)
            print(read_1, file=file)
            print(read_2, file=file)
            print(read_3, file=file)
            print("------------", file=file)
    print(f"{read}")
    print(f"{count}")