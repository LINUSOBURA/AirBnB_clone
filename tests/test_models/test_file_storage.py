import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_all_method_returns_dictionary_of_objects(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        objects = self.storage.all()
        self.assertEqual(len(objects), 2)
        self.assertIn("BaseModel." + obj1.id, objects)
        self.assertIn("BaseModel." + obj2.id, objects)

    def test_new_method_sets_object_correctly(self):
        obj = BaseModel()
        self.storage.new(obj)
        objects = self.storage.all()
        self.assertIn("BaseModel." + obj.id, objects)

    def test_save_method_serializes_objects_to_file(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload_method_deserializes_file_to_objects(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        objects = new_storage.all()
        self.assertIn("BaseModel." + obj.id, objects)

    def test_reload_method_does_nothing_if_file_does_not_exist(self):
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_base_model_save_method_calls_save_method_of_storage(self):
        obj = BaseModel()
        obj.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_base_model_init_calls_new_method_of_storage_for_new_instance(self):
        obj = BaseModel()
        objects = self.storage.all()
        self.assertIn("BaseModel." + obj.id, objects)

if __name__ == '__main__':
    unittest.main()
