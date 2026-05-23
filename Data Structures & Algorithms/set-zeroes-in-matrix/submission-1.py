class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])
        zero_coordinates = []
        # find 0s
        # traverse through top
        # for i in range(left, right)

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                # find 0s 
                if matrix[y][x] == 0:
                    print("0s coordinate: ", y, x)
                    zero_coordinates.append((y, x))
                    
                print(y, x)

        for y, x in zero_coordinates:
            for i in range(len(matrix[0])):
                matrix[y][i] = 0
            for i in range(len(matrix)):
                matrix[i][x] = 0
        
        print(matrix)