class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        for i in digits:
            string+=str(i)
        res = int(string) + 1
        res_list = []
        for i in str(res):
            res_list.append(i)
        return res_list