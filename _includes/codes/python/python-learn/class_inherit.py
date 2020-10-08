
class Animal:
    def __init__(self,name,aggressivity,life_value):
        self.name=name
        self.aggressivity=aggressivity
        self.life_value=life_value
    def eat(self):
        print('%s is eating' % self.name)
class Dog(Animal):
    def __init__(self,name,aggressivity,life_value,breed):
        super().__init__(name,aggressivity,life_value)
        self.breed=breed
    def bite(self,people):
        people.life_value-=self.aggressivity
    def eat(self):
        super().eat()
        print('eat from dog')
class Person(Animal):
    def __init__(self,name,aggressivity,life_value,money):
        super().__init__(name,aggressivity,life_value)
        self.money=money
    def attack(self,dog):
        dog.life_value-=self.aggressivity
    def eat(self):
        super().eat()
        print('eat from person')
# 继承，是一种“是”的概念，人/狗是动物
egg=Person('egon',10,100,1000)
ha2=Dog('erlengzi','hashiqi',10,1000)
print(egg.name)
print(ha2.name)
egg.eat()
