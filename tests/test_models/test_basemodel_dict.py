import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModelFromDict(unittest.TestCase):

    def test_create_instance_from_dict(self):
        # Create a dictionary representation of a BaseModel instance
        base_model_dict = {
            'id': '123',
            'created_at': '2024-02-08T12:00:00.000000',
            'name': 'Test Model',
            'value': 42
        }
        
        # Create a BaseModel instance from the dictionary
        base_model = BaseModel(**base_model_dict)
        
        # Check if the instance is created correctly
        self.assertIsInstance(base_model, BaseModel)
        self.assertEqual(base_model.id, '123')
        self.assertEqual(base_model.name, 'Test Model')
        self.assertEqual(base_model.value, 42)
        self.assertEqual(base_model.created_at, datetime(2024, 2, 8, 12, 0, 0))

    def test_create_instance_from_empty_dict(self):
        # Create an empty dictionary
        empty_dict = {}
        
        # Create a BaseModel instance from the empty dictionary
        base_model = BaseModel(**empty_dict)
        
        # Check if the instance is created correctly with default values
        self.assertIsInstance(base_model, BaseModel)
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertEqual(type(base_model.created_at), datetime)

    def test_create_instance_from_dict_with_invalid_attribute(self):
        # Create a dictionary representation of a BaseModel instance
        base_model_dict = {
            '__class__': 'SomeClass',  # Should not be added as an attribute
            'id': '456',
            'created_at': '2024-02-08T12:00:00.000000',
            'name': 'Test Model',
            'value': 42
        }
        
        # Create a BaseModel instance from the dictionary
        base_model = BaseModel(**base_model_dict)
        
        # Check if the instance is created correctly
        self.assertIsInstance(base_model, BaseModel)
        self.assertFalse(hasattr(base_model, '__class__'))  # Check if '__class__' is not added as an attribute
        self.assertEqual(base_model.id, '456')
        self.assertEqual(base_model.name, 'Test Model')
        self.assertEqual(base_model.value, 42)
        self.assertEqual(base_model.created_at, datetime(2024, 2, 8, 12, 0, 0))


if __name__ == '__main__':
    unittest.main()
