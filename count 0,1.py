def suy(arr,n):
    count0=0
    count1=0
    for i in range(0,n):
        if(arr[i]==0):
            count0=count0+1
        else:
            count1=count1+1
arr = [ 0, 1, 0, 1, 1, 1 ]
n = len(arr)
suy(arr, n)
