def main():
    N = int(input())

    if N <= 10**3 - 1:
        print(N)
    elif N <= 10**4 - 1:
        N = (N // 10) * 10
        print(N)
    elif N <= 10**5 - 1:
        N = (N // 100) * 100
        print(N)
    elif N <= 10**6 - 1:
        N = (N // 1000) * 1000
        print(N)
    elif N <= 10**7 - 1:
        N = (N // 10000) * 10000
        print(N)
    elif N <= 10**8 - 1:
        N = (N // 100000) * 100000
        print(N)
    else:
        N = (N // 1000000) * 1000000
        print(N)


if __name__ == "__main__":
    main()
