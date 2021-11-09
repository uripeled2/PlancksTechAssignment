from unittest import TestCase
import requests

from ArcaffeMenu.repeatedTasks.create_menu_file import create_json_file_by_category_name


class TestCreateJsonFileByCategoryName(TestCase):
    def setUp(self):
        url = "https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup"
        self.r_json = requests.get(url).json()
        if not self.r_json["Success"]:
            raise Exception(F"Error in the request, {self.r_json['Errors']}")

    def test_with_invalid_category_name(self):
        with self.assertRaises(ValueError):
            create_json_file_by_category_name(self.r_json, "invalid_category_name")

    def test_with_valid_category_name(self):
        pass














