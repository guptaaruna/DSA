def sortColors(nums):
    ind1=0
    ind2=0
    ind3=len(nums)-1
    while ind2<=ind3:
        if nums[ind2]==0:
            (nums[ind1],nums[ind2])=(nums[ind2],nums[ind1])
            ind1+=1
            ind2+=1
        elif nums[ind2]==1:
            ind2+=1
        elif nums[ind2]==2:
            (nums[ind2],nums[ind3])=(nums[ind3],nums[ind2])
            ind3-=1
                
    return nums


nums=[2,0,2,1,1,0]
print(sortColors(nums))