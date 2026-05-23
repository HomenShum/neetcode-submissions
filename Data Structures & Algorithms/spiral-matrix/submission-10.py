class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 1, 2, 3, 4, 5
        # 6, 7, 8, 9, 10
        # 11, 12, 13, 14, 15
        # start with left top 
        # rule 1: until the end, go down in column
        # rule 2: until the end, go left in row 
        # rule 3: until the end, go up in column
        # We are constantly rotating the plane 
        # however, when we face a previously recognized value
        # that's when we shift back to the rule 1
        new_list = []

        # define the four corners
        top = 0
        bottom = len(matrix) -1
        left = 0
        right = len(matrix[0]) -1

        while top <= bottom and left <= right:
            print(top, bottom, left, right)
            for i in range(left, right + 1):
                print("top", i)
                new_list.append(matrix[top][i])
            top += 1

            for i in range(top, bottom +1):
                print("right", i)
                new_list.append(matrix[i][right])
            right -= 1

            if top <= bottom: 
                print(left, right)
                for i in range(right, left-1, -1):
                    print("bot", i)
                    new_list.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                print("run", bottom, top-1)
                for i in range(bottom, top-1, -1):
                    print("left", i)
                    new_list.append(matrix[i][left])
                left += 1

        
        print(new_list)

        return(new_list)