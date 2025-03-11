def main():
    N = int(input())
    S = input()
    flags = [False, False, False]
    for i,s in enumerate(S):
        if s == "A":
            flags[0] =True
        elif s == "B":
            flags[1] =True
        else:
            flags[2] =True
        if check(flags):
            print(i+1)
            return 0
    return 0

def check(flags):
    for flag in flags:
        if flag == False:
            return False
    return True
if __name__ == "__main__":
    main()
