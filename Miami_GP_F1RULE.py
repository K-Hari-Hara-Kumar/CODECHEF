# cook your dish here
def Miami_GP(X:int,Y:int)->str:
    ref = int(X*1.07)
    res = "yes" if Y <= ref else "NO"
    return res
    
if __name__ == "__main__":
    for i in range(int(input())):
        X,Y = list(map(int,input().split()))
        op = Miami_GP(X,Y)
        print(op)
    
