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

import heapq

# In the proper sieve we will cross multiples as we go,
# For each prime we found we'll keep its largest multiple generated
# that wasn't reached so far in our search.
#
# When our iteration reaches a multiple, it gets popped and the next
# multiple is inserted in the heap.
def proper_sieve():
    yield 2
    crt = 3
    cross_list = [(4,2)]

    while True:
        next_crossed = cross_list[0]
        if next_crossed[0] > crt:
            for n in range(crt, next_crossed[0]):
                yield n
                heapq.heappush(cross_list, (n * n, n))
            crt = next_crossed[0]
        else:
            while next_crossed[0] == crt:
                heapq.heappop(cross_list)
                heapq.heappush(cross_list, (next_crossed[0] + next_crossed[1], next_crossed[1]))
                next_crossed = cross_list[0]
            crt += 1

if __name__ == '__main__':
    s = proper_sieve()
    for i in range(0,100000):
        print(next(s))
