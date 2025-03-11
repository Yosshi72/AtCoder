def main():
    N=int(input())
    S=list(input())
    winner=None
    num_t=0
    num_a=0
    for s in (S):
        if s=="T":
            num_t+=1
        else:
            num_a+=1
        if num_t > num_a:
            winner="T"
        elif num_t < num_a:
            winner = "A"
    print(winner)

if __name__=="__main__":
    main()