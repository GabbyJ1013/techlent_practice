from app.src.srcsub1.calculator import Calculator

cal = Calculator()

def test_add():
	assert cal.add(1,2)==3
	assert cal.add(1,1)==2 

def test_subtract():
	assert cal.subtract(2,1)==1
	assert cal.subtract(3,1)==2
	assert cal.subtract(5,2)==3
