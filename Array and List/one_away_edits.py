# check if two strings are just one edit away

def new_method(input_str_1, input_str_2):
    str_1 = input_str_1 if len(input_str_2) > len(input_str_1) else input_str_2
    str_2 = input_str_2 if len(input_str_2) > len(input_str_1) else input_str_1
    idx1 = 0
    idx2 = 0
    diff = False

    if len(str_2) - len(str_1) > 1:
        return False

    while idx1 < len(str_1) and idx2 < len(str_2):
        if str_1[idx1] != str_2[idx2]:
            if not diff:
                diff = True
            else:
                return False
            if len(str_1) == len(str_2):
                idx1 += 1
        else:
            idx1 += 1
        idx2 += 1
    return True

# def is_one_away(input_str_1, input_str_2):
#     list_1 = list(input_str_1)
#     list_2 = list(input_str_2)
#
#     if len(list_1) >= len(list_2):
#         for char in list_2:
#             if char in list_1:
#                 list_1.remove(char)
#         if len(list_1) == 1:
#             return True
#     else:
#         for char in list_1:
#             if char in list_2:
#                 list_2.remove(char)
#         if len(list_2) == 1:
#             return True
#     return False

def main():
    str_1 = 'pale'
    str_2 = 'pabbe'
    # print is_one_away(str_1, str_2)
    print new_method(str_1,str_2)

main()
