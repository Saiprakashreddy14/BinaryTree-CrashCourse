# class Solution:

#     def smallestFarthest(self,arr):
#         ans =[]

#         for i in range(len(arr)):
#             mn = 9999
#             mi = -1
#             for j in range(i+1,len(arr)):
#                 if arr[j] < arr[i]:
                    
#                     mn = min(arr[i],mn)
#                     mi = max(j,i)
#             ans.append(mi)
#         return ans

# print(Solution().smallestFarthest([3,1,5,2,4]))
# print(Solution().smallestFarthest([1,2,3,4,0]))

def farthest_min(a, n):
 
    # To store minimum element
    # in the range i to n
    suffix_min = [0 for i in range(n)]
    suffix_min[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        suffix_min[i] = min(suffix_min[i + 1], a[i])
 
    for i in range(n):
        low = i + 1
        high = n - 1
        ans = -1
 
        while (low <= high):
            mid = (low + high) // 2
 
            # If current element in the suffix_min
            # is less than a[i] then move right
            if (suffix_min[mid] < a[i]):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
 
        # Print the required answer
        print(ans, end=" ")
 
 
# Driver code
a = [3, 1, 5, 2, 4]
n = len(a)
 
farthest_min(a, n)