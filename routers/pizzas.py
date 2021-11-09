from fastapi import APIRouter
from .utilts import get_data_from_category_name, get_data_by_id

router = APIRouter()


@router.get("/")
def get_all_pizzas():
    """
    Get all pizzas available from Pizzas.json
    :return: [{<pizza_format>}, {<pizza_format>}, ...] *pizza_format:
      {"dishId": int, "dishName": str, "dishPrice": int, "dishImage": str}
    """
    return get_data_from_category_name("Pizzas")


@router.get("/{pizza_id}")
def get_pizza_by_id(pizza_id: int):
    """
    Get pizza by id from Pizzas.json
    :param pizza_id: pizza id
    :return: {"dishId": int, "dishName": str, "dishPrice": int, "dishImage": str}
    """
    return get_data_by_id("Pizzas", pizza_id)
