import sqlite3

class Transaction:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS transactions (item_no INTEGER PRIMARY KEY, amount REAL, category TEXT, date TEXT, description TEXT)")
        self.conn.commit()
    
    def get_transactions(self):
        self.cursor.execute("SELECT * FROM transactions")
        rows = self.cursor.fetchall()
        return rows
    
    def get_categories(self):
        self.cur.execute('SELECT DISTINCT category FROM transactions ORDER BY category')
        rows = self.cur.fetchall()
        return [row[0] for row in rows]
    
    def add_category(self, category_name):
        sql = "INSERT INTO categories (category_name) VALUES (?)"
        self.cur.execute(sql, (category_name,))
        self.conn.commit()

    def add_transaction(self, amount, category, date, description):
        self.cur.execute("INSERT INTO transactions VALUES (NULL, ?, ?, ?, ?)", (amount, category, date, description))
        self.conn.commit()

    def delete_transaction(self, item_no):
        self.cur.execute("DELETE FROM transactions WHERE item_no=?", (item_no,))
        self.conn.commit()

    def modify_category(self, item_no, category):
        self.cur.execute("UPDATE transactions SET category=? WHERE item_no=?", (category, item_no))
        self.conn.commit()

    def show_categories(self):
        self.cur.execute("SELECT DISTINCT category FROM transactions")
        rows = self.cur.fetchall()
        for row in rows:
            print(row[0])

    def show_transactions(self):
        self.cur.execute("SELECT * FROM transactions")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

    def summarize_by_date(self):
        self.cur.execute("SELECT date, SUM(amount) FROM transactions GROUP BY date")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

    def summarize_by_month(self):
        self.cur.execute("SELECT strftime('%Y-%m', date) AS month, SUM(amount) FROM transactions GROUP BY month")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

    def summarize_by_year(self):
        self.cur.execute("SELECT strftime('%Y', date) AS year, SUM(amount) FROM transactions GROUP BY year")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

    def summarize_by_category(self):
        self.cur.execute("SELECT category, SUM(amount) FROM transactions GROUP BY category")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
