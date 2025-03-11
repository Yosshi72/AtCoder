def main():
    S = input()
    candStr = ["ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"]

    for s in candStr:
        if S == s:
            print("Yes")
            return 0
    print("No")
    
    return 0


if __name__ == "__main__":
    main()
