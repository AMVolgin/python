class Matrix:
    def __init__(self, my_matrix1):
        self.my_matrix1 = [[1, 3, 5], [2, 4, 6], [3, 7, 9]]
        self.my_matrix2 = [[11, 13, 15], [12, 14, 16], [13, 17, 19]]


    def printMatrix(self, my_matrix1):
        for i in range(len(my_matrix1)):
            for j in range(len(my_matrix1[i])):
                print("{:3d}".format(my_matrix1[i][j]), end="")
            print()

    def __str__(self, my_matrix1):
            pass

    def __add__(self, my_matrix1, my_matrix2):
            pass

    def resultMatrix(self, my_matrix1, my_matrix2):
        i = 0
        j = 0
        x = 0
        res_matrix = []
        res_matrix= [[my_matrix1[i][j] + my_matrix2[i][j] for j in range
        (len(my_matrix1[0]))] for i in range(len(my_matrix1))]

        for r in res_matrix:
            print(r)


mm = Matrix("MY_MATRIX")
mm.printMatrix(mm.my_matrix1)
print(mm.my_matrix1)
mm.resultMatrix(mm.my_matrix1, mm.my_matrix2)



