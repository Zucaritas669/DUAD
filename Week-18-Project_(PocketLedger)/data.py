from models import User,Category,Movement
from logic import PocketLedger
import json
import csv


def save_data(pocket_ledger):
    data = {
        "user" : [],
        "category" : [],
        "movement" : [],
    }

    for u in pocket_ledger.user_list:
        data["user"].append({
            "name": u.name,
            "email" : u.email,
            "password" : u.password
        })
    
    for c in pocket_ledger.categories_list:
        data["category"].append({
            "name": c.name,
            "color": c.color
        })

    for m in pocket_ledger.movements_list:
        data["movement"].append({
            "title": m.title,
            "amount": m.amount,
            "category": m.category.name,
            "movement_type": m.movement_type,
            "date": m.date
        })

    with open("pocket_ledger.json","w",encoding='utf-8')as file:
        json.dump(data,file,indent=4)


def load_data(pocket_ledger):
    try:
        with open("pocket_ledger.json","r",encoding='utf-8')as file:
            data = json.load(file)
        
        for u in data["user"]:
            user = User(u["name"],u["email"],u["password"])
            pocket_ledger.user_list.append(user)

        for c in data["category"]:
            category = Category(c["name"],c["color"])
            pocket_ledger.categories_list.append(category)

        for m in data["movement"]:
            category = pocket_ledger.find_category(m["category"])
            movement = Movement(m["title"], float(m["amount"]), category, m["movement_type"], m["date"])
            pocket_ledger.movements_list.append(movement)

    except FileNotFoundError:
        pass


def export_csv(pocket_ledger):

    field_names = ["date", "title", "amount", "category", "movement_type"]

    with open("pocket_ledger.csv","w",newline="", encoding='utf-8') as file:
        writer = csv.DictWriter(file,field_names)
        writer.writeheader()

        for m in pocket_ledger.movements_list:
            writer.writerow({
                "date": m.date,
                "title": m.title,
                "amount": m.amount,
                "category":m.category.name,
                "movement_type": m.movement_type
            })
            
        total_income, total_expense, balance = pocket_ledger.get_total()
        writer.writerow({"date": "Totals:"})
        writer.writerow({"title": "Total income:", "amount": total_income})
        writer.writerow({"title": "Total expense:", "amount": total_expense})
        writer.writerow({"title": "Balance", "amount": balance})




            
                

            
            


        


    
