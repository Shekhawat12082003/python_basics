class student :
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks 

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

    def total_marks(self):
        return sum(self.marks)
    
    def average(self):
        return sum(self.marks)/len(self.marks)
    
student1 = student("Gagandeep",[85,90,94])
student1.display()

print("Total:", student1.total_marks())
print("Average:", student1.average())