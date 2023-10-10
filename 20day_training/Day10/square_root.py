def sqrt_binary_search(num,epsilon=1e-6):
    if num<0:
        raise ValueError("Cannot compute the square value")
    if num<1:
        left,right=num,1
    else:
        left,right=0,num
    while abs(left-right)>epsilon:
        mid=(left+right)/2
        mid_square=mid*mid
        if mid_square<num:
            left=mid
        else:
            right=mid
    return (left+right)/2

num=int(input())
print(sqrt_binary_search(num))
