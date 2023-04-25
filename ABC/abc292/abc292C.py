import numpy as np


def main():
    N = int(input())
    pairs = {}
    count = 0
    for i in range(1, N):
        ab = i
        cd = N - i
        if ab not in pairs.keys():
            pairs[ab] = divisor_list_s(ab)
        if cd not in pairs.keys():
            pairs[cd] = divisor_list_s(cd)
        count += pairs[ab] * pairs[cd]
    print(count)


def divisor_list_s(num):
    divisors = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i**2 == num:
                continue
            divisors.append(int(num / i))
    return len(divisors)


if __name__ == "__main__":
    main()
