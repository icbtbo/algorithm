def q(n,m):
    if n < 1 or m < 1:
        return 0
    if n is 1 or m is 1:
        return 1
    if n < m:
        return q(n,n)
    if n is m:
        return 1 + q(n,n-1)
    if n > m:
        return q(n,m-1) + q(n-m,m)

mark = [] # 记录要输出的数据
def divide(now,k,pre,n):
    global mark
    if now > n:
        return
    if now == n:
        tempstr = str(n)+"="
        for i in range(k-1):
            tempstr += str(mark[i]) + "+"
        tempstr += str(mark[k-1])
        print(tempstr)
    else:
        for i in range(pre):
            num = pre - i
            if num <= pre:
                mark[k] = num
                now += num
                divide(now,k+1,num,n)
                now -= num


if __name__ == "__main__":
    n = int(input("请输入要划分的整数:"))
    # n = int(n)
    print("正整数" + str(n) + "的划分个数：",q(n,n))
    print("======================================")
    mark = [0 for i in range(n)]
    divide(0,0,n,n)
