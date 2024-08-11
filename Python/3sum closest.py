def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = 0   
    min_diff = 0  

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        seen = set()
        j = i + 1
        while j < len(nums):
            other = - nums[i] - nums[j]
            if other in seen:
                triplet_sum = nums[i] + nums[j] + other
                diff = abs(triplet_sum - target)
                if diff < min_diff:
                    closest_sum = diff
                    min_diff = diff
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1
    result = closest_sum
    return closest_sum
nums = [-1, 2, 1, -4]
target = 1
result = threeSumClosest(nums, target)
print(result)
    
        

        
