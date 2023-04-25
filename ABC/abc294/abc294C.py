def make_C(A:list, B:list) -> tuple:
    (index_A,index_B) = (0,0)
    sorted_A = [ i for i in range(len(A))]
    sorted_B = [ i for i in range(len(B))]
    C = []
    while index_A < len(A) and index_B < len(B):
        if A[index_A] < B[index_B]:
            C.append(A[index_A])
            sorted_A[index_A] = len(C)
            index_A+=1
        else:
            C.append(B[index_B])
            sorted_B[index_B] = len(C)
            index_B+=1
    if index_A != len(A):
        sorted_A[index_A:] = [len(C)+i for i in range(1,len(A)-index_A+1)]
    if index_B != len(B):
        sorted_B[index_B:] = [len(C)+i for i in range(index_B+1,len(B)-index_B+1)]
    return sorted_A,sorted_B
def main():
    N,M = map(int,input().split())
    A= list(map(int,input().split()))
    B= list(map(int,input().split()))
    index_A,index_B = make_C(A,B)
    print(*index_A)
    print(*index_B)
    

if __name__ == "__main__":
    main()
