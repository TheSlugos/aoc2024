import pathlib

class aoc:
    def __init__(self):
        self.rules = []
        self.sum = 0
        self.sum2 = 0

    def check_rule(self, before, after):
        y = [x for x in self.rules if x[0] == before and x[1] == after]
        if len(y) > 0:
            return True
        else:
            return False
    
    def fix(self, x):
        i = 1
        while i < len(x):
            j = i
            while j > 0 and not(self.check_rule(x[j-1], x[j])):
                tmp = x[j]
                x[j] = x[j - 1]
                x[j -1] = tmp
                j -= 1
            i += 1
    
    def run(self, fn):
        with open(pathlib.Path(__file__).parent.joinpath(fn), "r") as f:
            for line in f:
                if '|' in line:
                    x = list(map(int, line.strip().split("|")))
                    self.rules.append(x)
                elif ',' in line:
                    x = list(map(int, line.strip().split(",")))
                    valid = True
                    for i in range(len(x) - 1):
                        if not(self.check_rule(x[i], x[i+1])):
                            valid = False
                            self.fix(x)
                            break

                    if valid:
                        self.sum += x[len(x) // 2]
                    else:
                        self.sum2 += x[len(x) // 2]

        return (self.sum, self.sum2)

day05 = aoc()
assert(day05.run("test.txt") == (143,123))
print(day05.run("input.txt"))