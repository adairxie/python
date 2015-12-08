class PrivateExc(Exception):
    print('you have changed priate variable');

class Privacy:
    def __setaddr__(self, attrname,value):
        if attrname in self.private:
            raise PrivateExc(attrname,self)
        else:
            self.__dict__[attrname] =value
class Test1(PrivateExc):
   privates=['age']

class Test2(PrivateExc):
     privates=['name','pay']
     def __init__(self):
        self.__dict__['name']='Tom'
