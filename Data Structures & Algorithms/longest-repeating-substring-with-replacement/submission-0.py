class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        maxf = 0
        res = 0
        l = 0
        for i in range(len(s)):
            
            if s[i] not in mp:
                mp[s[i]] = 1
            elif s[i] in mp:
                mp[s[i]] += 1
            
            maxf = max(maxf, mp[s[i]])

            while (i - l + 1) - maxf > k:
                mp[s[l]] -= 1
                l += 1
            res =max(res, i-l+1)
        return res