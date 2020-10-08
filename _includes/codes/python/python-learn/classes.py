from math import pi


class Person:
    role='person'
    def __init__(self,name,aggressivity,life_value,money):
        self.name=name
        self.aggressivity=aggressivity
        self.life_value=life_value
        self.money=money
    def walk(self):
        print("person is walking...")
    def attack(self, dog):
        dog.life_value-=self.aggressivity
class Dog:
    role='dog'
    def __init__(self,name,breed,aggressivity,life_value):
        self.name=name
        self.breed=breed
        self.aggressivity=aggressivity
        self.life_value=life_value
    def bite(self, people):
        people.life_value-=self.aggressivity
class Weapon:
    def __init__(self,name,price,aggrev,life_value):
        self.name=name
        self.price=price
        self.aggrev=aggrev
        self.life_value=life_value
    def update(self,obj):
        obj.money-=self.price
        obj.aggressivity+=self.aggrev
        obj.life_value+=self.life_value
    def prick(self,obj):
        obj.life_value-=500
class Circle:
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return pi*self.radius**2
    def perimeter(self):
        return 2*pi*self.radius
class Ring:
    def __init__(self,radius_outside,radius_inside):
        self.inside_circle=Circle(radius_inside)
        self.outside_circle=Circle(radius_outside)
    def area(self):
        return self.outside_circle.area()-self.inside_circle.area()
    def perimeter(self):
        return self.outside_circle.perimeter()+self.inside_circle.perimeter()

lance=Weapon('spear',200,6,100)
egg=Person('egon',10,1000,600)
ha2=Dog('erlengzi','hashiqi',10,1000)
print('person walk: ',Person.walk)
if egg.money>lance.price:
    lance.update(egg)
    egg.weapon=lance
print(egg.money,egg.life_value,egg.aggressivity)
print(ha2.life_value)
egg.attack(ha2)
print(ha2.life_value)
egg.weapon.prick(ha2)
print(ha2.life_value)

# test ring/circle class 
# 组合的关系建立类之间的联系，是一种“有”的关系，比如环中有圆
ring_tem=Ring(10,5)
print(ring_tem.perimeter())
print(ring_tem.area())

