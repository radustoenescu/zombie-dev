def count_bits(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count


def count_bits_wicked(n):
    count = 0
    while n > 0:
        n &= n - 1
        count += 1
    return count


if __name__ == '__main__':
    number = 0b0101010101010010010101010010101010101
    assert 17 == count_bits(number)
    assert count_bits(number) == count_bits_wicked(number)