def main():
    N=int(input())
    Q=int(input())
    box=[[] for _ in range(N+1)]
    card={}
    for _ in range(Q):
        query=list(map(int,input().split()))
        if query[0]==1:
            box[query[2]].append(query[1])
            if query[1] not in card.keys():
                card[query[1]]=[query[2]]
            else:
                if query[2] not in card[query[1]]:
                    card[query[1]].append(query[2]) 
        elif query[0]==2:
            print(*sorted(box[query[1]]))
        elif query[0]==3:
            print(*sorted(card[query[1]]))
    return 0

if __name__=="__main__":
    main()