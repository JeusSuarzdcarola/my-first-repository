# AutoCountry Vehicle Finder v0.1.5
# This program is designed to help the AutoCountry sales manager choose which vehicles to purchase and sell.
import os

#Stored vehicle file
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
                
def save_vehicles(vehicles):
    with open(VEHICLE_FILE, 'w') as f:
        for v in vehicles:
            f.write(v + '\n')

def add_vehicle(vehicle, vehicles):
    if vehicle in vehicles:
        print(f"{vehicle} is already in the authorized vehicles list.")
    else:
        vehicles.append(vehicle)
        save_vehicles(vehicles)
        print(f"{vehicle} has been added as an authorized vehicle.") 

def delete_vehicle(vehicle, vehicles):
    if vehicle in vehicles:
        confirm = input(f"Are you sure you want to delete {vehicle}? (yes/no): ").strip().lower()
        if confirm == 'yes':
            vehicles.remove(vehicle)
            save_vehicles(vehicles)
            print(f"{vehicle} has been removed from the list.")
        else:
            print("Delete cancelled.")
    else:
        print(f"{vehicle} is not in the authorized vehicles list.")

def display_menu():
    print("\nPlease enter a number from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")

def main():
    vehicles = load_vehicles()
    while True:
        display_menu()
        choice = input("choose an option (1-5): ").strip()

        if choice == '1':
            print("\n The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
            for v in vehicles:
                print(f"- {v}")

        elif choice == '2':
             name = input("\nsearch vehicle name: ").strip()
             if name in vehicles:
                print(f"{name} is an authorized vehicle.")
             else:
                    print(f"{name} is NOT an authorized vehicle. If you received this error, please check the spelling and try again.")

        elif choice == '3':
            new_vehicle = input("\nplease enter vehicle name to add: ").strip()
            add_vehicle(new_vehicle, vehicles)

        elif choice == '4':
             remove_vehicle = input("\nPlease enter the full vehicle name to remove: ").strip()
             delete_vehicle(remove_vehicle, vehicles)
            
        elif choice == '5':
             print("\nThank you for using the AutoCountry Vehicle Finder. Good-bye!!")
             break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
        