def main():
    N=int(input())
    is_True=eratosthenes(int(N**(0.2))+1)
    count=0
    for a in range(int(N**(0.2))):
        if not is_True[a]:
            continue
        
        
def eratosthenes(n):
    is_prime = [False, False] + [True] * (n-1)
    for p in range(2, n+1):
        if not(is_prime[p]):
            continue
        for k in range(p*2, n+1, p):
            is_prime[k] = False
    return is_prime

if __name__=="__main__":
    main()