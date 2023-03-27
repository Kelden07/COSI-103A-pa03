from transaction import Transaction

class Tracker:
    def __init__(self, db_filename):
        self.db_filename = db_filename
        self.transaction = Transaction(db_filename)

    def show_categories(self):
        categories = self.transaction.get_categories()
        print("Categories:")
        for category in categories:
            print(category)

    def add_category(self):
        new_category = input("Enter new category name: ")
        self.transaction.add_category(new_category)
        print(f"{new_category} added to categories.")

    def modify_category(self):
        old_category = input("Enter category name to modify: ")
        new_category = input("Enter new category name: ")
        self.transaction.modify_category(old_category, new_category)
        print(f"{old_category} modified to {new_category}.")

    def show_transactions(self):
        transactions = self.transaction.get_transactions()
        print("Transactions:")
        for transaction in transactions:
            print(transaction)

    def add_transaction(self):
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        self.transaction.add_transaction(amount, category, date, description)
        print("Transaction added.")

    def delete_transaction(self):
        transaction_id = input("Enter transaction id to delete: ")
        self.transaction.delete_transaction(transaction_id)
        print(f"Transaction {transaction_id} deleted.")

    def summarize_by_date(self):
        summary = self.transaction.summarize_by_date()
        print("Summary by Date:")
        for row in summary:
            print(row)

    def summarize_by_month(self):
        summary = self.transaction.summarize_by_month()
        print("Summary by Month:")
        for row in summary:
            print(row)

    def summarize_by_year(self):
        summary = self.transaction.summarize_by_year()
        print("Summary by Year:")
        for row in summary:
            print(row)

    def summarize_by_category(self):
        summary = self.transaction.summarize_by_category()
        print("Summary by Category:")
        for row in summary:
            print(row)

    def print_menu(self):
        print("Tracker Menu")
        print("0. Quit")
        print("1. Show categories")
        print("2. Add category")
        print("3. Modify category")
        print("4. Show transactions")
        print("5. Add transaction")
        print("6. Delete transaction")
        print("7. Summarize transactions by date")
        print("8. Summarize transactions by month")
        print("9. Summarize transactions by year")
        print("10. Summarize transactions by category")
        print("11. Print this menu")

if __name__ == "__main__":
    tracker = Tracker("tracker.db")
    tracker.print_menu()
    option = input("Enter option: ")
    while option != "0":
        if option == "1":
            tracker.show_categories()
        elif option == "2":
            tracker.add_category()
        elif option == "3":
            tracker.modify_category()
        elif option == "4":
            tracker.show_transactions()
        elif option == "5":
            tracker.add_transaction()
        elif option == "6":
            tracker.delete_transaction()
        elif option == "7":
            tracker.summarize_by_date()
        elif option == "8":
            tracker.summarize_by_month()
        elif option == "9":
            tracker.summarize_by_year()
        elif option == "10":
            tracker.summarize_by_category()
        elif option == "11":
            tracker.print_menu()
        else:
            print("Invalid option. Please try again.")
        option
