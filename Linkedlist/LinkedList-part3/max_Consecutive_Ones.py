def findMaxConsecutiveOnes(nums):
    dic={}
    dic[0]=0
    dic[1]=0
    maxi=0
    for i in nums:
        if i==1:
            dic[1]+=1
        else:
            if maxi<dic[1]:
                maxi=dic[1]
            dic[1]=0
    if maxi<dic[1]:
        maxi=dic[1]
    return(maxi)