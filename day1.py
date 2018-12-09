def run(data):
    freq = set()
    current = 0
    while True:
        for i in data:
            current += i
            if current in freq:
                return current
            else:
                freq.add(current)


with open('input_day1.txt') as f:
    data = [int(i) for i in f.read().splitlines()]
    print 'sum is ' + sum(data)

    print 'repeated at' + run(data)

    