class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if s == '':
        #     return 0
        # # keep track of the count and the previous char
        # count = 0
        # track = []
        # potentials = 0
        # large_count = 0
        # large_track = []
        # for char in s:
        #     if count > 0:
        #         if char is s[count-1]:
        #             potentials = max(potentials, count)
        #             count = 0
        #             track = []
        #         if char in track:
        #             potentials = max(potentials, len(track))
        #             count = 0
        #             track = []
        #         if char not in large_track:
        #             large_track.append(char)
        #             print(char, large_track)         
        #             large_count += 1
        #             print(large_count)
        #             potentials = max(potentials,large_count)
        #     track.append(char)
        #     count += 1
        #     print(char, count)
        #     potentials = max(potentials, count)
        
        # return potentials

        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res