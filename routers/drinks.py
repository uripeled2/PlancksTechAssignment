from fastapi import APIRouter

from .utilts import get_data_from_category_name, get_data_by_id

router = APIRouter()


@router.get("/")
def get_all_drinks():
    """
    Get all drinks available from Drinks.json
    :return: [{<drink_format>}, {<drink_format>}, ...] *drink_format:
      {"dishId": int, "dishName": str, "dishPrice": int, "dishImage": str}
    """
    return get_data_from_category_name("Drinks")


@router.get("/{drink_id}")
def get_drink_by_id(drink_id: int):
    """
    Get drink by id from Drinks.json
    :param drink_id: drink id
    :return: {"dishId": int, "dishName": str, "dishPrice": int, "dishImage": str}
    """
    data = get_data_by_id("Drinks", drink_id)
    return data
