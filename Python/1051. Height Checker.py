def heightChecker(heights):
    count = 0
    if len(heights) < 1:
        return 0
    correctO = sorted(heights)
    for i in range(len(heights)):
        if correctO[i] != heights[i]:
            count +=1 
    return count
print(heightChecker([1,1,4,2,1,3]))
