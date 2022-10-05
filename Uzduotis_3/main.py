# Duotas "audi" žodynas.

# Parašykite funkciją "get_dict_values", kuri:
# * Turės 'docstring' tipo komentarą apie tai, ką ji atlieka.
# * Nekeis žodyno, priimto kaip argumento, savo viduje.
# * Kaip argumentą priims žodyną ir grąžins sąrašą su visomis jo reikšmėmis (values).

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

def get_dict_values(sarasas):
  '''
     Funkcija priima paduotą žodyną ir grąžina sąrašą su visomis jo reikšmėmis

    :param sarasas: Paduodamas norimas sąrašas
    :return: Grąžina sąrašą su visomis jo reikšmėmis
  '''
  return list(sarasas.values())

print(get_dict_values(audi))
