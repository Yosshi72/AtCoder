def main():
    H,W = map(int,input().split())
    A = []
    for i in range(H):
        row = list(input().split())
        for j in row:
            if j == "0":
                print(".",end="")
            else:
                print(chr(int(j)+64),end="")
        print()


if __name__ == "__main__":
    main()
