def main():
    N,A,B=map(int,input().split())
    C=list(map(int,input().split()))
    ans = A+B
    for i,c in enumerate(C):
        if ans == c:
            print(i+1)
            return 0
        
        
if __name__=="__main__":
    main()