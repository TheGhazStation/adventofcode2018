
maxX = 1000
maxY = 1000

def parseline(line):
    global maxX 
    global maxY
    p = line.split('#')[1].split(' ')
    x, y = p[2].replace(':', '').split(',')
    l, w = p[3].split('x')
    x = int(x)
    y = int(y)
    l = int(l)
    w = int(w)
    maxX = max(maxX, x+l)
    maxY = max(maxY, y+w)

    return (x, y, l, w)

def part1():
    with open('data/input_day3_1.txt') as f:
        data = f.read().splitlines()
        lines = list(parseline(l) for l in data)
    
        count = 0
        grid = [[0]*maxX for i in range(maxY)]
        for (x, y, l, w) in lines:
             for i in range(x, x+l):
                 for j in range(y, y+w):
                     grid[i][j] += 1
                     if grid[i][j] == 2:
                         count += 1
        return count


print(part1())