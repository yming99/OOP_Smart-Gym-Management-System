from Member import Member
from Staff import Staff
from Equipment import Equipment
from datetime import datetime as dt
from datetime import timedelta

today_date = dt.today().date().strftime('%Y-%m-%d')

class SGMS:
    def __init__(self):
        #initialize member list
        self.members = [
            Member(1, 'John', 20, 18.5, 'Cycling',None, {today_date: 'Cycling'}),
            Member(2, 'Jane', 21, 19.5, 'Swimming', 'Dumb bell'),
            Member(3, 'Jim', 22, 20.5, 'Running'),
            Member(4, 'Joe', 23, 21.5, 'Yoga', 'Yoga Mat'),
            Member(5, 'Jill', 24, 22.5, 'Weight Lifting')
        ]
        #initialize equipments list
        self.equipments = [
            Equipment(1, 'Bike', 10, 5),
            Equipment(2, 'Dumbbell', 20, 10),
            Equipment(3, 'Swimsuit', 30, 15),
            Equipment(4, 'Yoga Mat', 40, 20),
            Equipment(5, 'Weight Lifting Gloves', 50, 25)
        ]
        #initialize staff with key
        self.staff = Staff(1, 'Admin')

    #  register member by staff
    def registerMember(self, id, name, age, bmi, workoutType, key):
        if self.staff.checkKey(key):
            member = Member(id, name, age, bmi, workoutType) #create member object
            self.members.append(member) #add member to list
            print(self.members[-1].getDetails())
            return print('Member registered successfully')
        else:
            return print('Invalid key')
    
    #display member details
    def displayMember(self, name):
        for member in self.members: #loop through membersList
            if member.get_name() == name: #check if member name matches
                return member.getDetails()
    
    #remove member
    def removeMember(self, name):
        for member in self.members:
            if member.get_name() == name:
                self.members.remove(member)
                return print('Member removed successfully')
            else:
                return print('Member not found')

    #add workout by members
    def addWorkout(self, name, workout):
        for member in self.members:
            if member.get_name() == name:
                member.addWorkout({today_date: workout})
                return print('Workout added successfully')
            else:
                return print('Member not found')
    
    #fitness tips for members
    def tips(self, name):
        for member in self.members:
            if member.get_name() == name:
                bmi = member.getBMI() #based on BMI
                if bmi < 18.5:
                    print('You need to gain weight')
                    return 'You need to gain weight'
                elif bmi > 24.9:
                    print('You need to lose weight')
                    return 'You need to lose weight'
                else:
                    print('You are within a healthy range')
                    return 'You are within a healthy range'
            else:
                print('Member not found')
                return 'Member not found'
    
    #  Summary workout
    def summaryWorkout(self, name):
        for member in self.members:
            if member.get_name() == name:
                #find last 7 days workouts
                seven_days_ago = dt.today().date() - timedelta(days=7)

                count = 0
                for entry in member.workoutList:
                    for date_str in entry:
                        date_obj = dt.strptime(date_str, '%Y-%m-%d').date()
                        if seven_days_ago <= date_obj <= dt.today().date():
                            count += 1 #save count for workout
                print(f"Workouts from the last 7 days: {count}")
                return count
    
    # add equipment by staff to equipment data
    def addEquip(self, id, name, quant, key):
        if self.staff.checkKey(key): #check key
            equip = Equipment(id, name, int(quant)) #create equipment object
            self.equipments.append(equip)
            return print(self.equipments[-1].getDetails())
        else:
            return print('Invalid key')
    
    #member uses equipment
    def useEquip(self, name, key):
        if self.staff.checkKey(key):
            for i in self.equipments:
                if i.equipName == name:
                    i.startUse()
                    return print(i.getDetails())
            return print('Equipment not found')
    
    #member ends using equipment
    def endEquip(self, name, key):
        if self.staff.checkKey(key):
            for i in self.equipments:
                if i.equipName == name:
                    i.endUse()
                    return print(i.getDetails())
            return print('Equipment not found')
    
    #get equipment used by all members
    def memberEquip(self, key):
        member_equipment = []
        equipment_count = []

        if self.staff.checkKey(key):
            for member in self.members:
                if hasattr(member, 'equip') and member.equip:
                    member_equipment.append(member.get_name())
                    equipment_count.append(member.equip)
                    print(f"Member: {member.get_name()}, Equipment used: {member.equip}")
            return member_equipment, equipment_count #return member name and equipment used
        else:
            print('Invalid key')
            return member_equipment, equipment_count

    #get equipment statistics
    def equipStat(self, key):
        max = 0
        equipment = ''
        if self.staff.checkKey(key):
            for equip in self.equipments:
                if equip.getCount() > max: #find max of count
                    max = equip.getCount()
                    equipment = equip.equipName
                    
        print(f"Equipment with maximum usage: {equipment}, {max} times")
        return equipment, max