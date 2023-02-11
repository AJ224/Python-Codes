#Write a Python program using for loop to print all the numbers from m-n thereby classifying them as even or odd
#Roll no. 1316

m=int(input("Enter number from where u want to start: "))
n=int(input("Enter number till where u want to End: "))
for a in range(m,n+1):
    if(a % 2 == 0):
        print("Even no. : ""{0}".format(a))
    elif(a%2!=0):
    	print("Odd no. : ""{0}".format(a))