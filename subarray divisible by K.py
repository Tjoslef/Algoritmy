def subarraysDivByK(nums, k):
        count = 0
        cumulative_sum = 0
        sum_dict = {0: 1}
        for num in nums:
            cumulative_sum += num
            if(cumulative_sum -k) in sum_dict:
                  count += sum_dict[cumulative_sum - k]
            if cumulative_sum in sum_dict:
                sum_dict[cumulative_sum] += 1
            else:  
                sum_dict[cumulative_sum] = 1
        return count
print(subarraysDivByK([1,1,1],2))