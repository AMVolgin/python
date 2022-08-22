class Matrix:
    def __init__(self, my_matrix):
        self.my_matrix = [[1, 3, 5], [2, 4, 6], [3, 7, 9]]

    def printMatrix(self, my_matrix):
        for i in range(len(my_matrix)):
            for j in range(len(my_matrix[i])):
                print("{:3d}".format(my_matrix[i][j]), end="")
            print()

mm = Matrix("MY_MATRIX")
mm.printMatrix(mm.my_matrix)



