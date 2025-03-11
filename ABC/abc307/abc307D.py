def main():
    N = int(input())
    S = input()
    heads = []
    tuples = []
    originTuple = []
    for i in range(N):
        if S[i] == "(":
            heads.append(i)
        elif S[i] == ")":
            if len(heads) != 0:
                if len(heads) == 1:
                    originTuple.append((heads.pop(-1), i))
                    tuples = []
                else:
                    tuples.append((heads.pop(-1), i))
    originTuple += tuples
    index = 0
    returnS = ""
    for tuple in originTuple:
        returnS += S[index : tuple[0]]
        index = tuple[1] + 1
    returnS += S[index : len(S)]
    print(returnS)
    return 0


if __name__ == "__main__":
    main()
