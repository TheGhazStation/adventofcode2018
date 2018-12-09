
maxX = 1000
maxY = 1000

def parseline(line):
    global maxX 
    global maxY
    p = line.split('#')[1].split(' ')
    claim = int(p[0])
    x, y = p[2].replace(':', '').split(',')
    l, w = p[3].split('x')
    x = int(x)
    y = int(y)
    l = int(l)
    w = int(w)
    maxX = max(maxX, x+l)
    maxY = max(maxY, y+w)

    return (claim, x, y, l, w)

def run():
    with open('data/input_day3_1.txt') as f:
        data = f.read().splitlines()
        lines = list(parseline(l) for l in data)
    
        count = 0
        grid = [[0]*maxX for i in range(maxY)]
        claims = set()
        for (claim, x, y, l, w) in lines:
             claims.add(claim)
             for i in range(x, x+l):
                for j in range(y, y+w):
                    if grid[i][j] == 0:
                        grid[i][j] = claim
                    elif grid[i][j] != -1:
                        claims.discard(grid[i][j])
                        count += 1
                        grid[i][j] = -1 
                        claims.discard(claim)
                    else:
                        claims.discard(claim)

        print('double claims ' + str(count))
        print('unique claim ' + str(claims.pop()))

run()