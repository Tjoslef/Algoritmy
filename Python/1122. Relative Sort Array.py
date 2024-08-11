def relativeSortArray(arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        order_map = {val:index for index,val in enumerate(arr2)}
        def csorting(val):
                if val in order_map:
                        return(0,order_map[val])
                else:
                        return(1,val)
        arr1.sort(key=csorting)

        return arr1
arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
result = relativeSortArray(arr1, arr2)
print(result)
        