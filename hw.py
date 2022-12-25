try:
    with open("file.txt", "w") as file4:
        print("Car", file=file4)
        print("is", file=file4)
        print("faster", file=file4)
        print("than human", file=file4)

    with open("file.txt", "r") as file4:
        con = file4.readlines()
    list = []
    with open("file.txt", "w") as file5:
        for item in con:
            a = list.append(item.replace("\n", ""))
            r = list[::-1]
            a = list[-1]
            s = []
            for i in a:
                s.append(i)
            s = s.reverse()
            print(s)
            del list[0]
    print("----------")
except Exception as ex:
    print(f"Error: {ex}")