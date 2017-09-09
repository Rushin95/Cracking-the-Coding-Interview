# determine if any permutation of the givern string is palindrome or not

def is_per_pali(input_str):
    counter = {}
    flag = 0
    for idx, char in enumerate(input_str.lower()):
        if char not in counter:
            counter[char]=1
        else:
            counter[char]+=1
    # ignore white space
    counter.pop(' ',None)
    for key,value in counter.iteritems():
        if value%2 != 0:
            flag+=1
            # if more than one odd counts return false
            if flag>1:
                return False
    return True

def main():
    str_1 = 'Tact Coa'
    str_2 = 'ABaBAba'
    print str_1, is_per_pali(str_1)
    print str_2, is_per_pali(str_2)

main()
