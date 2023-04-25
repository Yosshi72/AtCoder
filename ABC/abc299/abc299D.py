def main():
    count=0
    N=0
    right=1
    while True:
        if count==0:
            count+=1
            N=int(input())
            left=N
        index=(right+left)//2
        print("?",index)
        S_index=int(input())
        if S_index==0:
            right=index
        else:
            left=index
        if left-right<=1:
            print("!",right)
            break

if __name__=="__main__":
    main()