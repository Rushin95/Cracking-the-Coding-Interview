# replace white space with '%20'

def return_url(input_str):
    # Method 1
    input_list = list(input_str)
    for idx,char in enumerate(input_list):
        if char == ' ':
            input_list[idx] = '%20'
    return ''.join(input_list)

    # Method 2
    # return input_str.replace(' ', '%20')

def main():
    my_str = "My name is Bond."
    print 'Before:', my_str
    new_str = return_url(my_str)
    print 'After:', new_str

main()
