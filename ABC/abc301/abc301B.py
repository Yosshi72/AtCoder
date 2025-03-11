def main():
    N=int(input())
    A=list(map(int,input().split()))
    print(*insert_numbers(A))
    
def insert_numbers(A):
    while True:
        i = 0
        while i < len(A) - 1:
            if abs(A[i] - A[i+1]) == 1:
                i += 1
            else:
                break
        else:
            break
        start=A[i]
        end=A[i+1]
        if A[i] < A[i+1]:
            for j in range(A[i]+1, A[i+1]):
                i+=1
                A.insert(i, j)
        else:
            for j in range(A[i]-1, A[i+1], -1):
                i+=1
                A.insert(i, j)
                
    return A
if __name__=="__main__":
    main()