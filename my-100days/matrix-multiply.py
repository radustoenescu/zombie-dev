#2 mins to think
#17 mins to code
# 9 mins to debug

# https://en.wikipedia.org/wiki/Matrix_chain_multiplication
# https://medium.com/100-days-of-algorithms/day-2-matrix-chain-multiplication-3ae6349c34ab
import functools

def best_order(chain):
    size = len(chain)

    @functools.lru_cache(maxsize=1_000_000)
    def opt_section(i, j):
        assert 0 <= i <= j < size

        # one matrix - do nothing
        if (i == j):
            best = (chain[i][0], chain[i][1], 0)
        # base case 2 matrices
        elif (j - i == 1):
            # they can be multiplied
            assert chain[i][1] == chain[j][0]
            best = (chain[i][0], chain[j][1], chain[i][0] * chain[i][1] * chain[j][1])
        else:
            best = (None, None, None)
            for k in range(i + 1, j):
                r = combine(opt_section(i, k), opt_section(k + 1, j))
                best = better(r, best)
        return best

    return opt_section(0, size-1)


def better(a, b):
    assert a[2] or b[2]
    if (not b[2] or (a[2] <= b[2])):
        return a
    else:
        return b


def combine(l, r):
    lr, lc, lcost = l
    rr, rc, rcost = r
    return (lr, rc, lcost + rcost + lr * lc * rc)

if __name__ == '__main__':
    # chain = [(10, 20), (20, 30), (30, 40)]
    chain = [(10, 30), (30, 5), (5, 60)]
    print(best_order(chain))
