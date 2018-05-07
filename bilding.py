class Bilding():
    def __init__(self, w, c, n=0):
        self.what = w
        self.color = c
        self.numbers = n
        self.mwhere(n)

    def mwhere(self, n):
        if n == 0:
            self.where = "отсутствуют на складе"
        elif 0 < n < 100:
            self.where = "малый склад"
        else:
            self.where = "основной склад"

    def plus(self, p):
        self.numbers = self.numbers + p
        self.mwhere(self.numbers)

    def minus(self, m):
        self.numbers = self.numbers - m
        self.mwhere(self.numbers)

obj1 = Bilding("Доски", "лакированные", 100)
obj2 = Bilding("Кирпичи", "красные", 1000)
obj3 = Bilding("Обои", "оранжевые", 0)

print(obj1.what, obj1.color, obj1.where)
print(obj2.what, obj2.color, obj2.where)
print(obj3.what, obj3.color, obj3.where)

obj1.plus(100)
obj2.minus(900)

print(obj1.what, obj1.numbers, obj1.where)
print(obj2.what, obj2.numbers, obj2.where)