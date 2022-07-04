from abc import ABC,abstractmethod

class ParentClass(ABC):

	@abstractmethod
	def do_something(self):
		print("Inside Abstract!")

class SubClass(ParentClass):

	def do_something(self):
		super().do_something()
		print("Another SubClass")

y=ParentClass()
y.do_something()
#x=SubClass()
#x.do_something()				