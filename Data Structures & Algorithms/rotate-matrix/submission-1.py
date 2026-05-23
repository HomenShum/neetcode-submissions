class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # if we assign location
        # matrix = matrix[0][0],matrix[0][1],matrix[0][2],
                #  matrix[1][0],matrix[1][1],matrix[1][2],
                #  matrix[2][0],matrix[2][1],matrix[2][2],
        # res =    matrix[2][0],matrix[1][0],matrix[0][0],
                #  matrix[2][1],matrix[1][1],matrix[0][1],
                #  matrix[2][2],matrix[1][2],matrix[0][2],
        # The first row matrix and first column matrix rotates 

        matrix.reverse()
        print(matrix)
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]