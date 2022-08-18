def nextPermutation(nums):
    n=len(nums)
    for i in range(n-1,0,-1):
        if nums[i-1]<nums[i]:
            lis=nums[i:]
            l1=lis.copy()
            l1.sort()
            for k in l1:
                if k>nums[i-1]:
                    jus_gr=k
                    break
            ind=lis.index(jus_gr)+i
            (nums[i-1],nums[ind])=(nums[ind],nums[i-1])
            lis2=nums[i:]
            lis2.sort()
            m=0
            for k in range(i,n):
                nums[k]=lis2[m]
                m+=1
            return(nums)
    nums.sort()
    return(nums)


nums=[5,4,2,6,1]
print(nextPermutation(nums))
                