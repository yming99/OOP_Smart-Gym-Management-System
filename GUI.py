from SGMS import SGMS
from tkinter import *

class Interface:
    """
    This class is responsible for creating the GUI for the SGMS system.
    """
    def __init__(self):
        self.sgms = SGMS() #  Create an instance of the SGMS class
    
    def staffDashboard1(self): #function to display staff dashboard
        def memberEquipment():
            mem, count = self.sgms.memberEquip(self.key_entry.get())
            # Create table headers
            header1 = Label(tkw2, text="Member", font=("Arial", 10, "bold"), borderwidth=1, relief="solid", width=20)
            header1.place(x=200, y=100)
            header2 = Label(tkw2, text="Equipment Used", font=("Arial", 10, "bold"), borderwidth=1, relief="solid", width=20)
            header2.place(x=360, y=100)
            # Populate table rows
            for i in range(len(mem)):
                mem_label = Label(tkw2, text=mem[i], borderwidth=1, relief="solid", width=20)
                mem_label.place(x=200, y=130 + i * 30)
                count_label = Label(tkw2, text=count[i], borderwidth=1, relief="solid", width=20)
                count_label.place(x=360, y=130 + i * 30)

        def equipStat(): #show  equipment statistics
            equip, count = self.sgms.equipStat(self.key_entry.get()) #call function from sgms class
            equip_label = Label(tkw2, text=f"Equipment: {equip}, Max Usage: {count}")
            equip_label.place(x=200, y=100)


        tkw2 = Tk() #create new window
        tkw2.title("Staff Dashboard")
        cvs2 = Canvas(tkw2, width=600, height=400, bg="lightblue")
        cvs2.create_text(300, 50, text="Staff Dashboard", font=("Arial", 24), fill="black")
        memEquip_button = Button(tkw2, text="Member Equipment", command=memberEquipment) #create button
        memEquip_button.place(x=50, y=100) #place button
        stat_button = Button(tkw2, text="Equipment Stats", command=equipStat)
        stat_button.place(x=50, y=130)
        
        cvs2.pack()
        tkw2.mainloop()
    def memberDashboard1(self): #member dashboard
        member_name = self.member_entry.get()
        tkw2 = Tk()
        tkw2.title("Member Dashboard")
        cvs2 = Canvas(tkw2, width=600, height=400, bg="lightblue")
        cvs2.create_text(300, 50, text="Member Dashboard", font=("Arial", 24), fill="black")
        def memberProfile(): #member profile
            profile = self.sgms.displayMember(member_name)

            id_label = Label(tkw2, text=f"ID: {profile['id']}")
            id_label.place(x=200, y=100)
            name_label = Label(tkw2, text=f"Name: {profile['name']}")
            name_label.place(x=200, y=130)
            age_label = Label(tkw2, text=f"Age: {profile['age']}")
            age_label.place(x=200, y=160)
            bmi_label = Label(tkw2, text=f"BMI: {profile['bmi']}")
            bmi_label.place(x=200, y=190)
            workout_label = Label(tkw2, text=f"Workout Type: {profile['workoutType']}")
            workout_label.place(x=200, y=220)
            equip_label = Label(tkw2, text=f"Equipment: {profile['equipList']}")
            equip_label.place(x=200, y=250)
            workoutList_label = Label(tkw2, text=f"Workout: {profile['workoutList']}")
            workoutList_label.place(x=200, y=280)

        def newWork(): #  new workout
            new_workout_label = Label(tkw2, text="New Workout:")
            new_workout_label.place(x=200, y=320)
            new_workout_entry = Entry(tkw2)
            new_workout_entry.place(x=300, y=320)

            def addWorkout():
                new_workout = new_workout_entry.get()
                self.sgms.addWorkout(member_name, new_workout)

            add_workout_button = Button(tkw2, text="Add", command=addWorkout)
            add_workout_button.place(x=300, y=350)

        def memberTips(): #  member tips
            tips = self.sgms.tips(member_name)
            tips_label = Label(tkw2, text=f"Tips: {tips}", wraplength=350, justify=LEFT)
            tips_label.place(x=200, y=380)

        def weekWorkout(): #  weekly workout summary
            week_workout = self.sgms.summaryWorkout(member_name)
            week_workout_label = Label(tkw2, text=f"Weekly Workout: {week_workout}", wraplength=350, justify=LEFT)
            week_workout_label.place(x=70, y=380)


        profile_button = Button(tkw2, text="Profile", command=memberProfile)
        profile_button.place(x=50, y=100)
        work_button = Button(tkw2, text="New Workout", command=newWork)
        work_button.place(x=50, y=130)
        tips_button = Button(tkw2, text="Tips", command=memberTips)
        tips_button.place(x=50, y=160)
        week_button = Button(tkw2, text="Weekly Workout", command=weekWorkout)
        week_button.place(x=50, y=190)
        
        cvs2.pack()
        tkw2.mainloop()
    def add_member(self): #  add member
        member_id = self.id_entry.get()
        member_name = self.name_entry.get()
        member_age = self.age_entry.get()
        member_bmi = self.bmi_entry.get()
        member_workout_type = self.type_entry.get()
        key = self.key_entry.get()

        #call register member function
        self.sgms.registerMember(member_id, member_name, member_age, member_bmi, member_workout_type, key)

    def removeMember(self): # remove member
        member_name = self.name_entry.get()
        if member_name:
            self.sgms.removeMember(member_name)
            self.name_entry.delete(0, END)
            print(f"Member {member_name} removed successfully!")
        else:
            print("Please enter a valid name to remove.")

    def addEquip(self): # add equipment
        id = self.eid_entry.get()
        name = self.ename_entry.get()
        quant = self.quant_entry.get()
        key = self.key_entry.get()
        self.sgms.addEquip(id, name, quant, key)

    def useEquip(self):  #  use equipment
        name = self.ename_entry.get()
        key = self.key_entry.get()
        self.sgms.useEquip(name, key)

    def returnEquip(self): #  return equipment
        name = self.ename_entry.get()
        key = self.key_entry.get()
        self.sgms.endEquip(name, key)

    def memberUI(self): # member information on main menu
        self.id_label = Label(self.tkw, text="ID:")
        self.id_label.place(x=50, y=150)
        self.id_entry = Entry(self.tkw)
        self.id_entry.place(x=150, y=150)

        self.name_label = Label(self.tkw, text="Name:")
        self.name_label.place(x=50, y=180)
        self.name_entry = Entry(self.tkw)
        self.name_entry.place(x=150, y=180)

        self.age_label = Label(self.tkw, text="Age:")
        self.age_label.place(x=50, y=210)
        self.age_entry = Entry(self.tkw)
        self.age_entry.place(x=150, y=210)

        self.bmi_label = Label(self.tkw, text="BMI:")
        self.bmi_label.place(x=50, y=240)
        self.bmi_entry = Entry(self.tkw)
        self.bmi_entry.place(x=150, y=240)

        self.type_label = Label(self.tkw, text="Workout Type:")
        self.type_label.place(x=50, y=270)
        self.type_entry = Entry(self.tkw)
        self.type_entry.place(x=150, y=270)

        self.add_button = Button(self.tkw, text="Add Member", command=self.add_member)
        self.add_button.place(x=70, y=300)
        self.remove_button = Button(self.tkw, text="Remove Member", command=self.removeMember)
        self.remove_button.place(x=160, y=300)

    def equipUI(self): #equipment info on main menu
        self.eid_label = Label(self.tkw, text="ID:")
        self.eid_label.place(x=650, y=150)
        self.eid_entry = Entry(self.tkw)
        self.eid_entry.place(x=750, y=150)

        self.ename_label = Label(self.tkw, text="Name:")
        self.ename_label.place(x=650, y=180)
        self.ename_entry = Entry(self.tkw)
        self.ename_entry.place(x=750, y=180)

        self.quant_label = Label(self.tkw, text="Quantity:")
        self.quant_label.place(x=650, y=210)
        self.quant_entry = Entry(self.tkw)
        self.quant_entry.place(x=750, y=210)

        self.add_button = Button(self.tkw, text="Use Equipment", command=self.useEquip)
        self.add_button.place(x=670, y=300)
        self.remove_button = Button(self.tkw, text="Return Equipment", command=self.returnEquip)
        self.remove_button.place(x=770, y=300)
        self.get_button = Button(self.tkw, text="Add Equipment", command=self.addEquip)
        self.get_button.place(x=720, y=340)

    def memberDashboard(self): #direct to member dashboard
        self.member_label = Label(self.tkw, text="Name:")
        self.member_label.place(x=370, y=160)
        self.member_entry = Entry(self.tkw)
        self.member_entry.place(x=430, y=160)
        self.member_button = Button(self.tkw, text="Member Dashboard", command=self.memberDashboard1)
        self.member_button.place(x=425, y=200)

    def staffDashboard(self): #direct staff Dashboard
        self.member_button = Button(self.tkw, text="Staff Dashboard", command=self.staffDashboard1)
        self.member_button.place(x=425, y=240)
    def main(self):
        self.tkw = Tk() #main window
        self.tkw.title("Fitness Centre System")
        cvs = Canvas(self.tkw, width=1000, height=400, bg="lightblue")

        cvs.create_text(500, 50, text="Fitness Centre System", font=("Arial", 24), fill="black")
        cvs.create_text(150, 120, text="Member Info", font=("Arial", 12), fill="black")
        cvs.create_text(750, 120, text="Equip Info", font=("Arial", 12), fill="black")

        self.key_label = Label(self.tkw, text="Key:")
        self.key_label.place(x=400, y=100)
        self.key_entry = Entry(self.tkw)
        self.key_entry.place(x=450, y=100)

        #call other functions for main menu
        self.memberUI()
        self.equipUI()
        self.memberDashboard()
        self.staffDashboard()
        
        cvs.pack()
        self.tkw.mainloop()


ms = Interface()
ms.main()