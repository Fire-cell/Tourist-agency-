#Варіант № 13. Структура програми повинна містити наступні класи: туристична агенція, агент, клієнт. +
# Для кожного класу визначити властивості об’єктів. +
# Додати метод, який дозволяє сортувати записи за назвою, агентом, клієнтом. -
# Додати конструктор, який приймає параметри для зміни властивостей під час ініціалізації нового об’єкту класу. +
# Додати деструктор, який видаляє об'єкт класу. -

class TouristAgency():
    def __int__(self, name, address, postcode, telephone):
        self.name = name
        self.address = address
        self.postcode = postcode
        self.telephone = telephone

    #def __del__(self):
    #    print("Об'єкт успішно видалено")

    def Change(self, first, add, post, mobl):
        self.name = first
        self.address = add
        self.postcode = post
        self.mobile = mobl

   #def ClientAgent(self):
    #    print("Клієнт {} його агент {}".format(Client.FullName(), Agent.FullName()))

class Agent(TouristAgency):
    def __init__(self, firstname, surname, age):
        #super().__int__(self, firstname, surname)
        self.firstname = firstname
        self.surname = surname
        self.age = age

    #def __del__(self):
    #    print("Об'єкт успішно видалено")

    def FullName(self):
        return "{} {}".format(self.firstname, self.surname)

    def Change(self, first, sur, age):
        self.firstname = first
        self.surname = sur
        self.age = age


class Client(TouristAgency):
    def __init__(self, firstname, surname, address, postcode, mobile):
        #super().__int__(self, firstname, surname)
        self.firstname = firstname
        self.surname = surname
        self.address = address
        self.postcode = postcode
        self.mobile = mobile

    def __del__(self):
        print("Об'єкт видалено")


    def Email(self):
        return "{}{}@email.com".format(self.firstname, self.surname).lower()

    def FullName(self):
        return "{} {}".format(self.firstname, self.surname)

    def Change(self, first, sur, add, post, mobl):
        self.firstname = first
        self.surname = sur
        self.address = add
        self.postcode = post
        self.mobile = mobl

client1 = Client("Piter", "Griphin", "Elizabeth Bell 86/9", 38901, "+020 4556 3212")
agent1 = Agent("Mark", "Gimpo", 47)

print(client1.Email())
print(client1.FullName())
print(agent1.FullName())

client1.Change("Forest", "Gamp", "Elizabeth Bell 86/9", 38901, "+020 4556 3212")
print(client1.Email())
agent1.Change("Markivaro", "Simp", 49)





#touristagency = TouristAgency("Without Border!","Ferlando 80/21",40651,"+020 7634 1235")
#client2 = Client("John", "Smith", "Elizabeth Bell 90/6", 38901, "+020 4436 1392")
#client3 = Client("Piter", "Griphin", "Elizabeth Bell 86/9", 38901, "+020 4556 3212")
#client4 = Client("Piter", "Griphin", "Elizabeth Bell 86/9", 38901, "+020 4556 3212")
#client5 = Client("Piter", "Griphin", "Elizabeth Bell 86/9", 38901, "+020 4556 3212")
#client6 = Client("Piter", "Griphin", "Elizabeth Bell 86/9", 38901, "+020 4556 3212")
#client7 = Client("Piter", "Griphin", "Elizabeth Bell 86/9", 38901, "+020 4556 3212")
#client8 = Client("Piter", "Griphin", "Elizabeth Bell 86/9", 38901, "+020 4556 3212")
#client9 = Client("Piter", "Griphin", "Elizabeth Bell 86/9", 38901, "+020 4556 3212")