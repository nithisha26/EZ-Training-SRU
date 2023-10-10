l=input()
left=0
right=len(l)-1
while left<right:
    if l[left]==l[right]:
        left+=1
        right+=1
        
    else:
        left+=1
