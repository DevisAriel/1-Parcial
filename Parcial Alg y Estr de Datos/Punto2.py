from Supers import superheroes, is_villian
from Lista import List
from Cola import Queue

def orden_por_nombre(item):
    return item.name

def orden_por_nombre_real(item):
    return item.name

def orden_por_villano(item):
    if is_villian == True:    
        return item.is_villain

def orden_por_fecha_de_aparicion(item):
    return item.first_appearance

class Superhero:
    
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain
        self.movies = List()
        self.movies.add_criterion('name', orden_por_nombre)
        self.movies.add_criterion('year', orden_por_nombre)

    def __str__(self):
        return f"{self.name}, {self.real_name} - {self.is_villain}"
    

lista_superheroes = List()
lista_superheroes.add_criterion('name', orden_por_nombre)
print(sorted(lista_superheroes))

print(lista_superheroes.index('The Thing', 'name'))
print(lista_superheroes.index('Rocket Raccoon', 'name'))

lista_superheroes.add_criterion('is_villain', orden_por_villano)
print(lista_superheroes)

cola_de_villanos = Queue()


lista_superheroes.add_criterion('real_name', orden_por_nombre_real)
print(sorted(lista_superheroes))
lista_superheroes.add_criterion('first_appearance', orden_por_fecha_de_aparicion)
print(sorted(lista_superheroes))

for superhero in superheroes:
    hero = Superhero(
        name=superhero["name"],
        alias=superhero["alias"],
        real_name=superhero["real_name"],
        short_bio=superhero["short_bio"],
        first_appearance=superhero["first_appearance"],
        is_villain=superhero["is_villain"],
    )
    lista_superheroes.append(hero)

for superhero in lista_superheroes:
    if superhero.name.startswith(('Bl', 'My', 'W', 'G')):
        print(superhero)

for superhero in lista_superheroes:
    if superhero.short_bio(('time-traveling', 'suit')):
        print(superhero)

posicion = lista_superheroes.index('Electro', 'name')
print(lista_superheroes[posicion])
print(lista_superheroes.delete_value('Electro', 'name'))
posicion = lista_superheroes.index('Baron Zemo', 'name')
print(lista_superheroes[posicion])
print(lista_superheroes.delete_value('Baron Zemo', 'name'))

posicion = lista_superheroes.index('Ant Man', 'name')
lista_superheroes[posicion] = 'Scott Lang'
print(lista_superheroes[posicion])

