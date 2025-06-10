def encontrar(heroes, heroe, i=0):
   if i >= len(heroes):
      return print("no se encontro al Cap")
   elif heroes[i] == heroe:
      return print("Se encontro al Cap")
   else:
      return encontrar(heroes, heroe, i+1)
   
def listar(heroes, i=0):
   if i < len(heroes):
      return print(heroes[i]), listar(heroes, i+1)

supers = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Spider-Man",
    "Iron Man",
    "Capitan America",
    "Thor",
    "Hulk",
    "Black Panther",
    "Flash",
    "Green Lantern",
    "Aquaman",
    "Doctor Strange",
    "Wolverine",
    "Deadpool"
]

superheroe = "Capitan America"

print(encontrar(supers, superheroe))