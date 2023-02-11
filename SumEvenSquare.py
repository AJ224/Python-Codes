#Write a python program to calculate sum of square of even numbers
#Roll No. 1316

n=int(input("Enter no. : "))
def squaresum(n): 
       return (n * (n + 1) / 2) * (2 * n + 1) / 3
print("Sum Of Square Of Even No. from 1 to ",n,"is",squaresum(n))