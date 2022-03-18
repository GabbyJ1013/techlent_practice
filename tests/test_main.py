from app.src.srcsub1.calculator import Calculator

cal = Calculator()

def test_add():
	assert cal.add(1,2)==3
	assert cal.add(1,1)==2 
