def maxSubArray(arr):
    length=len(arr)
    ms=arr[0]
    me=arr[0]
    for i in range(1,length):
        me+=arr[i]
        if arr[i]>me:
            me=arr[i]
        if me>ms:
            ms=me
    return ms

nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))