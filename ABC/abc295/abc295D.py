import numpy as np 
import copy
def convert(true_or_false:int)->int:
    if true_or_false==0:
        return 1
    elif true_or_false==1:
        return 0
    else:
        return -1

def bin_to_int(binary:list)->int:
    tmp=0
    for i in range(len(binary)):
        tmp+=binary[i]*(2**i)
    return tmp

def combination(base:int)->int:
    if base ==0:
        return 0
    elif base==1:
        return 0
    else:
        return base*(base-1)//2

def main():
    S=list(input())
    satisfy_bin=[]
    satisfy_int={}
    for s in range(len(S)):
        if s == 0:
            tmp = [1 for _ in range(10)]
        else:
            tmp = copy.deepcopy(satisfy_bin[s-1])
        tmp[int(S[s])] = convert(tmp[int(S[s])])
        satisfy_bin.append(tmp)
        tmp_int=bin_to_int(tmp)
        if tmp_int in satisfy_int:
            satisfy_int[tmp_int]+=1
        else:
            satisfy_int[tmp_int]=1
    count=0
    for i in satisfy_int:
        count+=combination(satisfy_int[i])
        if i == 1023:
            count+=satisfy_int[i]
    print(count)
if __name__=="__main__":
    main()