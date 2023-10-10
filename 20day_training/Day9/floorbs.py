def bs_floor(l,target):
    start=0
    end=len(l)-1
    floor=-1
    while(start<=end):
        mid=(start+end)//2
        if l[mid]==target:
            print(l[mid])
            break
        elif l[mid]<target:
            floor=l[mid]
            start=mid+1
        else:
            end=mid-1
    else:
        print(floor)
l=list(map(int,input().split()))
target=int(input())
bs_floor(l,target)
#ceil=-1   ceil=l[mid] in else   ceil=float('inf')





