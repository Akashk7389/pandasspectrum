with open("ds44.txt","w") as f_obj:
	print(f_obj.tell())
	f_obj.write("hello")
	print(f_obj.tell())
	f_obj.seek(3)
	f_obj.write("python")