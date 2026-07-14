class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = []
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            sett.append(s[r])
            res = max(res,len(sett))
        return res




                    

           


        