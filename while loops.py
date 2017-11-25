v = int(input("number less than 10: "))
while v < 10:
	print("v is ", +v)
	print("adding 1 to v to make it bigger")
	v=v+1
	if v == 3:
		print("v is 3 error breaking")
		break
	else:
		print("no problem")
		continue
print("cheaking the value of v if it is 10 ")
if v == 10 :
	print("true")
	print("sucess")
else:
	print("false")
	print("failed")
	
