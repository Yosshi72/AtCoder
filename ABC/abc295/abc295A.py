def main():
    N=int(input())
    W=list(input().split())
    for w in W:
        if w=="and" or w=="not" or w=="that" or w=="the" or w=="you":
            print("Yes")
            return 0
    print("No")


if __name__=="__main__":
    main()