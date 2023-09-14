# no. of  Testcase
for i in range(int(input())):
[2;2R[3;1R[>77;30601;0c]10;rgb:bfbf/bfbf/bfbf]11;rgb:0000/0000/0000    """
    eg: str1 = 'aeiou'
    here, it will go to for loop and it gets checked
    whether each character is in "aeiou"
    if its there,

    op = op + that char

    else, temp will append with values present in op and clears the op


    """
    str1 = input()
    temp = []
    op = ""

    for j in range(len(str1)-1):
        if str1[j] in "aeiou":
            op = op + str1[j]
        else:
            temp.append(op)
            op = ""
    #print(temp)
    #print(max(len(temp)))
    """
    if length of temp is 0
    it checks with length of op, because it might be
    two cases
    i) whether all str1 is having vowels
    ii) all str1 is consonants


    """
    if len(temp) == 0:
        if len(op) > 2:
            print("Happy")

        else:
            print("Sad")

    else:
        if len(max(temp,key=len))>2:
            print("Happy")
        else:
            print("sad")

    """
    if length of highest length element is greater than 2
    it prints as Happy
    else, gives "Sad" as output

    """

