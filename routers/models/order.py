from typing import List
from pydantic import BaseModel


class Order(BaseModel):
    """
    Order model
    drinks: List[<id>, <id>, ...]
    desserts: List[<id>, <id>, ...]
    pizzas: List[<id>, <id>, ...]
    """
    drinks: List[int]
    desserts: List[int]
    pizzas: List[int]
