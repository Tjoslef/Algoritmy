from collections import Counter
def threeSum(nums):
    nums.sort()
    result = set()
    if len(nums) < 3:
         return []
    for i in range(len(nums)-2):
         if i > 0 and nums[i] == nums[i-1]:
              continue
         seen = set()
         j = i +1
         while j< len(nums):
              complement = -nums[i] - nums[j]
              if complement in seen:
                result.add(nums[i],nums[j],complement)
                while j +1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
              seen.add(nums[j])
              j += 1
    return list(result)     
print(threeSum([-1,2,1,-4]))               
    