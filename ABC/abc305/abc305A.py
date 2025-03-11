def main():
    N = int(input())
    restPoint = (N//5)*5 if N-(N//5)*5 < (N//5+1)*5 -N else (N//5+1)*5
    print(restPoint)

if __name__ == "__main__":
    main()
