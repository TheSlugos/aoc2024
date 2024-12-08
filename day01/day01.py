first = []
second = []
counter = {}
sum = 0
sum1 = 0
with open("input.txt") as f:
    for line in f:
        r = line.split()
        first.append(r[0])
        second.append(r[1])
        counter[r[1]] = counter.get(r[1], 0) + 1
first.sort()
second.sort()
for i in range(len(first)):
    sum = sum + abs(int(second[i]) - int(first[i]))
    sum1 = sum1 + int(first[i]) * counter.get(first[i], 0)
print(sum)
#print(first)
#print(counter)
print(sum1)