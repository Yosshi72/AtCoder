def main():
    S=[]
    for _ in range(8):
        S.append(list(input()))
    col=["a","b","c","d","e","f","g","h"]
    row=["8","7","6","5","4","3","2","1"]
    for r in range(8):
        for c in range(8):
            if S[r][c]=="*":
                print(col[c]+row[r])
                return 0
if __name__=="__main__":
    main()