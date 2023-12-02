
def Water_Park(W:int,H:int)->str:
    op = "yes" if 60<=W and 130>=H else "No"
    return op
if __name__ == "__main__":
    W,H = list(map(int,input().split()))
    res = Water_Park(W,H)
    print(res)

