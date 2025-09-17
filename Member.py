from Person import Person

class Member(Person):

    def __init__(self, id, name, age, bmi, workoutType, equip=None, workout=None):
        self.equipList = []
        self.workoutList = []

        #member attributes
        super().__init__(id, name)
        self.__age = age
        self.__bmi = bmi
        self.__workoutType = workoutType
        self.equip = equip
        self.workout = workout
        self.workoutList.append(workout)

    def getAge(self): # age getter method
        return self.__age
    
    def getBMI(self): #  bmi getter method
        return self.__bmi
    
    def setBMI(self, bmi): #  bmi setter method
        self.__bmi = bmi

    def getType(self): #  workout type getter method
        return self.__workoutType
    
    def setType(self, workoutType): #  workout type setter method
        self.__workoutType = workoutType

    def  getEquip(self): # equipment getter method
        return self.equipList
    
    def addEquip(self, equip): #  equipment setter method
        self.equipList.append(equip)

    def getWorkout(self): # return workout list
        return self.workoutList
    
    def addWorkout(self, workout): #  add workout
        self.workoutList.append(workout)

    def getDetails(self): #  return member details
        self.id, self.name = super().getDetails()
        print("ID: ", self.id)
        print("Name: ", self.name)
        print("Age: ", self.__age)
        print("BMI: ", self.__bmi)
        print("Workout Type: ", self.__workoutType)
        print("Equipment: ", self.equipList)
        print("Workout History: ", self.workoutList)

        return {
            "id": self.id,
            "name": self.name,
            "age": self.__age,
            "bmi": self.__bmi,
            "workoutType": self.__workoutType,
            "equipList": self.equipList,
            "workoutList": self.workoutList
        }