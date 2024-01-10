import csv

def search_contact(filename, search_query):
    found = False
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            # Combine first name and last name for full name search
            full_name = f"{row[0]} {row[1]}"
            if search_query in row or search_query == full_name:
                found = True
                print(f"Contact Found: {full_name}, Phone: {row[2]}")
                break
        if not found:
            print("Contact not found.")

def main():
    filename = 'contacts.csv'
    search_query = input("Enter the contact's name or phone number to search: ")
    search_contact(filename, search_query)

if __name__ == "__main__":
    main()
