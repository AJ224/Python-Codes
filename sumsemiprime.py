#p = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
p=[2]
for i in range(3,201): 
  if i>1: 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        p.append(i)

x = []
for i in p:
    for j in p:
        if i!=j:
            x.append(i*j)
            
a = []
for i in x:
    for j in x:
        if i+j<=200:
            a.append(i+j)


t = int(input())
for i in range(t):
    n = int(input())
    if n in a:
        print("YES")
    else:
        print("NO")