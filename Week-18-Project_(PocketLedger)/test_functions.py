from logic import PocketLedger
from models import User, Category,Movement

#pytest "Week-18-Project_(PocketLedger)"

#================================= 01 ===================================
def test_find_email():
    #AAA

    #Arrange
    pocket = PocketLedger()
    email = User("Fio", "fio@gmail.com", "pass1234")
    pocket.user_list.append(email)

    #Act
    result = pocket.find_email("fio@gmail.com")

    #Assert
    assert result == email


#================================= 02 ===================================
def test_find_user():
    #AAA

    #Arrange
    pocket = PocketLedger()
    user = User("Shalston", "shalston@gmail.com", "pass1234")
    pocket.user_list.append(user)

    #Act
    result = pocket.find_user("shalston@gmail.com", "pass1234")

    #Assert
    assert result == user


#================================= 03 ===================================
def test_find_category():
    #AAA

    #Arrange
    pocket = PocketLedger()
    category = Category("Test","#FFFFFF")
    pocket.categories_list.append(category)

    #Act
    result = pocket.find_category("Test")

    #Assert 
    assert result == category


#================================= 04 ===================================
def test_create_user_True():
    #AAA

    #Arrange
    pocket = PocketLedger()

    #Act
    result = pocket.create_user("Shalston", "shalston@gmail.com", "pass1234")

    #Assert 
    assert result == True



#================================= 05 ===================================
def test_create_user_False():
    #AAA

    #Arrange
    pocket = PocketLedger()
    pocket.create_user("Shalston", "shalston@gmail.com", "pass1234")

    #Act
    result = pocket.create_user("Shalston", "shalston@gmail.com", "pass1234")

    #Assert 
    assert result == False



#================================= 06 ===================================

def test_change_password():
    #AAA

    #Arrange
    pocket = PocketLedger()
    user = User("Shalston", "shalston@gmail.com", "pass1234")
    pocket.user_list.append(user)

    #Act
    result = pocket.change_password("shalston@gmail.com","password1234")

        #Assert 
    assert result == True


#================================= 07 ===================================

def test_change_password_same_password_return_false():
    #AAA

    #Arrange
    pocket = PocketLedger()
    user = User("Shalston", "shalston@gmail.com", "pass1234")
    pocket.user_list.append(user)

    #Act
    result = pocket.change_password("shalston@gmail.com","pass1234")

    #Assert 
    assert result == False


    #================================= 08 ===================================

def test_get_total():

    #Arrange
    pocket = PocketLedger()
    category = Category("Decoration", "#FFFFFF")
    movement = Movement("House", 2000, category, "income", "27/08/2003")
    pocket.movements_list.append(movement)

    #Act
    result = pocket.get_total()

    #Assert
    assert result == (2000, 0, 2000)













