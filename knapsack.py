class knap:
    def __init__(self,n,w,p,c):
        self.n = n
        self.w = w
        self.p = p
        self.c = c
        self.cw = 0
        self.cp = 0
        self.bestp = 0

    def Backtrack(self,i):
        if i > n:
            self.bestp = self.cp
            return
        if self.cw + self.w[i] <= self.c: # 进入左子树
            self.cw += self.w[i]
            self.cp += self.p[i]
            self.Backtrack(i+1)
            self.cw -= self.w[i]
            self.cp -= self.p[i]
        if self.Bound(i+1) > self.bestp: # 进入右子树
            self.Backtrack(i+1)
        
    def Bound(self,i):
        # 计算上界
        t = i
        cleft = self.c - self.cw
        b = self.cp
        while t <= n and self.w[t] <= cleft:
            cleft -= self.w[t]
            b += self.p[t]
            t += 1

        if t <= n:
            b += self.p[t] * cleft / self.w[t]
        
        return b

def knapsack(n,c,p,w):
    # 依物品单位重量价值排序
    list_pw = [
        (p[i],w[i],p[i]/w[i]) for i in range(n)  
    ]
    sorted(list_pw,key=lambda pw: pw[2])
    i = 1
    sorted_p = [0 for j in range(n+1)]
    sorted_w = [0 for j in range(n+1)]
    while i <= n:
        sorted_p[i] = list_pw[i-1][0]
        sorted_w[i] = list_pw[i-1][1]
        i += 1
 

    K = knap(n,sorted_w,sorted_p,c)
    K.Backtrack(1)
    return K.bestp

if __name__ == "__main__":
    n = 4
    c = 7
    p = [9,10,7,4]
    w = [3,5,2,1]
    bestp = knapsack(n,c,p,w)
    print(bestp)