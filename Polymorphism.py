# Parent Class
class  User:
    name = "Bill"
    email = "bill@aol.com"
    phone = "321-456-7544"
    password = "abcde1234"

    def getLoginInfo(self):
        entry_name = input("Enter your name:  ")
        entry_email = input("Enter your email: ")
        entry_phone = input("Enter your Phone Number: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#Child Class Employee
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"


    def getLoginInfo(self):
        entry_name = input("Enter your name:  ")
        entry_email = input("Enter your email: ")
        entry_phone = input("Enter your Phone Number: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect.")

#Child Class Employee
class Manager(User):
    position = "Senior"
    department = "Operations"
    manager_password = "special_level"


    def getLoginInfo(self):
        entry_name = input("Enter your name:  ")
        entry_email = input("Enter your email: ")
        entry_phone = input("Enter your Phone Number: ")
        entry_password = input("Enter your password: ")
        entry_man_pswd = input("Enter your Manager Password: ")
        if (entry_password == self.password and entry_man_pswd == self.manager_password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The Password or Manager Password is incorrect.")


            
# The following code invokes the methods inside each class for User and Employee

customer = User()
customer.getLoginInfo()

employee = Employee()
employee.getLoginInfo()
    
manager = Manager()
manager.getLoginInfo()
