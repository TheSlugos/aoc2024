import re

def process_mul(mul_text):
    patt = "\d+"
    mat = list(map(int, re.findall(patt, mul_text)))
    
    return mat[0] * mat[1]
        

with open("input.txt") as f:
    sum1 = 0
    sum2 = 0
    active = True
    mul_patt = "mul\(\d{1,3},\d{1,3}\)"
    switch_patt = "do\(\)|don't\(\)"
    active_ranges = []
    on_min = 0 # on by default
    for line in f:
        # find active ranges
        switch_matches = re.finditer(switch_patt, line)
        for s in switch_matches:
            if active and s.group() == "don't()":
                this_range = [on_min, s.start()]
                active_ranges.append(this_range)
                active = False
            elif not(active) and s.group() == "do()":
                on_min = s.start()
                active = True
        if active:
            this_range = [on_min, len(line)]
            active_ranges.append(this_range)

        # process matches
        mul_matches = re.finditer(mul_patt, line)
        for match in mul_matches:
            sum1 = sum1 + process_mul(match.group())
            for r in active_ranges:
                if match.start() >= r[0] and match.start() <= r[1]:
                    sum2 = sum2 + process_mul(match.group())
                    break
        #print(active_ranges)

        #reset for next line
        active_ranges = []  # clear range at end of line - derp
        on_min = 0  # reset min at end of line - derpx2
    
    print(sum1)
    print(sum2)