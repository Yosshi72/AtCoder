def main():
    N = int(input())
    A = list(map(int,input().split()))
    even_A = []
    for i in range(N):
        if A[i] %2 ==0:
            even_A.append(A[i])
    print(*even_A)

if __name__ == "__main__":
    main()
