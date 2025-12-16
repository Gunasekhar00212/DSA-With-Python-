def prefix_array(arr,n):
    prefix=[0]*n
    prefix[0]=arr[0]
    for i in range(1,n):
        prefix[i]=prefix[i-1]+arr[i]
    return prefix
def subarray_sum(prefix,l,r):
    if l==0:
        return prefix[r]
    else:
        return prefix[r]-prefix[l-1]

arr=[1,2,3,4]
n=len(arr)
prefix=prefix_array(arr,n)
result=subarray_sum(prefix,2,3)
print(result)  # Output: 7 (sum of elements from index 2 to 3)