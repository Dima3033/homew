try:
    with open("task.txt", "w") as file:
        file.write("While many of the world's top fashion designers now work in London,"
                   "  some of London's top designers, such as John Galliano,"
                   "are now in charge of major collections in Paris and New York.,"
                   "  Vivienne Westwood, who looked at London's punk styles and redesigned them for the international"
                   " off-the-peg market, is perhaps the most significant fashion designer of the past 50 years."
                   " Meanwhile Stella McCartney, the daughter of Paul McCartney")
    with open("task.txt", "r") as file:
        for line in file:
            print("Full text: ", line, end=" ")
    print()
    list = []
    s = line.split(' ')
    for i in s:
        a = len(i)
        if a > 7:
            list.append(i)
            with open("7+letters.txt", "w") as fle:
                print(f"Слова які мають 7 і більше літер: {list}", file=fle)
                print(f"Слова які мають 7 і більше літер: {i}")
except Exception as ex:
    print(f"Error: {ex}")