l=list(map(int,input().split()))
target=int(input())
left=0
right=len(l)-1
while left<right:
    sum1=l[left]+l[right]
    if sum1==target:
        print("Found")
        break
    elif sum1<target:
        left+=1
    else:
        right-=1
