
my_dict = {}

# update(використовується для оновлення словника, додаючи нові  значення)
my_dict.update({"a": 1, "b": 2})
print("update():", my_dict)

# del (використовується для видалення елемента зі словника за його ключем.)
del my_dict["a"]
print("del 'a':", my_dict)

# clear(використовується для видалення всіх елементів із словника, роблячи його порожнім.)
my_dict.clear()
print("clear():", my_dict)

# keys(повертає список ключів (ідентифікаторів) із словика)
my_dict = {"name": "Susan", "age": 69, "city": "WHRcity"}
print("keys():", my_dict.keys())

# values(повертає список значень, що відповідають ключам у словнику.)
print("values():", my_dict.values())

# items( повертає список кортежів, які представляють пари значен. у словнику.)
print("items():", my_dict.items())
