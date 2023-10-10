def generatemax(l,si,li):
    if(si==li):
        return l[si]
    mid=(si+li)//2
    return max(generatemax(l,si,mid),generatemax(l,mid+1,li))
    
l=[6,8,4,3,5]
print(generatemax(l,0,len(l)-1))
