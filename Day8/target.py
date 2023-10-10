def fun(l,target):
    def backtrack(start,sum,subset):
        if sum==target:
            res.append(subset)
            return
        if sum>target or start==len(l):
            return
        subset.append(l[start])
        backtrack(start+1,sum+l[start],subset)
        subset.pop()
        backtrack(start+1,sum,subset)
res=[]
backtrack(0,0,[])
