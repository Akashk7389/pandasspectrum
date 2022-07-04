class Person:

	def __init__(self,name,age,place):

		self.name=name
		self._age=age
		self.__place=place

p1=Person("Anu",23,"EKM")
print(p1.name)
print(p1._age)
print(p1.__place)		