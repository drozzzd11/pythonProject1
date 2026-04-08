matrix = [[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[1, 1, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0],[0, 0, 1, 0, 0, 0] ]
for x in range(1000):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (( i == 3 and (j == 0 or j == 1)) or (( i==4 or i ==5) and (j == 2)) or (j<2 and i>3)):
                        matrix[i][j] = 1
            elif (j - i == 2 or i == 0 or j == 5):
                matrix[i][j] == 0
            else:
                if (j > 0 and i < 5):
                    matrix[i][j] = 0.25 * ( matrix[i- 1][j] + matrix[i+1][j] + matrix[i][j+1] + matrix[i][j-1])
                elif ( i == 5):
                    matrix[i][j] = 0.25 *( 2 * matrix[i- 1][j] + matrix[i][j - 1] + matrix[i][j+1])
                elif (j == 0):
                    matrix[i][j] = 0.25 *(matrix[i- 1][j] + matrix[i+1][j] + 2* matrix[i][j+1])
for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(round(float(matrix[i][j]), 2), end = ' ')
        print("\n")
