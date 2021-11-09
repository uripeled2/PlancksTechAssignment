from typing import List, Tuple
from fastapi import APIRouter, HTTPException

from .utilts import get_data_by_id
from .models.order import Order

router = APIRouter()


@router.post("/")
def get_price_of_order(order: Order):
    """
    Calculate the price of an order,
     for each item in the order find the price of the item and add it to the total price.
    * If the item is not found in the menu, raise a HTTPException with status code 400.
    :param order: Order object
    :return: The price of the order
    """
    def add_price(category_name: str, lst: List[int]) -> Tuple[int, List[str]]:
        """
        Calculate the price from a list of ids (order.drinks/order.pizzas/order.desserts)
        :param category_name: category name (Drinks/Pizzas/Desserts)
        :param lst: list of ids (order.drinks/order.pizzas/order.desserts)
        :return: price and list of errors that occurred
        """
        category_name_errors = []
        price = 0
        for item_id in lst:
            ret = get_data_by_id(category_name, item_id)
            if isinstance(ret, HTTPException):
                category_name_errors.append(ret.detail)
            else:
                price += ret["dishPrice"]

        return price, category_name_errors

    drinks = order.drinks
    desserts = order.desserts
    pizzas = order.pizzas
    errors = []

    drinks_price, drinks_errors = add_price("Drinks", drinks)
    desserts_price, desserts_errors = add_price("Desserts", desserts)
    pizzas_price, pizzas_errors = add_price("Pizzas", pizzas)

    # Add errors is exists to the list of errors
    if drinks_errors:
        errors.append({'Drinks': drinks_errors})
    if desserts_errors:
        errors.append({'Desserts': desserts_errors})
    if pizzas_errors:
        errors.append({'Pizzas': pizzas_errors})

    if errors:
        raise HTTPException(status_code=400, detail=errors)

    return drinks_price + desserts_price + pizzas_price


# TODO delete
# {
#     "drinks": [2055846, 2055838],
#     "desserts": [2055836, 2055837],
#     "pizzas": [2055833, 2055830]
# }  # OUTPUT: 189