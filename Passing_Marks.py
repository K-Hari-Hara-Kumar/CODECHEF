for i in range(int(input())):
    NX = list(map(int,input().split()))
    N=NX[0]
    X = NX[1]
    marks = list(map(int,input().split()))
    marks.sort()
    for i in range(X):
        temp = marks.pop()
    print(temp-1)


"""
Sample Testcaes:

Input:

3
2 2
5 1
4 1
5 1 7 4
4 3
15 70 100 31

output:

0
6
30

Explaination:

    1. Initial Loop indicates the testcase iteration.
    2. NX is a list having number of students and Pass mark students
    3. N --> no of students
    4. X --> NO of students passed
    5.marks --> list of marks of N students
    6.sorted the marks list eg: [15,70,100,31] --> [15,31,70,100]
    7.Based on the given probelm condition 2nd loop is used with parameters of X
    8. it pops the max element from the marks list and given last stored elementin temp
    9.printing temp -1 , required result


"""
