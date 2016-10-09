#NonRepeatingNumbers.py
#Program looks for non-repeating number(s) in an N size array
#Created by: Oscar Cairoli

def main():

	counter = 0
	number_not_found = True
	one_number = 1
	myArray = []

	print('Program looks for non-repeating number(s) in an N size array.') 
	print('Returns none if not found.')
	print('')
	print('Hit "Ctrl-C" to quit program.')
	print('Press any non-digit key when done entering numbers')
	print('')
	
	while(True):
		print("Enter a number:")
		try:
			user_input = int(raw_input(">>"))
			myArray.append(user_input)
		except ValueError:
			break
	
	for i in range(0, len(myArray)):
		for j in myArray:
			if (myArray[i] == j):
				counter += 1

		if (counter == one_number):
			print("The number {} appears one time.".format(myArray[i]))
			number_not_found = False
		
		counter = 0

	if number_not_found:
		print("Number not found!")


if __name__ == "__main__":
	main()