# Duotas "users" sąrašas.

# Parašykite dvi funkcijas, kurios:
# * Turės 'docstring' tipo komentarą apie tai, ką jos atlieka.
# * Nekeis sąrašo, priimto kaip argumento, savo viduje.
# * Atliks nurodytas užduotis:

# 1. funkcija "filter_all_or_nothing_people" - kaip argumentą priims "users"
# sąrašą ir duoto sąrašo atveju grąžins sąrašą vartotojų, kurie arba neturi
# naminių gyvūnų visiškai, arba turi ir šunį, ir katę.

# 2. funkcija "filter_underaged_owners" - kaip argumentą priims "users" sąrašą
# ir duoto sąrašo atveju grąžins sąrašą vartotojų, kurie dar nėra pilnamečiai,
# bet turi bent vieną naminį gyvūną.

users = [
    { 'id': '1', 'name': 'John Smith', 'age': 17, 'hasDog': True, 'hasCat': True },
    { 'id': '2', 'name': 'Ann Smith', 'age': 24, 'hasDog': True, 'hasCat': False },
    { 'id': '3', 'name': 'Tom Jones', 'age': 63, 'hasDog': True, 'hasCat': True },
    { 'id': '4', 'name': 'Rose Peterson', 'age': 20, 'hasDog': True, 'hasCat': False },
    { 'id': '5', 'name': 'Alex John', 'age': 25, 'hasDog': False, 'hasCat': False },
    { 'id': '6', 'name': 'Ronald Jones', 'age': 31, 'hasDog': False, 'hasCat': True },
    { 'id': '7', 'name': 'Elton Smith', 'age': 16, 'hasDog': True, 'hasCat': False },
    { 'id': '8', 'name': 'Simon Peterson', 'age': 32, 'hasDog': False, 'hasCat': True },
    { 'id': '9', 'name': 'Daniel Cane', 'age': 15, 'hasDog': False, 'hasCat': False },
]

# 1.
users2 = []

def filter_all_or_nothing_people(sarasas):
    '''
        Funkcija paima paduotą sąrašą ir grąžina sąrašą vartotojų, kurie dar nėra pilnamečiai, bet turi bent vieną naminį gyvūną

        :param sarasas: Paduodamas norimas sąrašas
        :return: Grąžina sąrašą vartotojų, kurie dar nėra pilnamečiai, bet turi bent vieną naminį gyvūną
    '''
    for user in sarasas:
        if ((user['hasDog'] and user['hasCat']) == True) or ((user['hasDog'] or user['hasCat']) == False):
            users2.append(user)
    return users2

print(filter_all_or_nothing_people(users))

# 2.
users3 = []

def filter_underaged_owners(sarasas):
    '''
        Funkcija paima paduotą sąrašą ir grąžina sąrašą vartotojų, kurie arba neturi naminių gyvūnų visiškai, arba turi ir šunį, ir katę

        :param sarasas: Paduodamas norimas sąrašas
        :return: Grąžina sąrašą vartotojų, kurie arba neturi naminių gyvūnų visiškai, arba turi ir šunį, ir katę
    '''
    for user in sarasas:
        if ((user['age'] < 18) and ((user['hasDog'] or user['hasCat']) == True)):
            users3.append(user)
    return users3

print(filter_underaged_owners(users))
