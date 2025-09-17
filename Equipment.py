#Equipment
class Equipment:
    def __init__(self, id, name, quant, count=0):
        #Attributes
        self.equipId = id
        self.equipName = name
        self.__equipQuant = quant #available quantity
        self.__equipCount = count #number of borrowed

    #Member borrow equipment
    def startUse(self):
        self.__equipQuant -= 1
        self.__equipCount += 1 
    
    def endUse(self): #return of equipment
        self.__equipQuant += 1

    def getQuant(self): #__equipQuant getter
        return self.__equipQuant
    
    def getCount(self): #__equipCount getter
        return self.__equipCount
    
    def getDetails(self): #getting all details
        return self.equipId, self.equipName, self.__equipQuant, self.__equipCount

    