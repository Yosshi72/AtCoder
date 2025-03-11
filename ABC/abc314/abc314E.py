def main():
    N, M =map(int,input().split())
    for _ in range(N):
        inputValue = list(map(int,input().split()))
        C, P, S = inputValue[0], inputValue[1], inputValue[2:]
        print(C,P,S)
    return 0

if __name__ == "__main__":
    main()
