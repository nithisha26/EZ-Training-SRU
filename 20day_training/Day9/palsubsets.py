def has_palin(s):
    def ispalin_rev(left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    res=[]
    for i in range(len(s)):
        pal1=ispalin_rev(i,i)
        if len(pal1)>1:
            res.append(pal1)
        pal2=ispalin_rev(i,i+1)
        if len(pal2)>1:
            res.append(pal2)
    return res
s=input()
result=has_palin(s)
print(result)
