import pathlib
from rich import print

def checkX(a, b, c):
    if a == 'M' and b == 'A' and c == 'S':
        return 1
    else:
        return 0
    
def checkS(a, b, c):
    if a == 'A' and b == 'M' and c == 'X':
        return 1
    else:
        return 0

def checkA(a,b,c,d):
    if a == 'M' and b == 'S' and c == 'M' and d == 'S':
        return 1
    elif a == 'M' and b == 'M' and c == 'S' and d == 'S':
        return 1
    elif a == 'S' and b == 'S' and c == 'M' and d == 'M':
        return 1
    elif a == 'S' and b == 'M' and c == 'S' and d == 'M':
        return 1
    else:
        return 0
    
map = []
height = 0
width = 0
word_count = 0
word_count2 = 0
with open(pathlib.Path(__file__).parent.joinpath("input.txt")) as f:
    for line in f:
        height += 1
        width = 0
        row = []
        for x in line.strip():
            width += 1
            row.append(x)
        #print(row)
        for x in range(0,3):
            row.insert(0, 'B')
            row.append('B')
        map.append(row)
print(f"{width} x {height}")
row_padding = ['B' for i in range(0,width + 6)]
for i in range(0,3):
    map.insert(0, row_padding)
    map.append(row_padding)

for r in range(3, height + 3):
    for c in range(3, width + 3):
        if map[r][c] == 'X':
            # check to the right
            word_count += checkX(map[r][c+1], map[r][c+2], map[r][c+3])
            word_count += checkX(map[r+1][c], map[r+2][c], map[r+3][c])
            word_count += checkX(map[r+1][c+1], map[r+2][c+2], map[r+3][c+3])
            word_count += checkX(map[r-1][c+1], map[r-2][c+2], map[r-3][c+3])
        elif map[r][c] == 'S':
            word_count += checkS(map[r][c+1], map[r][c+2], map[r][c+3])
            word_count += checkS(map[r+1][c], map[r+2][c], map[r+3][c])
            word_count += checkS(map[r+1][c+1], map[r+2][c+2], map[r+3][c+3])
            word_count += checkS(map[r-1][c+1], map[r-2][c+2], map[r-3][c+3])
        elif map[r][c] == 'A':
            word_count2 += checkA(map[r-1][c-1],map[r-1][c+1],map[r+1][c-1],map[r+1][c+1])
print(word_count)
print(word_count2)