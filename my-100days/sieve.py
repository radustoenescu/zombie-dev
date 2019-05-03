import itertools

def sieve():
    # begin with all natural numbers above 1
    picker = itertools.count(2)
    while True:
        # take the next available number
        v = next(picker)
        yield v
        # filter from the generator its multiples
        picker = filter(lambda x, prime = v: x % prime != 0, picker)

if __name__ == '__main__':
    s = sieve()
    for i in range(0,100000):
        print(next(s))

