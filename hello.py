
# should determine the order of the sums of the rows
# then use that order to sort the order of the original matrix
# perhaps simultaneously

def sort_some_stuff(square_matrix):
    print(square_matrix)

    n = len(square_matrix[0])

    row_sums = [0]*5
    for i in range(n):
        for j in range(n):
          print(square_matrix[i][j], end=" ")        
          row_sums[i] += square_matrix[i][j] 
        print(f" = {row_sums[i]}")

    print("row sums = ", row_sums)

    # sort
    # depends on n > 1, but then so does sorting anything
    for i in range(n):
        for j in range(i):
            if row_sums[i] < row_sums[j]:
                row_sums[i], row_sums[j] = row_sums[j], row_sums[i]
                for k in range(n):
                    square_matrix[i][k], square_matrix[j][k] = square_matrix[j][k], square_matrix[i][k]

    print("-- sorted row sums = ", row_sums)
    for i in range(n):
        for j in range(n):
          print(square_matrix[i][j], end=" ")        
        print(f" = {row_sums[i]}")
   

if __name__=="__main__":
    print("---- atmosphere ----")
 
    # row first manipulation
    a = [[1,2,3,4,5], [15,4,3,2,1], [4,3,7,6,9], [7,4,3,9,2], [2,9,5,3,1]]

    sort_some_stuff(a)
    print("---- one nation under a groove ----")