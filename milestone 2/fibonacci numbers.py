def fibon():

	n = int(input("how many fibonacci numbers do you want: "))
	a = 1
	b = 1
	output = []
	for i in range(n):
		output.append(a)
		a,b = b,a+b
	print(output)
fibon()


