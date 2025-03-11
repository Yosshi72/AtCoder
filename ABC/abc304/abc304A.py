def main():
    N = int(input())
    name = []
    age = []
    for _ in range(N):
        info=list(input().split())
        name.append(info[0])
        age.append(int(info[1]))
    index = age.index(min(age))
    name = name[index:] + name[:index]
    for n in name:
        print(n)
if __name__=="__main__":
    main()