safe_r = 0

def is_valid(l, fixed_already):
    safe = True
    for i in range(0, len(l) - 1):
        sum = l[i] - l[i+1]
        if sum < 1 or sum > 3:
            safe = False
            if fixed_already == False:
                # try to fix
                remove_me = list(l)
                del remove_me[i]
                if is_valid(remove_me, True):
                    safe = True
                else:
                    remove_next = list(l)
                    del remove_next[i+1]
                    if is_valid(remove_next, True):
                        safe = True
            if safe == False:
                break
    return safe

with open("input.txt") as f:
    for line in f:
        r = list(map(int, line.split()))
        if r[1] > r[0]:
             r.reverse()
        if is_valid(r, False):
            safe_r = safe_r + 1
        else:
            print(r)
        
print(safe_r)

