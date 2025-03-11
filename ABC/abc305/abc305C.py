def main():
    H, W = map(int, input().split())
    row = []
    for i in range(H):
        S = list(input())
        if not "#" in S:
            continue
        flag = []
        for j in range(W):
            if S[j] == "#":
                flag.append(j)
        index = judgeContinuous(flag)
        if index != -1:
            print(i + 1, flag[index])
            return 0
        row.append(flag)
        if i != 0:
            flag, index = find_matching_index(row[i - 1], row[i])
            if index != -1:
                if flag == 0:
                    print(i + 1, row[i - 1][index] + 1)
                else:
                    print(i, row[i][index] + 1)
                return 0


def find_matching_index(list1, list2):
    flag = 0
    if len(list1) < len(list2):
        flag += 1
        list1, list2 = list2, list1
    for i, element in enumerate(list1):
        if element not in list2:
            return flag, i

    # 一致する要素が見つからない場合は-1を返す
    return flag, -1


def judgeContinuous(s):
    for i in range(1, len(s)):
        if abs(s[i - 1] - s[i]) != 1:
            return i
    return -1


if __name__ == "__main__":
    main()
