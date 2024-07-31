def maximum_gap(nums):
    if len(nums) < 2:
        return 0
    
    n = len(nums)
    maxVal = max(nums)
    exp = 1
    aux = [0] * n
    
    while maxVal // exp > 0:
        count = [0] * 10
        
        # Counting the number of occurrences of each digit
        for i in range(n):
            count[(nums[i] // exp) % 10] += 1
        
        # Transform count into the positions in the auxiliary array
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        # Building the auxiliary array
        for i in range(n - 1, -1, -1):
            index = (nums[i] // exp) % 10
            aux[count[index] - 1] = nums[i]
            count[index] -= 1
        
        # Copying the sorted elements back to nums
        for i in range(n):
            nums[i] = aux[i]
        
        exp *= 10
    
    # Calculating the maximum gap
    max_gap = 0
    for i in range(1, n):
        max_gap = max(max_gap, nums[i] - nums[i - 1])
    
    return max_gap

# Example usage
nums = [3,6,9,1]
print(maximum_gap(nums))  # Expected output: 9999999

    
    
