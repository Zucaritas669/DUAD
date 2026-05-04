
from models import User,Category,Movement
from logic import PocketLedger
from data import save_data, load_data, export_csv
import re
import FreeSimpleGUI as sg


def get_text(text):
    return text.replace(" ","").isalpha()


pocketLedger = PocketLedger()
load_data(pocketLedger)

def login_window():

    sg.theme("Topanga")
    layout = [
        [sg.Text("Login", justification="center" )],
        [sg.HorizontalSeparator()],
        [sg.Text("Email",size = (10,1)) ,sg.Input(key = "-EMAIL-",size = (25,1))],
        [sg.Text("Password",size = (10,1)),sg.Input(key = "-PASSWORD-", password_char= "*",size = (25,1))],
        [sg.Button("Login"),sg.Button("Sign up"),sg.Button("Forgot password")],
        [ sg.Button("Exit")]
    ]
    window = sg.Window("Login",layout)

    while True:
        event , value = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            window.close()
            break

        if event == "Sign up":
            window.close()
            create_user_window()
            break


        if event == "Login":
            email = value["-EMAIL-"]
            password = value["-PASSWORD-"]

            if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",email):
                sg.popup_error("Invalid email format")
            elif not re.match(r'^(?=.*\d).{8,}$',password):
                sg.popup_error("Invalid password format")

            else:
                user = pocketLedger.find_user(email,password)
                if user:
                    window.close()
                    main_pocket_ledger(user)
                    break
                    

                else:
                    sg.popup_error("User not found")

        if event == "Forgot password":
            window.close()
            forgot_password()
            break


def create_user_window():
    sg.theme("Topanga")
    layout = [
        [sg.Text("Sign up", justification="center" )],
        [sg.HorizontalSeparator()],
        [sg.Text("Name",size = (10,1)) ,sg.Input(key = "-NAME-",size = (25,1))],
        [sg.Text("Email",size = (10,1)) ,sg.Input(key = "-EMAIL-",size = (25,1))],
        [sg.Text("Password",size = (10,1)),sg.Input(key = "-PASSWORD-",size = (25,1))],
        [sg.Button("Sign up") ,sg.Button("Exit")]
    ]
    window = sg.Window("Sign up",layout)

    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            window.close()
            break

        if event == "Sign up":
            name = value["-NAME-"]
            email = value["-EMAIL-"]
            password = value[ "-PASSWORD-"]

            if not get_text(name):
                    sg.popup_error("Invalid name format")
            elif not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",email):
                    sg.popup_error("Invalid email format")
            elif not re.match(r'^(?=.*\d).{8,}$',password):
                    sg.popup_error("Invalid password format")

            else:
                user = User.create_user(name,email,password)
                if user:
                    pocketLedger.user_list.append(user)
                    save_data(pocketLedger)
                    window.close()
                    login_window()
                    break
                else:
                    sg.popup_error("Ops something has happened, please try again")


def forgot_password():
    sg.theme("Topanga")
    layout = [
        [sg.Text("New password", justification="center" )],
        [sg.HorizontalSeparator()],
        [sg.Text("Email",size = (10,1)),sg.Input(key = "-Email-",size = (25,1))],
        [sg.Text("New Password",size = (10,1)),sg.Input(key = "-NEW PASSWORD-",size = (25,1))],
        [sg.Button("New password"), sg.Button("Exit")]
    ]
    
    window = sg.Window("New password",layout)

    while True:
        event, value = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            window.close()
            break

        if event == "New password":
            email = value["-Email-"]
            new_password = value["-NEW PASSWORD-"]
            
            if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",email):
                sg.popup_auto_close("Invalid email format")
            elif not re.match(r'^(?=.*\d).{8,}$', new_password):
                sg.popup_auto_close("Invalid password format")
            
            else:
                user = pocketLedger.find_email(email)
                if not user:
                    sg.popup_auto_close("Email not found")

                else:
                    np = pocketLedger.change_password(email,new_password)
                    if np:
                        sg.popup_auto_close("Password changed correctly")
                        save_data(pocketLedger)
                        window.close()
                        login_window()
                        break
                    else:
                        sg.popup_auto_close("Password is the same as the current one")


def add_category_window(user):
    layout = [
        [sg.Text(f"Welcome, {user.name}",justification="center")],
        [sg.HorizontalSeparator()],
        [sg.Text("Name",size = (10,1)),sg.Input(key= "-NAME-",size = (25,1))],
        [sg.Text("Color",size = (10,1)),sg.Input(key= "-COLOR-",size = (25,1)), sg.ColorChooserButton("Pick Color",target= "-COLOR-")],
        [sg.Button("Save"), sg.Button("Exit")],
    ]
    window = sg.Window("Add Category",layout)

    while True:
        event,value = window.read()
        
        if event == sg.WIN_CLOSED or event == "Exit":
            window.close()
            break

        if event == "Save":
            name = value["-NAME-"]
            color = value["-COLOR-"]

            if not get_text(name):
                sg.popup_auto_close("Invalid name format")
            else:
                category = Category.create_category(name,color)    
                pocketLedger.add_category(category)
                sg.popup_auto_close("Category added correctly")
                save_data(pocketLedger)
                window.close()
                break
                

def get_categories_name():
    categories_names = []
    for c in pocketLedger.categories_list:
        categories_names.append(c.name)
    return categories_names




def add_movement_window(user,movement_type):
    layout = [
        [sg.Text(f"Welcome, {user.name}",justification="center")],
        [sg.HorizontalSeparator()],
        [sg.Text("Title",size = (10,1)),sg.Input(key= "-TITLE-",size = (25,1))],
        [sg.Text("Amount",size = (10,1)),sg.Input(key= "-AMOUNT-",size = (25,1))],
        [sg.Text("Category",size = (10,1)),sg.Combo(get_categories_name(),key= "-CATEGORY-",readonly=True)],
        [sg.Text("Date",size = (10,1)),sg.Input(key="-DATE-", size=(25,1)),sg.CalendarButton("Pick Date",target="-DATE-",format="%Y-%m-%d")],
        [sg.Button("Save"), sg.Button("Exit")],
    ]
    window = sg.Window("Movements",layout)

    while True:
        event, value = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            window.close()
            break

        if event == "Save":
            title = value["-TITLE-"]
            amount = value["-AMOUNT-"]
            category_name = value["-CATEGORY-"]
            date = value["-DATE-"]

            if not get_text(title):
                sg.popup_auto_close("Invalid title format")
            elif not amount.isdigit():
                sg.popup_auto_close("Invalid amount format")
            else:
                category = pocketLedger.find_category(category_name)
                move = Movement.create_movement(title,float(amount),category,movement_type,date)

                if movement_type.lower() == "income":
                    pocketLedger.add_income(move)
                    sg.popup_auto_close("Category added correctly")
                else:
                    pocketLedger.add_expense(move)
                    sg.popup_auto_close("Category added correctly")

                save_data(pocketLedger)
                window.close()
                break





def main_pocket_ledger(user):
    sg.theme("Topanga")
    pocketLedger.current_user = user

#-------------------- Create table ------------------------
    field_names = ["Date", "Title", "Type", "Amount"]

#---------- Create a function to add all the elements in a list --------------------
    def get_table():
        table_list = []
        raw_colors = []

        for i,m in enumerate(pocketLedger.movements_list):
            table_list.append([m.date , m.title, m.movement_type, m.amount])
            raw_colors.append((i, m.category.color))
        return table_list,raw_colors
    
    def refresh_table(): 
        table_data, row_colors = get_table()
        window["-TABLE-"].update(values = table_data, row_colors = row_colors)

    table_data, row_colors = get_table()

    layout = [
        [sg.Text(f"Welcome, {user.name}",justification="center")],
        [sg.HorizontalSeparator()],

        [sg.Table( values = table_data, headings= field_names, key = "-TABLE-",expand_x=True,row_colors=row_colors)], # <- This is how you create the table
        [sg.Button("Add Category",expand_x=True)],
        [sg.Button("Add Expense",expand_x=True)],
        [sg.Button("Add Income",expand_x=True)],
        [sg.Button("Export CSV",expand_x=True)],
        [sg.Button("Exit",expand_x=True)],
        ]
    window = sg.Window("Pocket Ledger",layout)

    while True:
        event,value = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            window.close()
            save_data(pocketLedger)
            break

        if event == "Add Category":
            add_category_window(user)
            refresh_table()

        elif event == "Add Expense":
            if not pocketLedger.categories_list:
                sg.popup_auto_close("You need to add a category first!")
            else:
                add_movement_window(user,"expense")
                refresh_table()

        elif event == "Add Income":
            if not pocketLedger.categories_list:
                sg.popup_auto_close("You need to add a category first!")
            else:
                add_movement_window(user,"income")
                refresh_table()
            
        elif event == "Export CSV":
            export_csv(pocketLedger)
            sg.popup_auto_close("CSV exported successfully!")


login_window()

