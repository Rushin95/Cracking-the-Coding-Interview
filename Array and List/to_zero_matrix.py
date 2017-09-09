
def put_zeros(input_matrix):
    print 'old:'
    print_matrix(input_matrix)
    new_matrix = input_matrix
    for i,row in enumerate(input_matrix):
        for j,value in enumerate(row):
            if value == 0:
                input_matrix[0][j] = 0
                input_matrix[i][0] = 0

    # nullify rows
    for


    print 'new:'
    print_matrix(input_matrix)




def print_matrix(input_list):
    for row in input_list:
        print row

def main():
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    put_zeros(matrix)

main()
