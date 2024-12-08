import pathlib

reading_rules = True
rules = []
sum = 0
sum2 = 0

def check_rule(r, before, after):
    y = [x for x in r if x[0] == before and x[1] == after]
    if len(y) > 0:
        return True
    else:
        return False
    
def fix(r, x):
    i = 1
    while i < len(x):
        j = i
        while j > 0 and not(check_rule(r, x[j-1], x[j])):
            tmp = x[j]
            x[j] = x[j - 1]
            x[j -1] = tmp
            j -= 1
        i += 1
    
with open(pathlib.Path(__file__).parent.joinpath("input.txt"), "r") as f:
    for line in f:
        if '|' in line:
            x = list(map(int, line.strip().split("|")))
            rules.append(x)
        elif ',' in line:
            x = list(map(int, line.strip().split(",")))
            valid = True
            for i in range(len(x) - 1):
                if not(check_rule(rules, x[i], x[i+1])):
                    valid = False
                    fix(rules, x)
                    break

            if valid:
                sum += x[len(x) // 2]
            else:
                sum2 += x[len(x) // 2]

print(sum)
print(sum2)
    

        