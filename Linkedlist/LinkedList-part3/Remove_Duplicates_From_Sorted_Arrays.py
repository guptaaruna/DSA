def removeDuplicates(nums):     
    dic={}
    l=len(nums)
    k=0
    i=0
    while(i<l):
        if nums[i] not in dic.keys():
            dic[nums[i]]=k
                
            i+=1
        else:
            k+=1
            nums.remove(nums[i])
            nums.append(0)
    print(nums)
    for i in range(k):
        nums.remove(nums[-1])
    return