def main():
    N = int(input())
    S = list(input())
    intS = [int(c) for c in S]

    count = sum(intS)

    prevValue = NAND(intS[0], intS[1])
    prevNAND = [prevValue]
    i = 2
    while i < N:
        prevValue = NAND(prevValue, intS[i])
        prevNAND.append(prevValue)
        i += 1
    count += sum(prevNAND)

    j = 1
    while j < N:
        print(prevNAND)
        if prevNAND[0] != intS[j]:
            prevNAND = prevNAND[:-1]
        else:
            prevNAND = prevNAND[1:]
        count += sum(prevNAND)
        j +=1
    print(count)
    return 0


def NAND(x, y):
    return int((not x or not y))
if __name__ == "__main__":
    main()
