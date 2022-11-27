'''n=int(input())
temp=1
for i in range(1,n+1):
    temp=temp*i
print(temp)'''

'''a=[2,3,4,5,6,7,9]
temp=0
for i in range(0,7):
    temp=temp+i
print(temp)'''
'''
count=0
for i in range(6):
    for i in range(5):
       count+=1
print(count)
'''

'''arr=[1,2,3,4,5,5]
r=0
for in range(7):
    for j in range(4)'''
'''
a='string'
s=''
for i in a:
    s=s+i
print(s[::-1])
'''



'''
s=[1,2,3,4,5,6,7,"u",8,8]
for i in range(len(s)):
    
print(len(i))
'''
'''
a=int(input("enter the number: "))
b=int(input("enter the number: "))
c=int(input("enter the number: "))
d=int(input("enter the number: "))
if a>b:
    if a>c:
        if a>d:
            print(a,"is greaterthen")

elif b>d:
    if b>c:
        if b>a:
            print(b,"is grater")

elif c>d:
    if c>b:
        if c>a:
            print(c,"is greater")
else:
    print(d,"is greater")

'''

'''
def suresh_kanni():
    
    a=[-1,2,3,-4,5,6,-7,8,-9,-15,5,6,7,-34]
    p=[]
    n=[]
    res=0
    for i in a:
        if i<=0:
            p.append(i)
        else:
            if i>=0:
                n.append(i)
    print(p)
    print(n)
suresh_kanni()
'''
'''
a=[-1,2,3,-4,5,6,-7,8,-9,-15,5,6,7,-34]
n=[]
p-=[]
res=0
for i in a:
    if i<=0:
        n=n+[i]#[]+[-1]=[-1]+[-4]=[-1,-4]
    else:
        if i>=0:
            p=p+[i]#[],+[2]=[2]+[3]=[2,3]
print(p)
print(n)
'''
'''
a = [1,0,20,34,3]
s = min(a)
print(s)
'''
'''
def fabo(n):
    if n<=1:
        return n
    else:
        return fabo(n-1)+fabo(n-2)
print(fabo(7))
'''

'''
a=[1,3,5,6,6,7,8,9,10]
e=[]
f=[]
for i in a:
    if i%2==0:
        e=e+[i*3]
    else:
        if i%2!=0:
            f=f+[i**2]
print(e)
print(f)
'''
'''
def sub(u,v):
    """
    This is an example of functions substraction
    """
    return(u-v)
z=sub(8,5)
print(z)
print(sub.__doc__)
'''
'''
def odd_num(n):
    
    s=0
    m=[]
    for i in range(0,n+1):
        if i%2!=0:
            s=s+i
            m=m+[i]
            
    
    return(s)
n=int(input())
m=int(input())
z=odd_num(n)
u=odd_num(m)
print(z)
print(m)

'''
'''
def bwt_numb(n):
    s=[]
    count=0
    for i in range(0,n+1):
        if i%2==0:
            s=s+[i]
    return (s)
def tot(w):
    d = 0
    for i in w:
        d += i
    return d
    

n=int(input())
w=bwt_numb(n)
print(w)
print(txot(w))
'''
'''
a=[1,2,3,4,5,6]
for i in a[1:5]:
    print([i])
'''

'''

def mul_num(n):

    i=1
    for i in range(0,11):
        if i<=10:
            i=i
        print(n ,"x",i,"=",(n*i))
n=int(input())
mul_num(n)
'''
a=str(input())
for i in a:
if a[::]==a[::-1]:
    print("palandram")
else:
    print("not a palandram")
    























    



































































































