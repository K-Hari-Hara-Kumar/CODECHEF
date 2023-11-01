
def Dracula_Eats(N:int)->int:


    c = 0
    while N>=2:
        c = c+1
        N = N-7
    return c

for i in range(int(input())):
    N = int(input())
    op = Dracula_Eats(N)
    print(op)

"""
There are 
�
N spooky days left until Halloween.
Dracula dines at a mysterious restaurant that changes its spooky menu daily. He particularly enjoys what they serve on Tuesday.

Today is Monday, so he wishes to calculate how many times he can indulge in his favourite menu in the next 
�
N days (including today) before Halloween.

Note that Dracula follows the standard 
7
7-day calendar, with Tuesday immediately following Monday.


APPROACH:
    1. use count c 
    2. use while statement i.e., N > =2 so, in case N is less than 2 it gives 0
    count
    3. N = N-7(as Dracula uses standard week days )



"""


