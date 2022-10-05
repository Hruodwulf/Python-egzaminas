import pprint
from functools import reduce

# Duotas "users" sąrašas.

# Parašykite dvi funkcijas, kurios:
# * Turės 'docstring' tipo komentarą apie tai, ką jos atlieka.
# * Nekeis sąrašo, priimto kaip argumento, savo viduje.
# * Atliks nurodytas užduotis:

# 1. funkcija "get_user_average_age" - kaip argumentą priims "users" sąrašą ir
# duoto sąrašo atveju grąžins visų vartotojų amžiaus vidurkį kaip skaičių,
# suapvalintą iki artimiausio sveikojo skaičiaus.

# 2. funkcija "get_users_names" - kaip argumentą priims sąrašą ir duoto sąrašo
# atveju grąžins sąrašą su visų vartotojų vardais, išrikiuotais abėcėlės tvarka,
# pvz. ['Alex John', 'Ann Smith', ...].

users = [
  { 'id': '1', 'name': 'John Smith', 'age': 20 },
  { 'id': '2', 'name': 'Ann Smith', 'age': 24 },
  { 'id': '3', 'name': 'Tom Jones', 'age': 31 },
  { 'id': '4', 'name': 'Rose Peterson', 'age': 17 },
  { 'id': '5', 'name': 'Alex John', 'age': 25 },
  { 'id': '6', 'name': 'Ronald Jones', 'age': 63 },
  { 'id': '7', 'name': 'Elton Smith', 'age': 16 },
  { 'id': '8', 'name': 'Simon Peterson', 'age': 30 },
  { 'id': '9', 'name': 'Daniel Cane', 'age': 51 },
]


# 1.
arr = []
def get_user_average_age(sarasas):
  '''
    Funkcija priima paduotą saraša ir grąžina visų vartotojų amžiaus vidurkį kaip skaičių, suapvalintą iki artimiausio sveikojo skaičiaus

    :param sarasas: Paduodamas norimas sąrašas
    :return: Gražina visų vartotojų amžiaus vidurkį kaip skaičių, suapvalintą iki artimiausio sveikojo skaičiaus
  '''
  for user in sarasas:
    arr.append(user['age'])
  arr2 = round(reduce(lambda x, y: x + y, arr) / len(sarasas))
  return arr2

print(get_user_average_age(users))

# 2.
names = []
def get_users_names(sarasas):
  '''
    Funkcija priima paduotą saraša ir grąžina sąrašą su visų vartotojų vardais, išrikiuotais abėcėlės tvarka

    :param sarasas: Paduodamas norimas sąrašas
    :return: Grąžina sąrašą su visų vartotojų vardais, išrikiuotais abėcėlės tvarka
  '''
  for user in sarasas:
    names.append(user['name'])
  sorted_names = pprint.pprint(sorted(names))
  return sorted_names

get_users_names(users)


