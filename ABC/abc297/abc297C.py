def main():
    H,W=map(int,input().split())
    for h in range(H):
        S=list(input())
        p=0
        while p<len(S)-1:
            if S[p]==S[p+1]=="T":
                S[p]="P"
                S[p+1]="C"
                p+=2
            else:
                p+=1
        print("".join(S))

if __name__=="__main__":
    main()