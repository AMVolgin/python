class Matrix:
    def __init__(self, my_matrix1):
        pass


    def __str__(self, my_matrix1):
        print(f"{my_matrix1}")

    def show_matrix(self, my_matrix1):
        for i in range(len(my_matrix1)):
            for j in range(len(my_matrix1[i])):
                print("{:3d}".format(my_matrix1[i][j]), end="")

    def __add__(self, my_matrix1, my_matrix2):

        i = 0
        j = 0
        x = 0
        res_matrix = []
        res_matrix = [[my_matrix1[i][j] + my_matrix2[i][j] for j in range
        (len(my_matrix1[0]))] for i in range(len(my_matrix1))]

        for r in res_matrix:
            print(r)


mm = Matrix("MY_MATRIX")
mm1 = [[1, 3, 5], [2, 4, 6], [3, 7, 9]]
mm2 = [[11, 13, 15], [12, 14, 16], [13, 17, 19]]
mm.__str__(mm1)
mm.show_matrix(mm1)
print("\n")
mm.__add__(mm1, mm2)
//ggg
