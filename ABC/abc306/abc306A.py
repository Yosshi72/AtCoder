def main():
    N = int(input())
    S = list(input())
    ans = []
    for s in S:
        ans.append(s * 2)
    print(*ans, sep="")
    return 0


if __name__ == "__main__":
    main()
