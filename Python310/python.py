'''
i=0
while i<35:
    i=i+1
    if i ==3 or i==15:
        continue
    print(i)
'''
'''
arr =[ 1,2,3,6,7,-1,-4,-7]
p=[]
n=[]
for i in arr:
    if i>0:
        p.append(i)
    else:
        n.append(i)
print(p)
print(n)
'''
"""
a = [1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(a)):
    if i%2==0:
        print(i**2)
"""



'''
s='MSys is a company'
res={'upper':0, 'lower':0, 'space':0}
for i in s:
    if i==' ':
        res['space'] += 1
    elif 'A' <= i <= 'Z':
        res['upper']=res['upper']+1
    elif 'a'<= i <= 'z':
        res['lower']=res['lower']+1
print(res)
'''
'''
arr =[1,2,3,1,10]
res={}

print(res)
'''


'''
arr = [-1, -3, 1, -5, 2, -10, 8, 7]
for i in arr:
    if arr>0:
        print(arr[])
'''
n = int(input())
fact = 1
for i in range(1,n+1):
    fact = fact*i

print(n,"factorial is",fact)
'''
'''n = input("enter ur string:")
up = ""
lo =""
sp=""
for i in n:
    if  i == i.upper():
        up = up+i

    elif i==i.lower():
        lo = lo + i
    else:
        sp =sp+i
print("uppercase letters:",up)
print("lower caseletters:",lo)
print("special charecters:",sp)'''
'''
n = input()
res={"up":0, "low":0,"sp":0}
for i in n:
    if i == " ":
        res["sp"] += 1
    elif "A" <= i<= "Z":
        res["up"] += 1
    elif "a"<= i <= "z":
        res["low"] += 1
print(res)
for k,v in res.items():
    print(k,":",v)
'''







'''
l=[10,5,7,8,9]
t=0
for i in l[1:4]:
    t = t+i
    
print(t)
print(l[1:4])

'''
'''
d=[3,6,8,10,3,5]
t=0
for i in range(0,len(d)):
    if i%2==0:
        t += i
    
print(t)

'''
'''
s=int(input())
r=int(input())
l=[]
j=[]
for i in range(s,r+1):
    if i%2==0:
       
        l.append(i)
    else:
        j.append(i)
print(j)
print(l)
'''


'''
a = 'msystech'
for i in range(0,7):
    if i%2==0:
        print(a[i])
'''
'''
l = int(input("entr your no:"))
n1,n2 = 0,1
if l<=1:
    print(1)
print("fabonacci series:",n1,n2,end=" ")
for i in range(2,l+1):
    n3 = n1+n2
    n1 = n2
    n2 = n3
    print(n3,end=" ")
print()
'''
n = input()
l = len(n)
t = 0
for i in n:
    i = int(i)
    t += i**l
if int(n)==t:
    print("armstrong")
else:
    print("not")
'''
'''
n=int(input())
temp=1
for i in range(1,n+1):
    temp =temp*i
print(n)
'''
























































































































