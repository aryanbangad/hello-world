print("welcome to bill maker")

items = []
itemprices = []
itemquantitys = []
totalprices = []

print("choose what you want to do")
print("to add new item enter: new")
print("to show bill enter: show")
while True:
	choice = input("your choice: ")
	if choice == "new":
		item = input("item: ")
		items.append(item)
		itemprice = int(input("price of item: "))
		itemprices.append(itemprice)
		itemquantity = int(input("quantity of the item: "))
		itemquantitys.append(itemquantity)
		totalprice = itemprice * itemquantity
		totalprices.append(totalprice)
	elif choice == "show":
		print("item            price            quantity            total price")
		print(str(items[0])+"            "+str(itemprices[0])+"            "+str(itemquantitys[0])+"            "+str(totalprices[0]))