#!/usr/bin/python3
"""
    Module contains unittetst for base model
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """class defines tests for base model"""

    def setUp(self):
        """setup method for class test"""
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.my_model.created_at = datetime.now()

    @unittest.skip("demonstrating skipping test")
    def test_nothing(self):
        self.fail("shouldnt happen")

    def test_name(self):
        """tests model name"""
        self.assertEqual(self.my_model.name, "My First Model")

    def test_number(self):
        """tests model number"""
        self.assertEqual(self.my_model.my_number, 89)

    def test_id(self):
        """tests id"""
        self.assertTrue(self.my_model.id)

    def test_save(self):
        self.my_model.save()
        self.assertNotEqual(self.my_model.created_at, datetime.now())

    def test_data(self):
        """tests the time"""
        self.assertNotEqual(self.my_model.created_at, datetime.now())


"""
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key,
    type(my_model_json[key]), my_model_json[key]))
"""

if __name__ == "__main__":
    unittest.main()
