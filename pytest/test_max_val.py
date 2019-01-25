import pytest

#create a maximum val function
lis_ted = [4,20,56,25,29,40,70,76,89,1000,10001]

def max_cal_func(lis_ted):
    for i in range(0, len(lis_ted)):
        temp = lis_ted[0]
        if temp < lis_ted[i]:
            temp = lis_ted[i]
    return temp
        
print (max_cal_func(lis_ted)) 

'''
test inputs and outputs below, includes fixtures: helps
with repeated execution
'''

@pytest.fixture
def maximum():
	return 10001

def test_values_and_functions(maximum): #passed test case
	assert 10001 == lis_ted[10]

def test_len_object(maximum):
	assert 10001 == max_cal_func(maximum)#int has no len failed test

def test_value_of_function(maximum):
	assert 10001 == max_cal_func(lis_ted) #passed test case