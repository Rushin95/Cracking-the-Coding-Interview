# determine if a string has all unique characters

def is_unique(input):
    # check if the character is present in the remaining string
    for idx,value in enumerate(input):
        if value in input[idx+1:]:
            return False
    return True

def main():
    my_str_1 = 'abcd'
    my_str_2 = 'abca'
    print 'result of 1:', is_unique(my_str_1)
    print 'result of 2:', is_unique(my_str_2)

main()
