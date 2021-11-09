import json


def create_json_file_by_category_name(r: dict, category_name: str):
    """
    This function creates a category_name.json file of the categories_list from category_name.
    :param r: json data of the restaurant from the web
    :param category_name: category name (Drinks/Pizzas/Desserts)
    """

    with open(F"{category_name}.json", "w") as f:
        done = False
        for categories_list in r["Data"]["categoriesList"]:
            if done:
                break
            if categories_list["categoryName"] == category_name:
                json_object = json.dumps(categories_list)
                f.write(json_object)
                done = True
        if not done:
            raise ValueError(f"{category_name} not found")
