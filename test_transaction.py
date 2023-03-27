import unittest
from transaction import Transaction

class TestTransaction(unittest.TestCase):
    def test_init(self):
        t = Transaction("test.db")
        self.assertIsNotNone(t.conn)
        self.assertIsNotNone(t.cur)
