y=input()
d=1
for j in range(len(y)-1):
    s=y[j]+y[j+1]
    p=int(s)
    if p<=26 and y[j]!="0":
        d+=1
if d==3:
    print(d)
else:
    print(d+(d-1)//2)
