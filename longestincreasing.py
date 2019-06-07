n1=int(input())
l1=list(map(int,input().split()))
m1=[]
c1=1
for i1 in range(n1-1):
	if l1[i1]<l1[i1+1]:
		c1+=1
	else:
		m1.append(c1)
		c1=1
m1.append(c1)
print(max(m1))
