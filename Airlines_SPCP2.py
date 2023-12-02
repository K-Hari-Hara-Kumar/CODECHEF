def Airlines(X:int,N:int)->int:
    #res = 0 if N%100==0 else 1
    res = 0
    for i in range(0,N,100):
        res = res + 1
    op = res - X
    aircrafts = 0 if op <=0 else op
    return aircrafts
if __name__ == "__main__":
    for i in range(int(input())):
        X,N = list(map(int,input().split()))
        result = Airlines(X,N)
        print(result)
