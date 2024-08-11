import numpy as np
def part(n):
        def format(n):
            a = [0 for i in range(n + 1)]
            k = 1
            y = n - 1
            while k != 0:
                x = a[k - 1] + 1
                k -= 1
                while 2 * x <= y:
                    a[k] = x
                    y -= x
                    k += 1
                l = k + 1
                while x <= y:
                    a[k] = x
                    a[l] = y
                    yield a[:k + 2]
                    x += 1
                    y -= 1
                a[k] = x + y
                y = x + y - 1
                yield a[:k + 1]
        partitions = list(format(n))
        partition_products = [np.prod(partition) for partition in partitions]
        unique_partition_products = sorted(set(partition_products))
        Range = np.max(unique_partition_products) - np.min(unique_partition_products)
        avg = np.mean(unique_partition_products)
        median = np.median(unique_partition_products)
        return f"Range: {Range} Average: {avg:.2f} Median: {median:.2f}"

print(part(5))    

