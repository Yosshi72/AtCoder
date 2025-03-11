def main():
    S=list(input())
    N=int(input())
    tmp_S=0
    for i,s in enumerate(S):
        if s!="?":
            tmp_S+=int(s)*(2**(len(S)-i-1))
    N-=tmp_S
    for i,s in enumerate(S):
        if s == "?":
            bin_i=2**(len(S)-i-1)
            if bin_i<=N:
                N-=bin_i
                tmp_S+=bin_i
                S[i]="1"
            else:
                S[i]="0"
    if N<0:
        print("-1")
    else:
      print(tmp_S)
if __name__=="__main__":
    main()