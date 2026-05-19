class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 0:
            # mirrors, evens only, palindrome alike
            vp1 = '[]'
            vp2 = '()'
            vp3 = '{}'

            for i in range(len(s) // 2):
                if vp1 in s:
                    s = s.replace(vp1, "")
                elif vp2 in s:
                    s = s.replace(vp2, "")            
                elif vp3 in s:    
                    s = s.replace(vp3, "")
                else:
                    return False
            print(s)
            if len(s) == 0:
                return True
        return False