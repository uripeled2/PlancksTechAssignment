from typing import Optional
import json

from fastapi import HTTPException


def get_data_from_dish(dish: dict) -> Optional[dict]:
    """
    :param dish: {"dishId": int, "dishName": str, "dishPrice": int, "dishImage": str, ...}
    :return: standard format -> {"dishId": int, "dishName": str, "dishPrice": int, "dishImage": str}
    """

    return {"dishId": dish['dishId'], "dishName": dish['dishName'],
            'dishDescription': dish['dishDescription'], "dishPrice": dish['dishPrice']}


def get_data_from_dish_list(dish_list: list) -> list:
    """
    :param dish_list: [<dish>, <dish>, ...]
    :return: [<dish_format>, <dish_format>, ...] * see dish_format in get_data_from_dish
    """
    data = []
    for dish in dish_list:
        data.append(get_data_from_dish(dish))
    return data


def get_data_from_category_name(category_name: str) -> list:
    """
    :param category_name: category name (Drinks/Pizzas/Desserts)
    :return: [<dish_format>, <dish_format>, ...]  * see dish_format in get_data_from_dish
    """
    with open(F"{category_name}.json", 'r') as f:
        dish_list = json.load(f)['dishList']
        return get_data_from_dish_list(dish_list)


def get_data_by_id(category_name: str, dish_id: int):
    # Can validate dish_id over middleware
    """
    :param category_name: category name (Drinks/Pizzas/Desserts)
    :param dish_id: dish id
    :return: dish_format * see dish_format in get_data_from_dish or HTTP404 if item not found or an HTTP404 if
    id not found
    """
    with open(F"{category_name}.json", 'r') as f:
        dish_list = json.load(f)['dishList']
        for dish in dish_list:
            if dish['dishId'] == dish_id:
                return get_data_from_dish(dish)
    return HTTPException(status_code=404, detail=F"Item from {category_name} with id = {dish_id} not found")
