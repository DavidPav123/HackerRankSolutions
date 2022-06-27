from unicodedata import digit


if __name__ == '__main__':
    s = input()

    alnumeric, albetic, digits, lower, upper = False, False, False, False, False

    for i in s:
        if i.isalnum(): alnumeric = True 

        if i.isalpha(): albetic = True

        if i.isdigit(): digits = True

        if i.islower(): lower = True

        if i.isupper(): upper = True

    print(alnumeric)
    print(albetic)
    print(digits)
    print(lower)
    print(upper)




    

