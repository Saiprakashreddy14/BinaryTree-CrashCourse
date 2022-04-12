class Solution :
    def __init__(self) -> None:
        pass
    def minCoins(self,coins,target,dic):

        if target < 0 :
            return float('inf')
        
        if target == 0 :
            return 0 
        if target in dic:
            return dic[target]
        
        best = float('inf')
        for i in coins :
            best = min(best , 1+ self.minCoins(coins,target-i,dic))
        dic[target] = best
         
        return best


print(Solution().minCoins([9,6,5,1],21,{}))