def prefix_array(arr,n):
    prefix=[0]*n
    prefix[0]=arr[0]
    for i in range(1,n):
        prefix[i]=prefix[i-1]+arr[i]
    return prefix
arr=[1,2,3,4]
print(prefix_array(arr,len(arr)))