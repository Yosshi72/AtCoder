def main():
    A = list(map(int, input().split()))
    ans = 0
    for i, a in enumerate(A):
        if a == 1:
            ans += 2**i
    print(ans)


if __name__ == "__main__":
    main()
