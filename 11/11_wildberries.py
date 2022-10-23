from requests import Session
from models2 import Category, add


def get_response():
    with Session() as session:
        response = session.get(
            url='https://www.wildberries.ru/webapi/menu/main-menu-ru-ru.json'
        )
        # print(response.json())
        return response.json()


def add_to_category_from_smt(list_of_dicts):
    for dictionary in list_of_dicts:
        list_to_add = []
        if isinstance(dictionary, dict):
            for key, value in dictionary.items():
                if isinstance(value, str):
                    if key in ['name', 'seo']:
                        list_to_add.append(value)
                if len(list_to_add) == 2:
                    print(dictionary)
                    category = Category(
                        name=list_to_add[0],
                        descr=list_to_add[1],
                    )
                    add(category=category)
                    list_to_add = []
                if isinstance(value, list):
                    add_to_category_from_smt(value)


url_dict = get_response()
# def a(l):
#     for i in l:
#         if isinstance(i, dict):
#             for key, value in i.items():
#                 if isinstance(value, list):
#                     a(value)
#
#
# a(url_dict)

add_to_category_from_smt(url_dict)
