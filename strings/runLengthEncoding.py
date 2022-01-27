class Solution :
    def runLengthEncode(self,s):
        if not s:
            return s
        
        buf = s[0]
        ans = ""
        cnt = 1
        for i in s[1:]:
            if i==buf:
                cnt+=1
            else:
                ans+=(buf+str(cnt))
                cnt=1
                buf = i
        ans += (buf+str(cnt))
        return ans

print(Solution().runLengthEncode("abbbcdddd"))