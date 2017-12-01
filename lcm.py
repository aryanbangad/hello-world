print("hello ,this is a tool to find the lcm of numbers")
a=int(input("Enter first number: "))

b=int(input("Enter second number: "))
if(a<b):
	min1=b
else:
	min1=a
while(1):
	if(min1%a==0 and min1%b==0):
		print("lcm is",min1)
		break
	min1=min1+1

