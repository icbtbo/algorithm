def BinarySearch(a,n,x):
    left = 0
    right = n-1
    while left <= right:
        middle = (left + right) // 2
        if a[middle] is x:
            i = j = middle
        if a[middle] > x:
            right = middle - 1
        else:
            left = middle + 1
    i = right
    j = left
    return i,j

def SearchTag(a,n):
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if a[middle] == middle:
            return middle
        if a[middle] > middle:
            right = middle - 1
        else:
            left = middle + 1
    
    return -1



if __name__ == "__main__":
    a =[1,2,3,5,6,7]
    i,j = BinarySearch(a,len(a),4)
    print(i,j)
    b = [-1,0,1,3,5,7]
    print(SearchTag(b,len(b)))