import re

def mul(a, b):
    return a * b

def process_mul(mul_text):
    patt = "\\d+"
    mat = list(map(int, re.findall(patt, mul_text)))
    
    return mat[0] * mat[1]
        

with open("input.txt") as f:
    sum1 = 0
    sum2 = 0
    active = True
    switch_patt = "mul\\(\\d{1,3},\\d{1,3}\\)|do\\(\\)|don't\\(\\)"

    line = f.read().replace("\\n","")

    # find active ranges
    switch_matches = re.finditer(switch_patt, line)
    for s in switch_matches:
        if active and s.group() == "don't()":
            active = False
        elif not(active) and s.group() == "do()":
            active = True
        elif "mul" in s.group():
            # should be mul as the only other option
            prod = process_mul(s.group())
            #prod = eval(s.group())
            sum1 = sum1 + prod
            if active:
                sum2 = sum2 + prod
    
    print(sum1)
    print(sum2)