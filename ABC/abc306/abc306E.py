import heapq
import heapq

N, K, Q = map(int, input().split())


class AandB:
    def __init__(self, k):
        self.A = [0] * (N+1)
        self.B = [0] * (N+1)
        self.k = k

    def update(self, i, v):
        old_value = self.A[i]
        self.A[i] = v

        # Bを更新する
        if old_value in self.B:
            self.B.remove(old_value)
            heapq.heappush(self.B, v)

        else:
            min_value = self.B[0]
            if v > min_value:
                heapq.heapreplace(self.B, v)


# 使用例
ab = AandB(k=K)
for _ in range(Q):
    x,y=map(int,input().split())
    ab.update(x,y)
    print(sum(heapq.nlargest(K,ab.B)))

