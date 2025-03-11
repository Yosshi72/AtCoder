import copy 

def main():
    N, M =map(int,input().split())
    S = list(input())
    C = list(map(int,input().split()))

    colorS = {}

    for i, c in enumerate(C):
        if c not in colorS:
            colorS[c] = []
        colorS[c].append(i)
    
    for values in colorS.values():
        values = sorted(values, reverse = True)
        for i in range(len(values)-1):
            S[values[i]], S[values[i+1]] = S[values[i+1]], S[values[i]]
        # S[values[len(values)-1]] = tmp
    print(*S, sep ="")
    return 0

if __name__ == "__main__":
    main()
