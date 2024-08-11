def checkSubarraySum(nums, k):
    if len(nums) < 2:
        return False
    
    Dstory = {0: -1}
    csum = 0
    Zcount = 0
    
    for i in range(len(nums)):
        if nums[i] == 0:
            Zcount += 1
        else:
            Zcount = 0  # reset count if the current number is not zero
        
        if Zcount >= 2:
            return True
        
        csum += nums[i]
        
        if k != 0:
            remaider = csum % k
        else:
            remaider = csum
        
        if remaider in Dstory:
            if i - Dstory[remaider] > 1:
                return True
        else:
            Dstory[remaider] = i
    
    return False
print(checkSubarraySum([5,0,0,0],3))

            
            
                