def main():
    N ,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    sellers = sorted(A)
    buyers = sorted(B)
    
    left, right = 0, max(buyers[-1], sellers[0])
    result = -1

    while left <= right:
        mid = (left + right) // 2

        sell_count = sum(1 for s in sellers if s <= mid)
        buy_count = sum(1 for b in buyers if b >= mid)
        
        if sell_count >= buy_count:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    print(result)

if __name__ == "__main__":
    main()
