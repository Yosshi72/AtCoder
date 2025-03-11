def main():
    N,K=map(int,input().split())
    
    for k in range(K):
        N=base8_to_9(N)
    print(N)

def base8_to_9(N:int)->int:
    base10=base8_to_10(N)
    base9=int(base10_to_9(base10))
    return base9

def base8_to_10(N:int)->int:
    base10=0
    for i in reversed(range(len(str(N)))):
        base10+=(N//(10**i))*8**i
        N%=10**i
    return base10

def base10_to_9(N:int)->str:
    remain=str(N%9)
    if remain=="8":
        remain="5"
    if N/9>0:
        return base10_to_9(N//9)+remain
    return remain

if __name__=="__main__":
    main()

