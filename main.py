import requests

from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

from repeatedTasks.create_menu_file import create_json_file_by_category_name
from routers import drinks, pizzas, desserts, orders

app = FastAPI()


# create json files for each category, Update every day
@app.on_event("startup")
@repeat_every(seconds=60 * 60 * 24)   # 60 seconds * 60 minutes * 24 hours = 1 day
def create_menu_json_files():
    url = "https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup"
    r_json = requests.get(url).json()
    if not r_json["Success"]:
        raise Exception(F"Error in the request, {r_json['Errors']}")

    create_json_file_by_category_name(r_json, "Drinks")
    create_json_file_by_category_name(r_json, "Pizzas")
    create_json_file_by_category_name(r_json, "Desserts")


# Routes
app.include_router(drinks.router, prefix="/drinks")
app.include_router(pizzas.router, prefix="/pizzas")
app.include_router(desserts.router, prefix="/desserts")
app.include_router(orders.router, prefix="/orders")
