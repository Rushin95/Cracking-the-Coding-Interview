# find if one string is rotation another

def isSubString(input_1, input_2):
    str_1 = input_1 if len(input_1) > len(input_2) else input_2
    str_2 = input_1 if len(input_1) < len(input_2) else input_2

    print str_1, str_2
    for i in range(len(str_1)-len(str_2)+1):
        if str_1[i:i+len(str_2)] == str_2:
            return True

    # now considering the rotation
    for i in range(len(str_1)-len(str_2)+1,len(str_1)):
        print i
        if str_1[i:]+str_1[len(str_2) -(len(str_1)-i)]:
            return True
    return False

print isSubString('erbottlewat', 'waterbottle')
