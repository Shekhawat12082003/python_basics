class employee:
    def __init__(self,name,emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Id: {self.emp_id}")

class manager(employee):
    def __init__(self, name, emp_id,department):
        super().__init__(name, emp_id)    
        self.department = department

    def display_manager_info(self):
        self.display_info()
        print(f"Department: {self.department}")

class Developer(employee):
    def __init__(self, name, emp_id, programming_language):
        super().__init__(name, emp_id)
        self.language = programming_language

    def display_developer_info(self):
        self.display_info()
        print(f"Programming Language: {self.language}")

manager1 = manager("Amit Sharma", 101, "HR")
dev1 = Developer("Priya Mehta", 102, "Python")

print("\n Manager Details:")
manager1.display_manager_info()

print("\n Developer Details:")
dev1.display_developer_info()