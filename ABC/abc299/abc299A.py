def main():
    N=int(input())
    S=list(input())
    flag=0
    for s in S:
        if s=="*" :
            if flag==1:
                print("in")
                break
            else:
                print("out")
                break
        if s=="|":
            if flag==0:
                flag=1
            else:
                flag=0
    return 0
        

if __name__=="__main__":
    main()