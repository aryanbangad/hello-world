print("lists")
l=[1,2,3,4,5,6,7,8,9,10]
for num in l:
	if num % 2 == 0:
		print("even")
	else:
		print("odd")
print("tuples")
tup = [(9,0),(3,4),(8,9),(6,7)]
for (v1,v2) in tup:
	print(v1)
	print(v2)
print("dic")
dic = {"k1" :1, "k2" :2, "k3" :3}
for k,v in dic.items():
	print(k)
	print(v)
quit()
