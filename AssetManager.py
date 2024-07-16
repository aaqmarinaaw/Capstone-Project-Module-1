from tabulate import tabulate

# Define asset database 

asset_database = [
    {"Asset Number": "2024000001", "Asset Status": "Active", "Asset Type": "Notebook", "Asset Description": "HP Elitebook G10", "Employee First Name": "Brad", "Employee Last Name": "Smith"},
    {"Asset Number": "2024000002", "Asset Status": "Active", "Asset Type": "Notebook", "Asset Description": "HP Elitebook G10", "Employee First Name": "Brad", "Employee Last Name": "Pitt"},
    {"Asset Number": "2024000003", "Asset Status": "Active", "Asset Type": "Notebook", "Asset Description": "HP Elitebook G10", "Employee First Name": "Miley", "Employee Last Name": "Cyrus"},
    {"Asset Number": "2024000004", "Asset Status": "Active", "Asset Type": "Phone", "Asset Description": "Samsung Galaxy S10", "Employee First Name": "Hotma", "Employee Last Name": "Smith"},
    {"Asset Number": "2024000005", "Asset Status": "Active", "Asset Type": "Phone", "Asset Description": "Samsung Galaxy S20", "Employee First Name": "Angelina", "Employee Last Name": "Jolie"},
]


# Function to Print the Welcome Message and Validate User Input
def welcome_user():
    while True:
        first_name = input("Enter your First Name: ")
        if not first_name:
            print("You have not entered any data. Please try again.")
            continue
        elif first_name.isdigit(): 
            print("You have entered incorrect data. Please try again.")
            continue
        
        while True:
            last_name = input("Enter your Last Name: ")
            if not last_name:
                print("You have not entered any data. Please try again.")
                continue
            elif last_name.isdigit():
                print("You have entered incorrect data. Please try again.")
                continue
            break
        

        print(f"Welcome to AssetManager, {first_name} {last_name}!")
        break
    

# Function to Display the Main Menu:
def display_menu():
    print("\nPlease choose an option:")
    print("1. Create New Asset")
    print("2. Read Asset Records")
    print("3. Update Asset Records")
    print("4. Filter Asset Records")
    print("5. Delete Asset Records")
    print("6. Exit")
    

# Function to Create a New Asset:
def create_asset():
    while True:
        last_asset_number = int (asset_database [-1] ["Asset Number"])
        new_asset_number = f"{last_asset_number + 1:010d}"
        
        asset_status = input("Enter Asset Status: ").strip()
        if not asset_status or not asset_status.isalpha():
            print("You have not entered any data or the data you entered is incorrect. Please try again.")
            continue

        asset_type = input("Enter Asset Type: ").strip()
        if not asset_type or not asset_type.isalpha():
            print("You have not entered any data or the data you entered is incorrect. Please try again.")
            continue

        asset_description = input("Enter Asset Description: ").strip()
        if not asset_description:
            print("You have not entered any data. Please try again.")
            continue

        employee_first_name = input("Enter Employee First Name: ").strip()
        if not employee_first_name or not employee_first_name.isalpha():
            print("You have entered incorrect data. Please try again.")
            continue

        employee_last_name = input("Enter Employee Last Name: ").strip()
        if not employee_last_name or not employee_last_name.isalpha():
            print("You have entered incorrect data. Please try again.")
            continue

        new_asset = {
            "Asset Number": new_asset_number,
            "Asset Status": asset_status,
            "Asset Type": asset_type,
            "Asset Description": asset_description,
            "Employee First Name": employee_first_name,
            "Employee Last Name": employee_last_name,
        }
        asset_database.append(new_asset)
        print(f"Asset Number {new_asset_number} is successfully inputted.")
        break


# Function to Read Asset Records:
def read_assets():
    print(tabulate(asset_database, headers='keys', tablefmt = 'pretty'))
    

# Function to Update an Asset*:
def update_asset():
    while True:
            asset_number = input("Enter the Asset Number to update: ").strip()
            if not asset_number.isdigit():
                print("You have entered incorrect data. Try again.")
                continue

            asset_to_update = next((asset for asset in asset_database if asset["Asset Number"] == asset_number), None)
            if not asset_to_update:
                print("Asset Not Found. Try Again.")
                continue

            print("\nChoose the field to update:")
            print("1. Asset Status")
            print("2. Employee First Name")
            print("3. Employee Last Name")

            field_choice = input().strip()
            if field_choice == "1":
                new_value = input("Enter new Asset Status: ").strip()
                if new_value and new_value.isalpha():
                    asset_to_update["Asset Status"] = new_value
                else:
                    print("Invalid input. Update failed.")
                    continue
            elif field_choice == "2":
                new_value = input("Enter new Employee First Name: ").strip()
                if new_value and new_value.isalpha():
                    asset_to_update["Employee First Name"] = new_value
                else:
                    print("Invalid input. Update failed.")
                    continue
            elif field_choice == "3":
                new_value = input("Enter new Employee Last Name: ").strip()
                if new_value and new_value.isalpha():
                    asset_to_update["Employee Last Name"] = new_value
                else:
                    print("Invalid input. Update failed.")
                    continue
            else:
                print("Invalid choice. Update failed.")
                continue

            print(f"Asset Number {asset_number} is updated successfully.")
            break


# Function to Filter Asset Records:
def filter_assets():
    print("\nChoose the field to filter by:")
    print("1. Asset Status")
    print("2. Asset Type")
    print("3. Asset Description")
    print("4. Employee First Name")
    print("5. Employee Last Name")
    
    field_choice = input("Enter choice: ")
    field_name = ["Asset Status", "Asset Type", "Asset Description", "Employee First Name", "Employee Last Name"][int(field_choice)-1]
    filter_value = input(f"Enter value to filter by for {field_name}: ")
    filtered_records = [asset for asset in asset_database if asset[field_name] == filter_value]
    print(tabulate(filtered_records, headers='keys', tablefmt = 'pretty'))


# Function to Delete an Asset
def delete_asset():
    print ("\nDelete an asset.")
    while True:
            asset_number = input("Enter the Asset Number to delete: ").strip()
            if not asset_number.isdigit():
                print("You have input incorrect data. Try again.")
                continue

            asset_to_delete = next((asset for asset in asset_database if asset["Asset Number"] == asset_number), None)
            if not asset_to_delete:
                print("Asset Not Found. Try Again.")
                continue

            asset_database.remove(asset_to_delete)
            print(f"Asset Number {asset_number} successfully deleted.")
            break
    

# Main Function to Run the Program:
def main():
    welcome_user()
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_asset()
        elif choice == "2":
            read_assets()
        elif choice == "3":
            update_asset()
        elif choice == "4":
            filter_assets()
        elif choice == "5":
            delete_asset()
        elif choice == "6":
            print("Goodbye! See you next time!")
            break
        else:
            print("Invalid choice. Please try again.")

main()