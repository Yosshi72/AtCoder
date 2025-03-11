def main():
    N = int(input())
    S =[]
    for _ in range(N):
        S.append(input())
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if S[i]+S[j] == S[j][::-1]+S[i][::-1]:
                print("Yes")
                return 0
    print("No")
    return 0

if __name__ == "__main__":
    main()
