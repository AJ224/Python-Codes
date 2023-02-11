#Write a Python program that display all leap years form 1900-2101
#Roll no. 1316

print("Leap Years : ")
for a in range(1900,2101):
	if (a%4==0):
		print("{0}".format(a))