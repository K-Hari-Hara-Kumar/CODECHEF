for i in range(int(input())):
    N,x,k = list(map(int,input().split()))
    #x = int(input())
    y = N - x
    #k = int(input())
    group_boys = x%k
    group_girls = y%k
    #print(group_boys)
    #print(group_girls)
    result = group_boys-group_girls
    print(abs(result))

