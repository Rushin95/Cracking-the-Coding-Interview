# return a new string with count of all the occuring characters.
# New string should be smaller than the original one

def compress_string(input_str):
    new_list = list(input_str[0])
    count = 1
    for i in range(len(input_str)):
        if i <len(input_str)-1:
            if input_str[i] == input_str[i+1]:
                count +=1

            else:
                # new_str += str(count) + input_str[i+1]
                new_list.append(str(count))
                new_list.append(input_str[i+1])
                count = 1
        else:
                new_list.append(str(count))
    if len(new_list)>len(input_str):
        return input_str
    else:
        return ''.join(new_list)
def main():
    my_str = 'ababbaaaaaaa'
    print compress_string(my_str)

main()
