from typing import List, Tuple
import sqlite3

class Transaction:
    '''This class will be used to create a database and add transactions to the database'''
    def __init__(self, db_file: str) -> None:

        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self) -> None:
        self.conn.execute('''CREATE TABLE IF NOT EXISTS transactions
                            (id INTEGER PRIMARY KEY,
                             item_number TEXT,
                             amount REAL,
                             category TEXT,
                             date TEXT,
                             description TEXT)''')

    def add_transaction(self, item_number: str, amount: float, category: str, date: str, description: str) -> None:

        self.conn.execute(
            "INSERT INTO transactions (item_number, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
            (item_number, amount, category, date, description)
        )
        self.conn.commit()

    def delete_transaction(self, id: int) -> None:
        # check if item number exists in the table
        cursor = self.conn.execute(f"SELECT item_number FROM transactions WHERE id = '{id}'")
        result = cursor.fetchone()
        # delete the transaction if it exists
        self.conn.execute(
            f"DELETE FROM transactions WHERE id = '{id}'")
        self.conn.commit()

    def add_category(self, category: str) -> bool:
        if self.get_category_id(category):
            return False
        self.conn.execute(
            f"INSERT INTO categories (category) VALUES ('{category}')")
        self.conn.commit()
        return True

    def modify_category(self, category: str, new_category: str) -> bool:
        if self.get_category_id(new_category):
            return False
        self.conn.execute(
            f"UPDATE categories SET category = '{new_category}' WHERE category = '{category}'")
        self.conn.commit()
        return True

    def get_category_id(self, category: str) -> int:
        cursor = self.conn.execute('''CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY, category TEXT)''')
        #ALTER TABLE categories ADD COLUMN name TEXT
        result = cursor.fetchone()
        if not result:
            return None
        return result[0]

    def get_transactions(self) -> List[Tuple]:
        cursor = self.conn.execute("SELECT * FROM transactions")
        return cursor.fetchall()

    def get_categories(self) -> List[str]:
        cursor = self.conn.execute(
            "SELECT DISTINCT category FROM transactions UNION SELECT category FROM categories")
        categories = cursor.fetchall()
        return [category[0] for category in categories]

    def summarize_by_date(self) -> List[Tuple]:
        cursor = self.conn.execute(
            "SELECT date, SUM(amount) FROM transactions GROUP BY date")
        return cursor.fetchall()

    def summarize_by_month(self) -> List[Tuple]:
        cursor = self.conn.execute(
            "SELECT strftime('%Y-%m', date) as month, SUM(amount) FROM transactions GROUP BY month")
        return cursor.fetchall()

    def summarize_by_year(self) -> List[Tuple]:
        cursor = self.conn.execute(
            "SELECT strftime('%Y', date) as year, SUM(amount) FROM transactions GROUP BY year")
        return cursor.fetchall()

    def summarize_by_category(self) -> List[Tuple]:
        cursor = self.conn.execute(
            "SELECT category, SUM(amount) FROM transactions GROUP BY category")
        return cursor.fetchall()

    def __del__(self) -> None:
        self.conn.close()
