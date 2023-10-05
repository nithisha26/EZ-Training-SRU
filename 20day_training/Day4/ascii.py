'''a=input()
if(a.islower()):
    print(ord(a)-64)
else:
    print(ord(a)-96)'''

x=input()
num=int(input())
if(x.islower()):
    if((ord(x)+num)>122):
        print(chr(ord(x)+num-26))
    else:
        print(chr(ord(x)+num))
else:
    if((ord(x)+num)>90):
        print(chr(ord(x)+num-26))
    else:
        print(chr(ord(x)+num))
        
