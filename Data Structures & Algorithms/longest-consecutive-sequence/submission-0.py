class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # 2, 3, 4, 5, 10, 20
        longest = 0

        for num in numSet:
            print(num)
            if (num - 1) not in numSet: # finding the leading number of the LCS == 2
                length = 1 # count first
                while (num + length) in numSet: # go through the while loop for as long as curr num + length is still in the set
                    length += 1 
                    # 2 + 1 == 3 length = 1
                    # 2 + 2 == 4 length = 2
                    # 2 + 3 == 5 length = 3
                    # length = 4
                longest = max(length, longest)
        return longest
