from collections import Counter

def part1():
    num2 = 0
    num3 = 0
    with open('data/input_day2_1.txt') as f:
        data = f.read().splitlines()
        for line in data:
            two = False
            three = False
            Counter(line)
            for i in c:
                if c[i] is 2:
                    two = True
                elif c[i] is 3:
                    three = True
            if two:
                num2 += 1
            if three:
                num3 += 1
        print(num2 * num3)

def find(data):
    l = len(data)
    for i in range(l):
        a = data[i]
        for j in range(i+1, l):
            b = data[j]
            off = 0
            r = ''
            for k in range(len(a)):
                if a[k] != b[k]:
                    off += 1
                else:
                    r += a[k]
            if off == 1:
                return r
    return []

                             

def part2():
    num2 = 0
    num3 = 0
    # with open('data/test3.txt') as f:
    with open('data/input_day2.txt') as f:
        data = f.read().splitlines()
        print(find(data))

part1()
part2()