def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return " Error: Cannot divide by zero."
    return a / b

def calculator():
    print("Welcome to the basic calculator")

    while True :
          print("\nSelect Operation:")
          print("1. Addition (+)")
          print("2. Subtraction (-)")
          print("3. Multiplication (*)")
          print("4. Division (/)")
          print("5. Exit")

          choice=int(input("Enter Choice(1-5): "))
          if choice==5:
              print("Thanks")
              break
          
          if choice is not ['1','2','3','4']:
              print("Enter Valid Choice")

          try:
              a = int(input("Enter First no: "))
              b = int(input("Enter Second no: "))

          except ValueError:
              print("Invalid Input")

          if choice ==1:
              result =add(a,b)
          elif choice == 2:
              result = subtract(a,b)
          elif choice ==3:
              result = multiply(a,b)
          elif choice == 4:
              result =divide(a,b)
          print(f"Result:{result}")
calculator()
