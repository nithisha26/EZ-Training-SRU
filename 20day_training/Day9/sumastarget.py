l=list(map(int,input().split()))
target=int(input())
left=0,right=len(l)-1
while(left<right):
    sum=l[left]+l[right]
    if sum==target:
        print("found")
    elif sum<target:
        left+=1
    else:
        right+=1
else:
    print("not found")
