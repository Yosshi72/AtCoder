def main():
    N=int(input())
    class_sum=[[0],[0]]
    for n in range(N):
        c,p=map(int,input().split())
        if c==1:
            class_sum[0].append(class_sum[0][n]+p)
            class_sum[1].append(class_sum[1][n])
        else:
            class_sum[0].append(class_sum[0][n])
            class_sum[1].append(class_sum[1][n]+p)            
    Q=int(input())
    for q in range(Q):
        l,r=map(int,input().split())
        print(class_sum[0][r]-class_sum[0][l-1],class_sum[1][r]-class_sum[1][l-1])

if __name__=="__main__":
    main()

