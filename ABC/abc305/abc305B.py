def main():
    dist = [3, 1, 4, 1, 5, 9]
    p,q=input().split()
    start = min(p,q)
    end = max(p,q)
    distPQ=0
    for i in range(returnIndex(start),returnIndex(end)):
        distPQ += dist[i]
    print(distPQ)

def returnIndex(alphabet):
    shift = ord("A")
    index = ord(alphabet) - shift
    return index


if __name__ == "__main__":
    main()
