def maximum_gap(nums):
    if len(nums) < 2:
        return 0
    
    n = len(nums)
    maxVal = max(nums)
    exp = 1
    aux = [0] * n
    
    while maxVal // exp > 0:
        count = [0] * 10
        
        
        for i in range(n):
            count[(nums[i] // exp) % 10] += 1
        
        
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        
        for i in range(n - 1, -1, -1):
            index = (nums[i] // exp) % 10
            aux[count[index] - 1] = nums[i]
            count[index] -= 1
        
        
        for i in range(n):
            nums[i] = aux[i]
        
        exp *= 10
    
    
    max_gap = 0
    for i in range(1, n):
        max_gap = max(max_gap, nums[i] - nums[i - 1])
    
    return max_gap

nums = [3,6,9,1]
print(maximum_gap(nums))  

    
    
