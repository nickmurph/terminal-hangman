guess = input("Enter your first letter guess: ")
while (validate_input(guess) != True):
	guess = input("Invalid input, enter a letter only:")
