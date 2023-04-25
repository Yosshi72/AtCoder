def main():
    a,b=map(int,input().split())
    count=subtractions((a,b),0)
    print(count)
    
def subtractions(a:tuple,count:int):
    if a[0]>a[1]:
        return subtractions((a[0]-a[1],a[1]),count+1)
    elif a[0]<a[1]:
        return subtractions((a[0],a[1]-a[0]),count+1)
    else:
        return count

if __name__=="__main__":
    main()