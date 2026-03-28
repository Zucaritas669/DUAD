user_logged_in = False

def requires_login(func):
    def wrapper(*args,**kwargs):
        if not user_logged_in:
            raise ValueError("Not log in yet")
        else:
            func(*args,**kwargs)
    return wrapper

@requires_login
def view_profile():
    print("Mostrando perfil del usuario")


view_profile()