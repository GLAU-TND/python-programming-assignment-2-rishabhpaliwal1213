n=int(input())
a=bin(n)
b=str(a)
c=0
max =0
for i in b:
    if i == '1':
        c=c+1
    elif c > max:
        max=c
        c=0
print(max)
