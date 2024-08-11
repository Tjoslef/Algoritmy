from bisect import bisect_left, bisect_right
def waysToSplit(nums):
    n = len(nums)
    if n < 3:
        return 0
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]

    count = 0


    for i in range(1, n - 1):
        if prefix_sums[i] * 3 > prefix_sums[n]:
            break

        left = bisect_left(prefix_sums, 2 * prefix_sums[i], i + 1, n)

   
        right = bisect_right(prefix_sums, (prefix_sums[n] + prefix_sums[i]) // 2, i + 1, n)
        if left < right:
            count += right - left

    return count
print(waysToSplit([0,0,0,0,0,0,0,0,0,0,0,0]))
