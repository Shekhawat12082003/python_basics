class student:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks 

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

    def total_marks(self):
        return sum(self.marks)
    
    def average_marks(self):
        return sum(self.marks)/len(self.marks)
    
def create_student():
    name = input("Enter name of student: ")

    try:
        num_sub= int(input("Enter the total no of subject: "))
    except ValueError:
        print("Enter valid value")
    marks =[]
    for i in range (num_sub):
        try:
            mark = float(input(f"Enter marks for subject {i+1}: "))
            marks.append(mark)
        except ValueError:
            print("⚠️ Invalid input. Enter numbers only.")
            return None

    return student(name, marks)

students = []

while True:
    choice = input("\nDo you want to add a student? (yes/no): ").lower()
    
    if choice == "yes":
        student = create_student()
        if student:
            students.append(student)
    elif choice == "no":
        break
    else:
        print("❌ Please type 'yes' or 'no'.")

print("\nStudent Report Summary:")
for s in students:
    s.display_info()
    print(f"Total: {s.total_marks()}")
    print(f"Average: {s.average_marks():.2f}")
    