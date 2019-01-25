import app

#make the test fail

def test_app():
	input_values = ['I', 'am', 'legend']
	output = []

	def mock_inputs(s):
		output.append(s)
		return input_values.pop(0)
	app.input = mock_inputs
	app.print = lambda s: output.append(s)

	app.main()

	assert output == ['hello']	

#make the test pass by changing the output result

def test_app():
	input_values = ['I', 'am', 'legend']
	output = []

	def mock_inputs(s):
		output.append(s)
		return input_values.pop(0)
	app.input = mock_inputs
	app.print = lambda s: output.append(s)

	app.main()

	assert output == ['first: ', 'second: ', 'third: ']	

