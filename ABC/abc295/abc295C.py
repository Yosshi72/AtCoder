def main():
    N=int(input())
    A=list(input().split())
    
    dict={}
    for n in range(N):
        if A[n] in dict.keys():
            dict[A[n]]+=1
        else:
            dict[A[n]]=1
    
    count=0
    for key in dict:
        count += int(dict[key]/2)
    print(count)



if __name__=="__main__":
    main()