import re
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class userlogin:
    def register (fullname,password,username):

        with open("name.txt", "a") as user:
            user.write(fullname + "\n")
        with open("pass.txt", "a") as passwords:
            passwords.write(password + "\n")
        with open("username.txt", "a") as nikename:
            nikename.write(username + "\n")

    def login ():
        while True:
            with open("username.txt", "r") as nikename:
                r=nikename.read(username + "\n")
            with open("pass.txt", "r") as passw:
                p=passw.read(username + "\n")  
            if not re.match(username,nikename):
                return False
            if not re.match(password,loginid):
                return False
            return True





class ExpenseTrackerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.login_button = Button(text='Login')
        self.login_button.on_press = self.show_login_form
        self.layout.add_widget(self.login_button)

        self.expense_label = Label(text='Total Spent: 0')
        self.expense_input = TextInput(hint_text='Enter expense')
        self.amount_input = TextInput(hint_text='Enter amount')
        self.add_button = Button(text='Add Expense')
        self.add_button.on_press = self.add_expense

        self.expense_label.disabled = True
        self.expense_input.disabled = True
        self.amount_input.disabled = True
        self.add_button.disabled = True

        self.layout.add_widget(self.expense_label)
        self.layout.add_widget(self.expense_input)
        self.layout.add_widget(self.amount_input)
        self.layout.add_widget(self.add_button)
        self.layout.add_widget(self.add_button)

        self.run_expense_tracker()

        return self.layout
    
    def register (fullname,password,username):

        with open("name.txt", "a") as user:
            user.write(fullname + "\n")
        with open("pass.txt", "a") as passwords:
            passwords.write(password + "\n")
        with open("username.txt", "a") as nikename:
            nikename.write(username + "\n")

    def login ():
        while True:
            with open("username.txt", "r") as nikename:
                r=nikename.read(username + "\n")
            with open("pass.txt", "r") as passw:
                p=passw.read(username + "\n")  
            if r!=username:
                break
            if p != password:
                break


    def set_expense_limit(self):
        limit = None
        while True:
            budget = input("Do you want to set a spend limit (Yes/No): ")
            if budget.capitalize() == "Yes":
                spend_limit = int(input("Enter your spend limit: "))
                limit = spend_limit
                break

            return limit

        

    def alert(limit, currentexpense):
        
        if currentexpense > limit:
            print("Expenses are crossing the spend limit")
        elif currentexpense == limit:
            print("You have reached the spend limit")





    def track_expense(self, expense, amount):
        with open("expenses.txt", "a") as spenton:
            spenton.write(expense + "\n")

        with open("cost.txt", "a") as spentamount:
            spentamount.write(str(amount) + "\n")
        

    def view_expenses(self):
        print("{:<20} {:>10}".format("Expense", "Cost"))

    with open("expenses.txt", "r") as spenton, open("cost.txt", "r") as spentamount:
        expensesandcosts = zip(spenton.readlines(), spentamount.readlines())
        for expense, cost in expensesandcosts:
            cost = cost.strip()
            print("{:<20} {:>10}".format(expense.strip(), cost))
        

    def get_total_spent():
        
        total = 0
        with open("cost.txt", "r") as spentamount:
            lines = spentamount.readlines()
            for line in lines:
                total += int(line.strip())

        return total
    def change_limit(self):
        global limit  
    choice = input("Do you want to change the spend limit? (Yes/No): ")
    if choice.capitalize() == "Yes":
        limit = None
        set_expense_limit()
limit = None      

def add_expense(self):
        expense = self.expenseinput.text
        amount = int(self.amountinput.text)

        
        total_spent = self.trackexpense(expense, amount)
        self.expenselabel.text = f'Total Spent: {total_spent}'
        









limit = ExpenseTrackerApp.set_expense_limit()

while True:
    name=input("enter your name ")
    lastname=input("enter your last name")
    username=input("enter a username")
    fullname=name+lastname
    password=input("enter a password")
    security=ExpenseTrackerApp.register()

    login=input("enter your user name")
    loginid=input("enter your password")
    if userlogin.login (username, password):
        print("Login successful!")
    else:
        print("Login failed. Please check your credentials.")





    expense = input("Spent on: ")
    amount = int(input(f"Amount spent on {expense}: "))
    ExpenseTrackerApp.track_expense(expense, amount)

    current_expense = ExpenseTrackerApp.get_total_spent()
    ExpenseTrackerApp.alert(limit, current_expense)
    choice = input("Do you want to view expenses? (Yes/No): ")
    if choice.capitalize() == "Yes":
        ExpenseTrackerApp.view_expenses()
        print("Total spent:", ExpenseTrackerApp.get_total_spent())

    ExpenseTrackerApp.change_limit()

    choice = input("Do you want to track another expense? (Yes/No): ")
    if choice.capitalize() != "Yes":
        break
print("Have a nice day!")







class LoginForm(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginForm, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.username_label = Label(text='Username:')
        self.username_input = TextInput(hint_text='Enter your username')

        self.password_label = Label(text='Password:')
        self.password_input = TextInput(password=True, hint_text='Enter your password')

        self.error_message = Label(text='')

        self.login_button = Button(text='Login')
        self.login_button.bind(on_press=self.on_login_press)

        self.add_widget(self.username_label)
        self.add_widget(self.username_input)
        self.add_widget(self.password_label)
        self.add_widget(self.password_input)
        self.add_widget(self.error_message)

        self.add_widget(self.login_button)

    def on_login_press(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        login_success, error_message = userlogin.login(username, password)

        self.error_message.text = error_message
        if login_success:
            # Enable expense tracking elements
            self.expense_label.disabled = False
            self.expense_input.disabled = False
            self.amount_input.disabled = False
            self.add_button.disabled = False
        else:
            print("Login failed:", error_message)

if __name__ == '__main__':
    ExpenseTrackerApp().run()