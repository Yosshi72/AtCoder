def main():
    S=input()
    flag=check(S)
    if flag:
        print("Yes")
    else:
        print("No")

def check(S:str)->bool:
    check_b=0
    check_k=[]
    for i,s in enumerate(S):
        if s=="R" or s=="K":
            check_k.append(s)
        if s=="B":
            check_b+=i%2
    if check_k[1]=="K" and check_b==1:
        return True
    return False

if __name__=="__main__":
    main()