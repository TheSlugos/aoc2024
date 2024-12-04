map = []

with open("test.txt") as f:
    for line in f:
        row = []
        for x in line.strip():
            row.append(x)
        print(row)
        map.append(row)
    print(len(map),len(map[0]))