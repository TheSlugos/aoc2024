# class DFA:
#     def __init__(self, Q, Sigma, delta, q0, F):
#         self.Q = Q # set of states
#         self.Sigma = Sigma # set of symbols
#         self.delta = delta # transition function as a dictionary
#         self.q0 = q0 # initial state
#         self.F = F # set of final states

#     def __repr__(self):
#         return f"DFA({self.Q},\n\t{self.Sigma}\n\t,{self.delta}\n\t,{self.q0},\n\t{self.F})"
state = 0
digit = 0
active = True
num1 = ""
num2 = ""
sum1 = 0
sum2 = 0
with open("input.txt") as f:
    for line in f:
        while line != "":
            match state:
                case 0:
                    digit = 0
                    num1 = ''
                    num2 = ''
                    if line[0] == 'm':
                        state = 1
                    elif line[0] == 'd':
                        state = 8
                    
                case 1:
                    if line[0] == 'u':
                        state = 2
                    else:
                        state = 0
                
                case 2:
                    if line[0] == 'l':
                        state = 3
                    else:
                        state = 0

                case 3:
                    if line[0] == '(':
                        state = 4
                    else:
                        state = 0

                case 4:
                    if line[0] in ['0','1','2','3','4','5','6','7','8','9']:
                        digit = digit + 1
                        num1 = num1 + line[0]
                        if digit > 3:
                            state = 0
                    elif line[0] == ',' and digit > 0:
                        state = 5
                        digit = 0
                    else:
                        state = 0
                
                case 5:
                    if line[0] in ['0', '1', '2', '3','4','5','6','7','8','9']:
                        digit = digit + 1
                        num2 = num2 + line[0]
                        if digit > 3:
                            state = 0
                    elif line[0] == ')' and digit > 0:
                        product = int(num1) * int(num2)
                        sum1 = sum1 + product
                        if active:
                            sum2 = sum2 + product
                        state = 0
                    else:
                        state = 0

                #d
                case 8:
                   if line[0] == 'o':
                       state = 9
                   else:
                       state = 0

                #do
                case 9:
                    if line[0] == '(':
                        state = 10
                    elif line[0] == 'n':
                        state = 11
                    else:
                        state = 0
                
                # do(
                case 10:
                    if line[0] == ')' and not(active):
                        active = True
                    state = 0

                #don
                case 11:
                    if line[0] == '\'':
                        state = 12
                    else:
                        state = 0

                #don'
                case 12:
                    if line[0] == 't':
                        state = 13
                    else:
                        state = 0

                #don't
                case 13:
                    if line[0] == '(':
                        state = 14
                    else:
                        state = 0

                #don't(
                case 14:
                    if line[0] == ')' and active:
                        active = False
                    state = 0
                    
            line = line[1:]
    print(sum1)
    print(sum2)