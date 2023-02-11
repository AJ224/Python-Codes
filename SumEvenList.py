list1 = [int(i) for i in input().split()] 
even_nos = [num for num in list1 if num % 2 == 0] 

print(even_nos)
sum=0
for num in even_nos:
  sum=sum+num
  
print(sum)

