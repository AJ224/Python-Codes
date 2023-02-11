#Write a Python program using for loop to calculate factorial of a number.
#Roll no.1316

a= int(input("Enter a Number: "))
fac = 1
for i in range(1, a + 1):
      fac = fac * i
print("factorial of ",a, " is ", fac)