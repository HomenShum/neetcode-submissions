class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        if t.lower() == s.lower(): 
            return t
        if t == "":
            return ""
        from collections import Counter
        window_counts = Counter()
        target_counts = Counter(t)
        matches = 0
        l = r = 0
        res, res_len = "", float("inf")

        while r < len(s):
            window_counts[s[r]] += 1

            if window_counts[s[r]] == target_counts[s[r]]:
                matches += 1
            
            while matches == len(target_counts):
                if (r - l + 1) < res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                
                if window_counts[s[l]] == target_counts[s[l]]:
                    matches -= 1

                window_counts[s[l]] -= 1
                l += 1
            
            r += 1

        return res
