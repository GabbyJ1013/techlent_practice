class Calculator():
	def __init__(self,name=None,color='blue',pie=3.1):
		self.brand = name
		self.color = color
		self.table = {'pi':pie, 'e':2.168}
		
	def add(self,a,b):
		return a+b
	def circlesquare(self, radius):
		return self.table['pi']*radius**2

if __name__ == "__main__":
	calculator = Calculator('monkey','red',3.141)
	print(calculator.add(1,3))
	print(calculator.brand)
	print(calculator.table['pi'])
	print(calculator.circlesquare(3))
	print(calculator.color)
	
# mainly for demo purposes
