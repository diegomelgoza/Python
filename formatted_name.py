def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + ' ' + last_name
	return full_name.title()
	
print("Enter 'q' at any time to quit.")
while True:
 	first = input("\nPlease give me a first name: ")
 	if first == 'q':
 		break
 	last = input("Please give me a last name: ")
 	if last == 'q':
 		break

formatted_name = get_formatted_name(first, last)
print("\tNeatly formatted name: " + formatted_name + '.')
