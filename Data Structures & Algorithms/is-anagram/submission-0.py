class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if same number of characters on both string then anagram is true
        # can we order a string
        if sorted(s) == sorted(t):
            return True
        return False