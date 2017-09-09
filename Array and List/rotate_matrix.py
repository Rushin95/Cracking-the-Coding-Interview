# rotate n*n matrix by 90 degree

def print_matrix(input_list):
    for row in input_list:
        print row

def rotate_matrix(input_matrix):
    print 'old:'
    print_matrix(input_matrix)
    n = len(input_matrix)
    l = []
    for j in range(n):
        temp = []
        for i in range(n-1,-1,-1):
            temp.append(input_matrix[i][j])
        l.append(temp)
    print 'new:'
    print_matrix(l)

def main():
    matrix = [[1,1,1],[1,0,1],[1,0,1]]
    rotate_matrix(matrix)

main()
