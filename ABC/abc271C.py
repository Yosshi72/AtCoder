def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    a = sorted(a)
    key = 1
    while True:
        if len(a)==0:
            break
        if a[0] == key:
            count += 1
            key += 1
            a.pop(0)
        else:
            if len(a)<2:
                break
            count+=1
            key+=1
            a.pop(len(a)-1)
            a.pop(len(a)-2)
    print(count)

        

if __name__ == "__main__":
    main()
