list_items = [90,23,88,45,20]
x = []

#functions to test
def sort_items (list_items):
	hold_sort = list_items.sort()
	return hold_sort

def value_sort(x):
	return x.sort()

	
#code test line by line	
def test_items():
	assert list_items == [90,23,88,45,20] #passed case
def test_function():
	assert sort_items(list_items) == [90,23,88,45,20] #failed case
def test_val_sort():
	assert 	value_sort([6,5,4]) == [4,5,6]#failed case

	
