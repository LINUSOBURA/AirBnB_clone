import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_empty(self):
        # Test if all() returns an empty dictionary when no objects are stored
        all_objects = self.storage.all()
        self.assertEqual(all_objects, {})

    def test_new(self):
        # Test if new() adds an object to __objects with the correct key
        obj = BaseModel()
        self.storage.new(obj)
        all_objects = self.storage.all()
        self.assertIn("BaseModel." + obj.id, all_objects)

    def test_save_reload(self):
        # Test if save() serializes objects to the file and reload() deserializes them back
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        # Create a new storage instance to simulate reloading from file
        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        self.assertIn("BaseModel." + obj1.id, all_objects)
        self.assertIn("BaseModel." + obj2.id, all_objects)

if __name__ == '__main__':
    unittest.main()
