import numpy as np
def main():
    H,W=map(int,input().split())
    A=[]
    B=[]
    for _ in range(H):
        A.append(list(input()))
    for _ in range(H):
        B.append(list(input()))
    A=np.array(A)
    B=np.array(B)
    for i in range(H):
        A=A.T
        A=leftShiftIndex(A,1)
        A=A.T
        for j in range(W):
            A=leftShiftIndex(A,1)
            print(A[0])
            if (A==B).all():
                print("Yes")
                return 0
    print("No")
def leftShiftIndex(arr, n):
   for i in range(n):
      temp = arr[:1]
      sample_array = arr[1:]
      arr = np.append(sample_array,temp,axis=0)
   return arr
if __name__=="__main__":
    main()