#Write a python program to sum the series 1+1/2+1/3+1/4….1/n
#Roll no. 1316

n=int(input("Enter the number of terms: "))
sum=0
for i in range(1,n+1):
    sum=sum+(1/i)
print("The sum of series is",round(sum,2))
if (n<=0):
	print("Invalid Input")