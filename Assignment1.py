#Name: Keyshawn Forde               Student ID: 100864963
#Assignment 1 

import time

class product:
    def __init__(self, ID, Name, Price, Category):
        self.ID = ID
        self.Name = Name
        self.Price = Price
        self.Category = Category

    def __str__(self):
        return f"ID: {self.ID}, Item Name: {self.Name}, Price: ${self.Price}, Category: {self.Category}"
    
    #Task 1 load and store data
def load_product_data(filename):
    productl = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                ID, Name, Price, Category = line.strip().split(',')
                productl.append(product(ID, Name, float(Price), Category))
        print("Product data loaded successfully.")
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except ValueError as e:
        print(f"Error parsing product data: {e}")
    except Exception as e:
        print(f"Error loading product data: {e}")
    return productl
#task 2 Data manipulation operations
#inserts/adds a new product in the array
def insert_product(productl):
    ID = input("Enter the product ID: ")
    Name = input("Enter the product name: ")
    Price = float(input("Enter the product price: "))
    Category = input("Enter the product category: ")
    n_product = product(ID, Name, Price, Category)
    productl.append(n_product)
    print("Product added.")
#updates the products
def update_product(productl):
    ID = input("Enter product ID to update: ")
    for product in productl:
        if product.ID == ID:
            Name = input(f"Enter new name for {product.Name} (leave blank to keep unchanged): ") or product.Name
            Price = float(input(f"Enter new price for {product.Name} (leave blank to keep unchanged): ") or product.Price)
            Category = input(f"Enter new category for {product.Name} (leave blank to keep unchanged): ") or product.Category
            product.Name = Name
            product.Price = Price
            product.Category = Category
            print("Product updated.")
            return
    print(f"Product with ID {ID} not found.")
#deletes the product in the array
def delete_product(productl):
    ID = input("Enter the products ID you want to delete: ")
    for product in productl:
        if product.ID == ID:
            productl.remove(product)
            print("Product deleted.")
            return
    print(f"Product with ID {ID} not found.")
#searches for the product in the array
def search_product(productl):
    ID = input("Enter product ID to search: ").strip()
    for product in productl:
        if product.ID == ID:
            print(f"Found Product: {product}")
            return
    print("Product not found")
#task 3 sorting algorithm
#using bubble sort to sort the array from lowest to highest price
def bubble_sort_products_by_price(productl):
    n = len(productl)
    for i in range(n):
        for j in range(0, n-i-1):
            if productl[j].Price > productl[j+1].Price:
                productl[j], productl[j+1] = productl[j+1], productl[j]
#task 4 complexity analysis
#measures the time it takes to sort using the bubble sort
def display_bubble_sort_time(productl):
    start_time = time.time()
    bubble_sort_products_by_price(productl)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken to sort: {duration:.6f} seconds")
    return duration
#analyzing sort complexity
def analyze_sort_complexity(productl):
    n = len(productl)
    print("\nSorting Complexity Analysis:")
    
    # Theoretical Time Complexity
    best_case_operations = n - 1
    average_case_operations = (n * (n - 1)) // 2
    worst_case_operations = (n * (n - 1)) // 2
    
    print("\nTime Complexity (Big O Notation):")
    print(f"Best Case Time Complexity: O({best_case_operations})")
    print(f"Average Case Time Complexity: O({average_case_operations})")
    print(f"Worst Case Time Complexity: O({worst_case_operations})")
#displays the array values
def display_product_list(productl):
    print("\nProduct List:")
    for product in productl:
        print(product)

def find_product_by_id(productl, ID):
    for product in productl:
        if product.ID == ID:
            return product
    return None

def main():
    filename = 'product_data.txt'
    productl = load_product_data(filename)
    
    if productl:
        display_product_list(productl)
    else:
        print("No products are loaded from the file.")

    while True:
        print("\nMenu:")
        print("1: Add a new product")
        print("2: Update/Change an existing product")
        print("3: Delete a product")
        print("4: Search for a product")
        print("5: Sort all the products by price (Lowest price to highest)")
        print("6: Analyze sort complexity")
        print("7: Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            insert_product(productl)
            display_product_list(productl)

        elif choice == '2':
            update_product(productl)
            display_product_list(productl)

        elif choice == '3':
            delete_product(productl)
            display_product_list(productl)

        elif choice == '4':
            search_product(productl)
            display_product_list(productl)

        elif choice == '5':
            display_bubble_sort_time(productl)
            bubble_sort_products_by_price(productl)
            display_product_list(productl)

        elif choice == '6':
            analyze_sort_complexity(productl)
        
        elif choice == '7':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()