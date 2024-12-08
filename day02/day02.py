safe_r = 0
safe_r2 = 0

def is_valid(l, fixed_already):
    safe = True
    for i in range(0, len(l) - 2):
        sum1 = l[i] - l[i+1]
        sum2 = l[i+1] - l[i+2]
        if sum1 == 0 or abs(sum1) > 3 or sum2 == 0 or abs(sum2) > 3 or (sum1 < 0 and sum2 > 0) or (sum1 > 0 and sum2 < 0):
            safe = False
            if fixed_already == False:
                # try to fix
                remove_me = list(l)
                del remove_me[i]
                if is_valid(remove_me, True):
                    return True
                remove_next = list(l)
                del remove_next[i+1]
                if is_valid(remove_next, True):
                    return True 
                remove_last = list(l)
                del remove_last[i+2]
                if is_valid(remove_last, True):
                    return True
            break
    return safe

with open("input.txt") as f:
    for line in f:
        r = list(map(int, line.split()))
        if is_valid(r, True):
            safe_r = safe_r + 1
        else:
            if is_valid(r, False):
                safe_r2 = safe_r2 + 1
        
print(safe_r)
print(safe_r + safe_r2)