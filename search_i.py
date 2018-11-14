def Partition(a, p, r):
    x = a[p]
    i = p + 1
    j = r
    while True:
        while a[i] < x and i < r:
            i += 1
        while a[j] > x:
            j -= 1
        if i >= j:
            break
        a[i],a[j] = a[j],a[i]
    a[p] = a[j]
    a[j] = x
    return j

def Select(a,p,r,i):
    if p == r:
        return a[p]
    q = Partition(a,p,r)
    k = q - p + 1
    if i == k:
        return a[q]
    elif i < k:
        return Select(a,p,q-1,i)
    else:
        return Select(a,q+1,r,i-k)


if __name__ == "__main__":
    a = [4,7,1,5,6,9,2]
    print(Select(a,0,len(a)-1,3))