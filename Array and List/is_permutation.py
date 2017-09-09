# determine if strings are permutation of eachother

def is_permutation(input_1, input_2):
    if sorted(input_1) == sorted(input_2):
        return True
    return False

def main():
    my_str_1 = '   aabc'
    my_str_2 = 'caab'
    my_str_3 = 'abAc   '
    print 'result of 1:', is_permutation(my_str_1, my_str_2)
    print 'result of 2:', is_permutation(my_str_1, my_str_3)

main()
