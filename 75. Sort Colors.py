def sortColors(nums):
    n = len(nums)
    for i in range(n):
        index = i
        for j in range(i+1,n):
            if nums[j] < nums[index]:
                index = j
        nums[i], nums[index] = nums[index] , nums[i] 
print(sortColors([2,0,2,1,1,0]))