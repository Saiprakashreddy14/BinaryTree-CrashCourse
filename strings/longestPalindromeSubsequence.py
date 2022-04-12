class Solution:
    def minInsertions(self,a):
        return len(a) - self.lps(a)

    def lps(self,a) :

        dp = {} 
        # dp[(m,n)]= 232

        def lcs(a,b,m,n):

            if (m,n) in dp :
                return dp[(m,n)]

            if m==0 or n==0 :
                return 0
            if a[m-1]==b[n-1]:
                ans =  1 + lcs(a,b,m-1,n-1)
            else:
                ans = max(lcs(a,b,m-1,n),lcs(a,b,m,n-1))

            dp[(m,n)] = ans

            return ans
            
        return lcs(a,a[::-1],len(a),len(a))


        
        
print(Solution().minInsertions("leetcode"))
