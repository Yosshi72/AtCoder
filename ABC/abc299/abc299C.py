def main():
    N=int(input())
    L=list(input())
    level=0
    tmp=0
    for l in L:
        if l =="o":
            tmp+=1
        else:
            if level<tmp:
                level=tmp
            tmp=0
    L=reversed(L)
    tmp=0
    for l in L:
        if l =="o":
            tmp+=1
        else:
            if level<tmp:
                level=tmp
            tmp=0
    if level==0:
        level=-1
    print(level)
        

if __name__=="__main__":
    main()