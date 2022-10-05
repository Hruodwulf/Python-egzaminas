# Sukurkite filmų klasę "Movie", kuri:
# * Turės klasės lygio 'docstring' tipo komentarą, trumpai aprašantį, kas tai
#   per klasė.
# * Turės 'docstring' tipo komentarą prie kiekvieno metodo, trumpai aprašantį,
#   ką tas metodas atlieka.
# * Gebės sukurti objektus su 3 savybėmis ir 1 metodu.

# Naudojant šią klasę sukurkite bent du skirtingus filmų objektus.

# Savybės:
# * title (str)
# * director (str)
# * budget (int)

# Metodas:
# * was_expensive() - jeigu filmo "budget" yra daugiau nei 100 mln. USD,
#   grąžins True, kitu atveju - False.

class Movie:
    '''
    Klasė aprašanti filmo duomenis, leiežia sukurti filmo objektą naudojant šias sąvybes

    :param title: Filmo pavadinimas
    :param director: Filmo režisierius
    :param budget: Filmo biudžetas
  '''
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget


    '''
     Metodas palygina sąlygos duomenis su vartotojo sukurto objekto įvestais duomenimis, šiuo atveju, biudžetu,
     ir grąžina atsakymą True arba False, priklausomai ar filmo biudžetas didenis nei sąlygos

    :return: Boolean - Ture arba False reikšmę
    '''
    def was_expensive(self):
        return self.budget > 100000000

filmas1 = Movie('Titanic', 'James Cameron', 200000000)
filmas2 = Movie("Mr. Bean's Holiday", 'Steve Bendelack', 25000000)

print(filmas1.was_expensive())
print(filmas2.was_expensive())
