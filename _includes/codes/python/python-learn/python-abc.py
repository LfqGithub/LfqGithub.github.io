import abc
import six

@six.add_metaclass(abc.ABCMeta) # for python2/3 compatibility
class Animal(object):
    @abc.abstractmethod
    def talk(self):
        pass
class People(Animal):
    def talk(self):
        print('say hello')
class Dog(Animal):
    def talk(self):
        print('say wangwang')
class Pig(Animal):
    def talk(self):
        print('say aoao')

pig1=Pig()
pig1.talk()

