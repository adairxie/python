#Add method to encapsulate operations for maintainability

from classtools import AttrDisplay
class Person(AttrDisplay):
    def __init__(self,name,job=None,pay=0):
        self.name = name
        self.job=job
        self.pay=pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay =int(self.pay * (1+percent ))

class Manager(Person):
    def __init__(self,name,pay):                #Redefine constructor
        Person.__init__(self,name,'mgr',pay)    #Run original with 'mgr'
    def giveRaise(self,percent,bonus=.10):
        Person.giveRaise(self,percent+bonus)  #Call Person's version

class Department:
    def __init__(self,*args):
        self.members = list(args)
    def addMember(self,person):
        self.members.append(person)
    def giveRaise(self,percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)
             
if __name__ == '__main__':
    bob=Person('Bob Smith')
    sue=Person('Sue Jones',job='dev',pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(),sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom=Manager('Tom Jones',50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
    print('--All Three--')
    for object in(bob,sue,tom):
        object.giveRaise(.10)
        print(object)
    print(tom.__dict__)


