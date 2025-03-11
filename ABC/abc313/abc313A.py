def main():
    N = int(input())
    P = list(map(int, input().split()))
    p1 = P[0]
    count = 0
    for i in range(1,len(P)):
        if p1 > P[i]:
            continue
        elif p1 == P[i]:
            p1 +=1
            count +=1
        else:
            count += (P[i] - p1+1)
            p1 = P[i] + 1
    print(count)
    return 0


if __name__ == "__main__":
    main()
