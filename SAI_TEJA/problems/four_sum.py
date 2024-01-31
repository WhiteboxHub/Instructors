def foursum(nums,target):
    nums.sort()
    result = []
    for i in range(len(nums)-3):
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,len(nums)-2):
            if j>i+1 and nums[j] == nums[j-1]:
                continue
            left,right = j+1,len(nums)-1
            while left<right:
                current_sum = nums[i]+nums[j]+nums[left]+nums[right]
                if current_sum == target:
                    result.append([nums[i],nums[j],nums[left],nums[right]])
                    
                    while left<right and nums[left] == nums[left+1]:
                        left +=1
                    while left<right and nums[right] == nums[right-1]:
                        right -=1

                    left+=1
                    right-=1
                elif current_sum<target:
                    left+=1
                else:
                    right-=1
    return result


nums=[1,0,-1,0,2,-2]
target = 0
result = foursum(nums,target)
print(result)