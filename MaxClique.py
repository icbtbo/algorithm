class Clique:
    def __init__(self,a,n):
        self.a = a # 图的邻接矩阵
        self.n = n # 图的顶点数
        self.x =[0 for i in range(n+1)] # 当前解
        self.bestx =[0 for i in range(n+1)] # 当前最优解
        self.cn = 0 # 当前顶点数
        self.bestn = 0# 当前最大顶点数

    def Backtrack(self,i):
        # 计算最大团
        if i > n:
            j = 1
            while j <= n:
                self.bestx[j] = self.x[j]
                j += 1
            self.bestn = self.cn
            return
        # 检查顶点i与当前团的连接
        OK = 1
        j = 1
        while j < i:
            if self.x[j] and self.a[i][j] == 0:
                # i 与 j不相连
                OK = 0
                break
            j += 1
        if OK:
            self.x[i] = 1
            self.cn += 1
            self.Backtrack(i+1)
            self.x[i] = 0
            self.cn -= 1
        if self.cn + self.n - i > self.bestn:
            self.x[i] = 0
            self.Backtrack(i+1)


def MaxClique(a,n):
    C = Clique(a,n)
    C.Backtrack(1)
    return C.bestn,C.bestx

if __name__ == "__main__":
    a = [
        [],
        [0,0,1,0,1,1],
        [0,1,0,1,0,1],
        [0,0,1,0,0,1],
        [0,1,0,0,0,1],
        [0,1,1,1,1,0]
    ]
    n = 5
    print(MaxClique(a,n))