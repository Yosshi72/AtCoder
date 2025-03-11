import math

def main():
    N=int(input())
    if is_prime(N):
        print(0)
        return 0
    primes=prime_factorize(N)
    L=len(primes)-1
    print(len(bin(L))-2)
    
def is_prime(N):
    if N==0 or N==1:
        return False
    for i in range(2,int(math.sqrt(N))+1):
        if N%i==0:
            return False
    return True

def prime_factorize(N:int) -> list:
    prime_list=[]
    for i in range(2,N):
        while (N%i==0):
            prime_list.append(i)
            N/=i
    return prime_list

if __name__=="__main__":
    main()
