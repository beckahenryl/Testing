
defineList = [6,7,4]
holdsum = sum(defineList)
string = ''.join(str(e) for e in defineList)
split = string.split()

#pass all test cases

def test_lists():
	assert defineList == [6,7,4]

def test_sum():
	assert holdsum == 17

def test_string():
	assert string == '674'

def test_split():
	assert split == ['674']	


