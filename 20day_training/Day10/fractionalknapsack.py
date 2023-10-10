w=int(input())
wt=list(map(int,input().split()))
pr=list(map(int,input().split()))
l=list(zip(wt,pr))
l.sort(key=lambda x:x[1]/x[0],reverse=True)
maxpr=0
for weight,profit in l:
    if weight<=w:
        maxpr+=profit
        w-=weight
    else:
        maxpr+=w*(profit/weight)
        break
print(maxpr)
