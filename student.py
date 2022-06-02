# Add these methods to class student - full_name, year_of_birth, initials. Create two instances and verify the work as expected


class Information:
    school="Akirachix"
    def __init__(self,first_name,second_name,age,country):
        self.first_name=first_name
        self.second_name=second_name
        self.country=country
        self.age=age
        self.country=country

    def fullnames(self):
        fullname= f"{self.first_name} {self.second_name}"
        return fullname

    def initials(self):
        intial=f"{self.first_name[0]},{self.second_name[0]}"
        return intial

    def year(self):
        user=int(input("Enter current year \n "))
        year_of_birth=user-self.age
        return year_of_birth

    def greet(self):
        return f"Hello there {self.first_name} {self.second_name} from {self.country} welcome to {self.school} and your year of birth is {self.age}" 
    
