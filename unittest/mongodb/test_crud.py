import unittest
from mongodb import CRUD


class TestCRUD(unittest.TestCase):
    def setUp(self) -> None:
        self.operation = CRUD()
        self.db = 'db_test'
        self.collection = 'collection_test'
        self.test_cases = [{'name': 'TestMan1', 'age': 30},
                           {'name': 'TestMan2', 'age': 40}]

    def tearDown(self) -> None:
        self.operation.delete(self.db, self.collection, name='TestMan1')
        self.operation.delete(self.db, self.collection, name='TestMan2')

    def test_create(self):
        res1 = self.operation.read(self.db, self.collection)
        self.operation.create(self.db, self.collection, **self.test_cases[0])
        res2 = self.operation.read(self.db, self.collection)
        self.assertEqual(len(res1) + 1, len(res2))
        self.operation.delete(self.db, self.collection, name='TestMan1')