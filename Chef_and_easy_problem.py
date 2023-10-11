

def chef_easy_problem(l1: list[int])->int:
    res = 0
    l1.sort(reverse=True)
    
    for i in l1[::2]:
        res = res + i
    return res

for i in range(int(input())):
    N = int(input())
    l1 = list(map(int,input().split()))[:N]
    op = chef_easy_problem(l1)
    print(op)


"""
APPROACH:

    1. sort in reverse order i.e., descending order
    2. initialize a variable for keeping the sum of chefs max. stone
    plies removing from the table
    3.Iterate , taking the sequnece as step l1[::2]
    4. add the i to res
    here, is the answer, which satisfied all testcases.


"""
