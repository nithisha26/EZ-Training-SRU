'''print the character after incrementing the present character with given index'''
n=input()
k=int(input())
l=ord(n)
if(l>=97 and l<=122):
    if(l+k>122):
        s=(l+k)-122
        print(chr(96+s))

