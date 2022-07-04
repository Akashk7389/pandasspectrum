f_obj=open("hello.txt",'w')
list1=["python\n","java\n","c++\n"]
f_obj.writelines(list1)
f_obj.close()