# AutoCountry Vehicle Finder v0.1
# This program is designed to help the AutoCountry sales manager determine which vehicles are authorized for purchase and sale.

#List of allowed vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla Cybertruck', 'Toyota Tundra', 'Nissan Titan']

def display_menu():
	"""Function to display the menu."""
	print("\nPlease Enter the following number below from the following menu:")
	print("1. PRINT all Authorized Vehicles")
	print("2. Exit")

def print_vehicles():
	"""Function to print the list of allowed vehicles."""
	print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
	for vehicle in AllowedVehiclesList:
		print(vehicle)

def main():
	"""Main Function to run the program."""
	while True:
		display_menu()
		choice = input("\nEnter your choice: ")
		if choice == '1':
			print_vehicles()
		elif choice == '2':
			print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
			break
		else:
			print("\nInvalid input. Please enter 1 or 2.")

#Run the program
if __name__== "__main__":
	main()
# The program will display a menu with two options: to print the list of authorized vehicles or to exit the program.
# When the user selects option 1, the program will print the list of authorized vehicles.
# When the user selects option 2, the program will exit.
# The program will continue to display the menu until the user chooses to exit.