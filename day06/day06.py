import sys
import pathlib
from aocd import get_data
from rich import print as rprint

def partone(map):
    start = ()
    for row in map:
        try:
            col_index = row.index('^')
            start = (map.index(row), col_index)
        except ValueError:
            pass

    height = len(map)
    width = len(map[0])

    pos = start
    up = (-1, 0)
    right = (0, 1)
    down = (1, 0)
    left = (0, -1)
    positions = set()
    dir = up
    while True:
        positions.add(pos)
        #map[pos[0]][pos[1]] = 'X'
        newpos = (pos[0] + dir[0], pos[1] + dir[1]) 
        if newpos[0] < 0 or newpos[0] >= height or newpos[1] < 0 or newpos[1] >= width:
            break

        if map[newpos[0]][newpos[1]] == '#':
            if dir == up:
                dir = right
            elif dir == right:
                dir = down
            elif dir == down:
                dir = left
            else:
                dir = up
        else:
            pos = newpos

    return positions

def testloop(barrier, map):
    start = ()
    for row in map:
        try:
            col_index = row.index('^')
            start = (map.index(row), col_index)
        except ValueError:
            pass

    if barrier == start:
        return 0
    
    # place temp barrier
    map[barrier[0]][barrier[1]] = '#'

    height = len(map)
    width = len(map[0])

    pos = start
    up = (-1, 0)
    right = (0, 1)
    down = (1, 0)
    left = (0, -1)
    
    positions = set()
    dir = up

    while True:
        state = pos + dir

        if state in positions:
            # have found a previously visited position and direction => loop
            map[barrier[0]][barrier[1]] = '.'
            return 1
        
        positions.add(state)
        newpos = (pos[0] + dir[0], pos[1] + dir[1]) 
        if newpos[0] < 0 or newpos[0] >= height or newpos[1] < 0 or newpos[1] >= width:
            break

        if map[newpos[0]][newpos[1]] == '#':
            if dir == up:
                dir = right
            elif dir == right:
                dir = down
            elif dir == down:
                dir = left
            else:
                dir = up
        else:
            pos = newpos

    map[barrier[0]][barrier[1]] = '.'
    return 0

path = "day06\\input.txt"

print(f"{path}")
puzzle_input = pathlib.Path(path).read_text().strip()
map = [[a for a in line] for line in puzzle_input.split('\n')]

positions = partone(map)        
rprint(f"Locations visited: {len(positions)}")

loops = 0
for x in positions:
    loops += testloop(x, map)

rprint(f"Loops: {loops}")