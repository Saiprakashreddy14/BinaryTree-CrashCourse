import heapq

class Solution:
    
    def sol1(self,arr,k):
        print("Ans is : ")
        return sorted(arr,reverse=True)[:k]


    def sol2(self,arr,k):
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j]<arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr[:k]


    def sol3(self,arr,k):
        arr = [-i for i in arr]
        heapq.heapify(arr)
        ans = []
        for i in range(k):
            ans.append((-1*heapq.heappop(arr)))
        return ans


print(Solution().sol1([23332,3,665,676,9090,22,323,42343446,45,6463443],4))
print(Solution().sol2([23332,3,665,676,9090,22,323,42343446,45,6463443],4))
print(Solution().sol3([23332,3,665,676,9090,22,323,42343446,45,6463443],4))