class Patient:  #base class
    pat_count=0
    def __init__(self,name,email): #default constructor
          self.name=name
          self.email=email
          Patient.pat_count+=1
    def DisplayDetails(self):
        print("Name: ",self.name,"Email: ",self.email)
    def DispCount(self):
        print("Total count of patients: ",Patient.pat_count)

class Doctor(Patient):#Inheritance Usage
    def __init__(self,Doc_name,email,Doctor_id): #default init constructor
        Patient.__init__(self,Doc_name,email)
        self.Doctor_id=Doctor_id
    def DisplayDetails(self):
        Patient.DisplayDetails(self)
        print("Doctor_ID: ",self.Doctor_id)

class Clerk(Doctor): #inheritance
    def __init__(self,name,email,emp_id,Doc_name,d_email,Doctor_id,time,date): #default Init constructor
        super().__init__(name,email,Doctor_id)   #usage of super call
        self.emp_id=emp_id
        self.name=name
        self.email=email
        self.dname=Doc_name
        self.demail=d_email
        self.did=Doctor_id
        self.time=time
        self.date=date
    def DisplayDetails(self):
        Patient.DisplayDetails(self)
        print("Emp ID:", self.emp_id)
        print("The aappointment time is: ",self.time)
        print("The appointment date is: ",self.date)


class Book():
    def __init__(self,pat_name,blood_pressure, sugar_level): #default init constructor
        self.patient_name=pat_name
        self.blood=blood_pressure
        self.sugar=sugar_level
    def DisplayDetaails(self):
        print("Patient_name: ",self.patient_name,"Blood pressure: ",self.blood,"Sugar level: ",self.sugar)

class Nurse(Patient,Book): #multiple Inheritance
    def __init__(self,name,email,pat_name,blood_pressure,sugar_level): #default init constructor
        # super().__init__(name,email)
        Patient.__init__(self,name,email)
        Book.__init__(self,pat_name,blood_pressure, sugar_level)

    def DisplayDetails(self):
        Book.DisplayDetaails(self)
        Patient.DisplayDetails(self)


#creation of instances for above classes

patient1=Patient('Akhila','akhila.atluri@gmail.com')
patient2=Patient('Kamal','kamaltej@gmail.com')
Doctor1=Doctor('Harish','harishc88@gmail.com','16262845')
Doctor2=Doctor('vinay','vinaymaturi@gmail.com','1645458')
Book1=Book('Akhila','180/60','normal')
Book2=Book('Kamal','140/50','normal')
print("##Patient Count##")
Patient.DispCount(Patient)

#nurse attending patients
Nurse1=Nurse('akhila atluri','akhila.atluri@gmail.com','Akhila','180/60', 'normal')
Nurse2=Nurse('kamal tej','kamtej@gmail.com','kamal','110/50','normal')

print("###Doctor Details###")
Doctor1.DisplayDetails();
Doctor2.DisplayDetails();

print("##Patient Details##")
patient1.DisplayDetails();
patient2.DisplayDetails();

print("##Book Details##")
Book1.DisplayDetaails();
Book2.DisplayDetaails();

print("#Nurse attending patient details")
Nurse1.DisplayDetaails();


clerk1=Clerk("rahul","rahu2g@gmail.com","162625252","Dr Harish","harishjoshi@gmail.com","12345","9 40 PM","16 JUNE")
print("clerk Issuing Appointments")
clerk1.DisplayDetails()

clerk2=Clerk("kunal","kunakrathod@gmail.com","990909876","Dr kavya","kavyajoshi@gmail.com","898976","8 00 AM","21 JUNE")
print("clerk Issuing Appointments")
clerk2.DisplayDetails()