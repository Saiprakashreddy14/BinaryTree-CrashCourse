class Solution:
    def solve(self, nums):
        prod, n = 1, len(nums)
        result = [1] * n

        
        for i in range(n):
            result[i] = prod
            print("RESULT at {} is {}".format(nums[i],result))
            prod *= nums[i]
        prod = 1
        for i in range(n - 1, -1, -1):
            result[i] *= prod
            print("RESULT at {} {} is {}".format(nums[i],prod,result))
            prod *= nums[i]
        return result

print(Solution().solve([11,2,6,3,4]))