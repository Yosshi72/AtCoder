def main():
    N,D = map(int,input().split())
    days = [0 for _ in range(D)]
    for _ in range(N):
        S = list(input())
        for i,s in enumerate(S):
            if s == "o":
                days[i] +=1
    max_days_count = count_max_consecutive(days,N)
    print(max_days_count)
    return 0

def count_max_consecutive(nums,N):
    if not nums: return 0
    max_num = N
    max_count = 0
    curr_count = 0
    for num in nums:
        if num == max_num:
            curr_count += 1
            max_count = max(max_count, curr_count)
        else:
            curr_count = 0
    return max_count

if __name__ == "__main__":
    main()
