print("hello,this is a tool to sort numbers into odd and even")
numbers=[]
count=int(input(" Enter the amount numbers you want to sort: "))
for i in range(1,count+1):
	b=int(input("Enter number "+str(i)+": "))
	numbers.append(b)
even=[]
odd=[]
for element in numbers:
	if(element%2==0):
		even.append(element)
	else:
		odd.append(element)
print("The even list: ",even)
print("The odd list: ",odd)