def generatesum(l,si,li):
    if(si==li):
        return l[si]
    mid=(si+li)//2
    return generatesum(l,si,mid)+generatesum(l,mid+1,li)
l=[1,2,3,4,5,6]
print(generatesum(l,0,len(l)-1))
