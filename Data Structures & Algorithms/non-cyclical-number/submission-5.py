class Solution:
    def isHappy(self, n: int) -> bool:
        # sum of the squares of its digits
        string_n = str(n)
        sum_val = 0
        for i in string_n:
            # print(int(i)**2)
            sum_val += int(i)**2
        print(sum_val)

        seen_list = [sum_val]

        while sum_val != 1:
            new_sum_val = 0
            for i in str(sum_val):
                new_sum_val += int(i)**2
            print(new_sum_val)            
            if new_sum_val in seen_list:
                break
            seen_list.append(new_sum_val)
            sum_val = new_sum_val
        


        return sum_val == 1