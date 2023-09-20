T = int(input())
for i in range(T):
    nx = input()
    n1 = input()
    l1 = nx.split(" ")
    n = int(l1[0])
    x = int(l1[1])
    l3 = []
    l2 = n1.split(" ")
    for i in l2:
        l3.append(int(i))
    l3.sort()
    for i in range(x):
        l3 = l3[:-1]
        num1 = l3[-1]
    print(num1-1)
