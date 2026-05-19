class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = "".join(char for char in s if char.isalnum()).lower()
        
        s_cleaned_reverse = ""
        for i in range(len(s_cleaned)-1, -1, -1):
            s_cleaned_reverse += s_cleaned[i]

        return s_cleaned_reverse == s_cleaned