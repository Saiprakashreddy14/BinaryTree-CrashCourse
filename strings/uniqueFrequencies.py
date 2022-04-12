class Solution:
    def solve(self, s):
        ans = 0
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        dkeys = sorted(d,key=d.get)[::-1]
        for i in dkeys:
            if d[]
        print(d)


print(Solution().solve("abbccc"))