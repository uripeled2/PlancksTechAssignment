from fastapi import APIRouter
from .utilts import get_data_from_category_name, get_data_by_id

router = APIRouter()


@router.get("/")
def get_all_desserts():
    """
    Get all desserts available from Desserts.json
    :return: [{<dessert_format>}, {<dessert_format>}, ...] *dessert_format:
      {"dishId": int, "dishName": str, "dishPrice": int, "dishImage": str}
    """
    return get_data_from_category_name("Desserts")


@router.get("/{dessert_id}")
def get_dessert_by_id(dessert_id: int):
    """
    Get dessert by id from Desserts.json
    :param dessert_id: dessert id
    :return: {"dishId": int, "dishName": str, "dishPrice": int, "dishImage": str}
    """
    return get_data_by_id("Desserts", dessert_id)
