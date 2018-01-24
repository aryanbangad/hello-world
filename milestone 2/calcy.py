import math
def calculator():
	print("welcome to calculator and converter")
	print("choice 1: addition ")
	print("choice 2: subtraction")
	print("choice 3: multiply")
	print("choice 4: divison")
	print("choice 5: remainder")
	print("choice 6: square")
	print("choice 7: squareroot")
	print("choice 8: celsious to fahrenheit")
	print("choice 9: fahrenheit to celsious")
	print("choice 10: find out if number is odd or even")
	choice = int(input("choice: "))
	if choice == 1:
		num1 = int(input("first num: "))
		num2 = int(input("second num: "))
		sum = num1 + num2
		print(sum)      
	elif choice == 2:
		num1 = int(input("first num: "))
		num2 = int(input("second num: "))
		ans = num1 - num2
		print(ans)
	elif choice == 3:
		num1 = int(input("first num: "))
		num2 = int(input("second num: "))
		ans = num1 * num2
		print(ans)
	elif choice == 4:
		num1 = int(input("first num: "))
		num2 = int(input("second num: "))
		ans = num1 / num2
		print(ans)
	elif choice == 5:
		num1 = int(input("first num: "))
		num2 = int(input("second num: "))
		ans = num1 % num2
		print(ans)
	elif choice == 6:
		num = int(input("num: "))
		ans = num ** 2
		print(ans)
	elif choice == 7:
		num = int(input("num: "))
		ans = math.sqrt(num)
		print(ans)
	elif choice == 8:
		temp = int(input("temperature: "))
		temp2 = (9/5) * temp + 32
		print(temp2 + " fahrenheit")
	elif choice ==  9:
		temp3 = int(input("temperature: "))
		temp4 = (temp3 - 32) * 5/9
		print(temp4 + " celsious")
	elif choice == 10:
		numbers = []
		count_of_numbers = int(input("how many numbers do you want to sort: "))
		for i in range(1,count_of_numbers + 1):
			i = int(input("enter number "+ str(i) + ": "))
			numbers.append(i)
		even = []
		odd = []
		for num in numbers:
			if num % 2 == 0:
				even.append(num)
			else:
				odd.append(num)
		print("the odd numbers are " ,odd)
		print("the even numbers are " ,even)
calculator()
repeat = input("do you want to repeat the calculator (please answer in yes or no): ")
while repeat == "yes":
	calculator()
else:
	print("bye")