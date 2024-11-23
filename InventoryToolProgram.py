def display_menu():
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Edit Item")
    print("4. Search by Name")
    print("5. Find Largest")
    print("6. Find Smallest")
    print("7. Calculate Average")
    print("8. Quit")

def add_item(collection):
    name = input("Enter item name: ")
    attribute = float(input("Enter item attribute (e.g., price, weight): "))
    collection.append({'name': name, 'attribute': attribute})
    print(f"Item '{name}' added.")

def remove_item(collection):
    name = input("Enter the name of the item to remove: ")
    for item in collection:
        if item['name'] == name:
            collection.remove(item)
            print(f"Item '{name}' removed.")
            return
    print(f"Item '{name}' not found.")

def edit_item(collection):
    name = input("Enter the name of the item to edit: ")
    for item in collection:
        if item['name'] == name:
            new_name = input("Enter new name: ")
            new_attribute = float(input("Enter new attribute: "))
            item['name'] = new_name
            item['attribute'] = new_attribute
            print(f"Item '{name}' updated.")
            return
    print(f"Item '{name}' not found.")

def search_by_name(collection):
    name = input("Enter the name of the item to search: ")
    for item in collection:
        if item['name'] == name:
            print(f"Item found: {item}")
            return
    print(f"Item '{name}' not found.")

def find_largest(collection):
    if not collection:
        print("No items in the collection.")
        return
    largest = max(collection, key=lambda x: x['attribute'])
    print(f"Item with the largest attribute: {largest}")

def find_smallest(collection):
    if not collection:
        print("No items in the collection.")
        return
    smallest = min(collection, key=lambda x: x['attribute'])
    print(f"Item with the smallest attribute: {smallest}")

def calculate_average(collection):
    if not collection:
        print("No items in the collection.")
        return
    average = sum(item['attribute'] for item in collection) / len(collection)
    print(f"Average attribute value: {average:.2f}")

def main():
    collection = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_item(collection)
        elif choice == '2':
            remove_item(collection)
        elif choice == '3':
            edit_item(collection)
        elif choice == '4':
            search_by_name(collection)
        elif choice == '5':
            find_largest(collection)
        elif choice == '6':
            find_smallest(collection)
        elif choice == '7':
            calculate_average(collection)
        elif choice == '8':
            print("Thank you for using the Inventory Management System! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
