# not-repeated
n=int(input())
i=list(map(int,input().split()))[:n]
for j in i:
    s=i.count(j)
    if s==1:
        print(j)
