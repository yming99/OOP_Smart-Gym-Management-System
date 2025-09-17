from Person import Person

class Staff(Person): #staff class (inherits from Person)

    def __init__(self, id, name, key=None):
        super().__init__(id, name) #calls parent class constructor
        self.__key = 'admin' #default key

    def checkKey(self, key):   ##checks if key is valid
        if self.__key == key:
            return True
        else:
            return False