'''n=int(input())
def fun(n):
    if(n==0):
        return
    fun(n-1)
    print(n)
fun(n)'''
n=int(input())
def fun(n):
    if(n==0):
        return
    print(n,end=" ")
    fun(n-1)
fun(n)
