#Write a python program to calculate sum of cubes of numbers from 1-n
#Roll No. 1316

n=int(input("Enter no. of Terms : "))
sum=0
for i in range(1,n+1):
    sum=sum+(i*i*i)
print("The sum of cubes of numbers from 1 to",n,"is",round(sum,2))