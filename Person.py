class Person:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    #id getter
    def get_id(self):
        return self.__id
    
    #id setter
    def get_name(self):
        return self.__name
        
    #name setter
    def set_name(self, name):
        self.__name = name

    #return details (id and name)
    def getDetails(self):
        return self.__id, self.__name