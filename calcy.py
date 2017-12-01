import math
def calculator():
	print("welcome to calculator")
	print("choice 1: addition ")
	print("choice 2: subtraction")
	print("choice 3: multiply")
	print("choice 4: divison")
	print("choice 5: remainder")
	print("choice 6: square")
	print("choice 7: squareroot")
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
	else:
		num = int(input("num: "))
		ans = math.sqrt(num)
		print(ans)
calculator()
repeat = input("do you want to repeat it please answer in yes or no: ")
while repeat == "yes":
	calculator()
else:
	print("bye")
