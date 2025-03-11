def main():
    S=list(input())
    T=list(input())
    cheat=['a','t','c','o','d','e','r']
    hashed_S={}
    at_S=0
    at_T=0
    for s in S:
        if s=='@':
            at_S+=1
        else:
            if s in hashed_S:
                hashed_S[s]+=1
            else:
                hashed_S[s]=1
    for t in T:
        if t=='@':
            at_T+=1
        else:
            if t in hashed_S:
                hashed_S[t]-=1
            else:
                hashed_S[t]=-1
    for key in hashed_S:
        while hashed_S[key]!=0:
            if hashed_S[key] >0:
                if at_T >0 and key in cheat:
                    hashed_S[key]-=1
                    at_T-=1
                else:
                    print("No")
                    return 0
            else:
                if at_S>0 and key in cheat:
                    hashed_S[key]+=1
                    at_S-=1
                else:
                    print("No")
                    return 0
    if at_S!=at_T:
        print("No")
    else:
        print("Yes")

if __name__=="__main__":
    main()