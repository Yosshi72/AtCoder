import numpy as np 
def manhattan(bomb:list,wall:list)->int:
    p_b=np.array([bomb[0],bomb[1]])
    p_w=np.array(wall)
    d=int(np.linalg.norm(p_b - p_w, ord=1))
    return d

def main():
    R,C = map(int,input().split())
    wall=[]
    bomb=[]
    B=[]
    for r in range(R):
        b_row=list(input())
        B.append(b_row)
        for c in range(C):
            if b_row[c]=="#":
                wall.append([r,c])
            elif b_row[c]!=".":
                bomb.append([r,c,int(b_row[c])])
    for w in wall:
        for b in bomb:
            d=manhattan(b,w)
            B[b[0]][b[1]]="."
            if d<=b[2]:
                B[w[0]][w[1]]="."
                continue
    for l in B:
        print(''.join(l))
                


if __name__=="__main__":
    main()