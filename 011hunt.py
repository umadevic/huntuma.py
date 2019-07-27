u=list(map(str,input().split()))
s=[]
for i in u:
	p=i[::-1]
	s.append(p)
for j in s:
	print(j,end=" ")
