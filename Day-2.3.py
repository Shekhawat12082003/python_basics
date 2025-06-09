import random
import string

def password_generator(length):
    if length<4 :
        print("Password must be equal to greater then 4")
    all_char = string.ascii_letters+string.digits+string.punctuation

    password = ''.join(random.choices(all_char,k=length))
    return password

def password_app():
    print ("Welcome in password generator app")

    while True :
        choice = input("Enter lenghth of password(or exit): ")
        try:
          if choice.lower() == "exit":
            print("Bye")
            break 

          length =int(choice)
          print(f"Password: {password_generator(length)}")
        except (ValueError): 
            print("Enter valid no") 

password_app()