def main():
    N=int(input())
    S=input()
    flag=False
    for s in S:
        if s =="x":
            print("No")
            return 0
        elif s=="o":
            flag=True
    if flag:
        print("Yes")
        return 0
    print("No")

if __name__=="__main__":
    main()