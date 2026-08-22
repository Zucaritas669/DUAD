import FreeSimpleGUI as sg
import re
from Repo.user_repository import UserRepository


admin_repo = UserRepository()

def get_text(text):
    return text.replace(" ","").isalpha()

def admin_window():

    sg.theme("Topanga")
    layout = [
        [sg.Text("CREATE ADMIN", justification="center" )],
        [sg.HorizontalSeparator()],
        [sg.Text("Name",size = (10,1)) ,sg.Input(key = "-NAME-",size = (25,1))],
        [sg.Text("Username",size = (10,1)) ,sg.Input(key = "-USERNAME-",size = (25,1))],
        [sg.Text("Email",size = (10,1)) ,sg.Input(key = "-EMAIL-",size = (25,1))],
        [sg.Text("Password",size = (10,1)),sg.Input(key = "-PASSWORD-",size = (25,1))],
        [sg.Button("Create") ,sg.Button("Exit")]
    ]
    window = sg.Window("CREATE ADMIN",layout)

    while True:
        event , value = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            window.close()
            break

        if event == "Create":
            name = value["-NAME-"]
            email = value["-EMAIL-"]
            username = value["-USERNAME-"]
            password = value["-PASSWORD-"]


            if not name.strip():
                sg.popup_error("Invalid name format")
            elif not username.strip():
                sg.popup_error("Invalid username format")
            elif not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
                sg.popup_error("Invalid email format")
            elif not re.match(r'^(?=.*\d).{8,}$', password):
                sg.popup_error("Invalid password format")

            else:
                result = admin_repo.create_admin(name, username, email, password)
                if result is False:
                    sg.popup_error("Email already exist")
                elif result is None:
                    sg.popup_error("Username already exist")

                else:
                    sg.popup_ok(f"Admin '{username}' created successfully")
                    window["-NAME-"].update("")
                    window["-USERNAME-"].update("")
                    window["-EMAIL-"].update("")
                    window["-PASSWORD-"].update("")

if __name__ == "__main__":
    admin_window()