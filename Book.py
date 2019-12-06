class Book:
    # ceci est le constructeur
    def __init__(self,isbn,title,author,publisher):
        self.isbn=isbn
        self.title=title
        self.author=author
        self.publisher=publisher

    def __eq__(self, b):
         if self.isbn==b.isbn:
            return True
         else:
             return False

    def __hash__(self):
        return hash(self.isbn)

    def __lt__(self, other):
         if self.isbn < other.isbn:
             return True
         else :
             return False

    def __gt__(self, other):
        if self.isbn > other.isbn:
            return True
        else:
            return False

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.isbn,self.title,self.author,self.publisher)





LePetitPrince= Book(1234,"LePetit Prince","Antoinde de Saint Exupery","Gallimard")#“
#ici on construit un objet dont le nom est LePetitPrince"
animalFarm=Book(1611,"Animal Farm","Georges Orwell","Penguin")

if LePetitPrince == animalFarm: # ici le signe == renvoi a la methode __eq__ de la ligne 9
    print("c est le meme livre")
else:
    print("ils sont differents")
print("===========")

print(LePetitPrince.title)
print(type(LePetitPrince))
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print(LePetitPrince)
print("@@@@@@@@@@@@@AAAAA@@@@@@@@@@@@@")

monLivrePrefere = str(LePetitPrince)
print(monLivrePrefere)
# maintenant on cree un Ensemble de nom Livre
germinal = Book(1255,"germinal","zola","nathan")
etranger = Book(7567,"etranger","camus","Gallimard")

Germinal=str(germinal)
Etranger=str(etranger)

Livre=[]
Livre.append(Germinal)
Livre.append(Etranger)
print(Livre)


