def main():
    N, M, H, K = map(int, input().split())
    S = input()
    c_p = [0, 0]
    item_p = {}
    for _ in range(M):
        item_p[input()] = True
    for n in range(N):
        c_p = move(c_p,S[n])
        H -= 1
        
        if H < 0:
            print("No")
            return 
        
        if H < K:
            if item_p.get(f"{c_p[0]} {c_p[1]}"):
                H = K
                item_p.pop(f"{c_p[0]} {c_p[1]}")
    print("Yes")

def move(c_p, command):
    n_px = c_p[0]
    n_py = c_p[1]
    if command == "R":
        n_px += 1
    elif command == "L":
        n_px -= 1
    elif command == "U":
        n_py += 1
    else:
        n_py -= 1
    return [n_px, n_py]


if __name__ == "__main__":
    main()
