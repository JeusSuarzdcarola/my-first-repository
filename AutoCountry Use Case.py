# AutoCountry Vehicle Finder v0.1.3
# This program is designed to help the AutoCountry sales manager determine which vehicles are authorized for purchase and sale.
# Path to the file storing authorized vehicles
import os

# File where vehicles are stored
VEHICLE_FILE = "data/test.txt"

def load_vehicles():
    if not os.path.exists(VEHICLE_FILE):
        os.makedirs(os.path.dirname(VEHICLE_FILE), exist_ok=True)
        default_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla Cybertruck', 'Toyota Tundra', 'Nissan Titan']
        with open(VEHICLE_FILE, 'w') as f:
            for vehicle in default_vehicles:
                f.write(vehicle + '\n')
        return default_vehicles
    else:
        with open(VEHICLE_FILE, 'r') as f:
            return [line.strip() for line in f if line.strip()]

def save_vehicle(vehicle):
    with open(VEHICLE_FILE, 'a') as f:
        f.write(vehicle + '\n')

def display_menu():
    print("\nPlease Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. Exit")

def main():
    vehicles = load_vehicles()
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            print("\nAuthorized Vehicles:")
            for v in vehicles:
                print(f"- {v}")

        elif choice == '2':
            name = input("\nEnter vehicle name to search: ").strip()
            if name in vehicles:
                print(f"{name} is an authorized vehicle.")
            else:
                print(f"{name} is NOT an authorized vehicle. If you received this error, please check the spelling and try again.")

        elif choice == '3':
            new_vehicle = input("\nPlease Enter the name of the vehicle to add: ").strip()
            if new_vehicle in vehicles:
                print(f"{new_vehicle} is already in the authorized vehicles list.")
            else:
                vehicles.append(new_vehicle)
                save_vehicle(new_vehicle)
                print(f"You have added {new_vehicle} as an authorized vehicle.")

        elif choice == '4':
            print("\nThank you for using the AutoCountry Vehicle Finder, Good-bye!")
            break

        else:
            print("\ninvalid input. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
# The program will display a menu with two options: to print the list of authorized vehicles or to exit the program.
# When the user selects option 1, the program will print the list of authorized vehicles.
# When the user selects option 2, the program will exit.
# The program will also allow the user to search for a specific vehicle by entering its name.
# If the vehicle is found in the list, the program will confirm that it is an authorized vehicle.
# The program will continue to display the menu until the user chooses to exit.