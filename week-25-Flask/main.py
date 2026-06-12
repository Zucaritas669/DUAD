from flask import Flask, request, jsonify
import json


# cd week-25-Flask
# python main.py

#________________ API ________________

app = Flask(__name__)


#________________Read and Write Json file ________________

task_file = "tasks.json"


def read_tasks():
    try:
        with open(task_file,"r",encoding="utf-8") as file:
            data = json.load(file)
            return data 
    except FileNotFoundError as ex:
        return []


def write_tasks(data):
    try:
        with open(task_file,"w",encoding="utf-8") as file:
            json.dump(data,file,indent=4,ensure_ascii=False)
    except Exception as ex:
        print(str(ex))
        


#___________This is how create a flask with a class ____________
class Tasks():

    def __init__(self,id,title,description,status):
        self.id = id 
        self.title = title
        self.description = description
        self.status = status
    

    #_________If you want to use a class with Flask , need to turn it into a dict _____________
    def task_to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description, 
            "status": self.status # (Not done, in progress , done)
        }
    

@app.route("/get_tasks",methods =["GET"])
def get_tasks():
    tasks = read_tasks()
    return {"Data":tasks},200


@app.route("/filter_tasks", methods =["GET"])
def get_filter_tasks():
    tasks = read_tasks()
    filter_tasks = request.args.get("status")

    if filter_tasks:            
        filtered = []
        for t in tasks:
            if t["status"] == filter_tasks:
                filtered.append(t)  
        return {"data": filtered}, 200
    else:
        return {"data": tasks}, 200
    


valid_status =["Not done", "In progress", "Done"]

@app.route("/create_task",methods=["POST"])
def create_task():
    try:
        if "id" not in request.json:
            raise ValueError("ID missing")
        
        if "title" not in request.json:
            raise ValueError("Title missing")
        
        if "description" not in request.json:
            raise ValueError("Description missing")
        
        if "status" not in request.json:
            raise ValueError("Status missing")    
        
        if request.json["status"] not in valid_status:
            raise ValueError("Hey dude, this status does not exit, please read!!!")

        tasks = read_tasks()
        for t in tasks:
            if t["id"] == request.json["id"]:
                raise ValueError("ID already exist")
            
        new_task = Tasks(
            id = request.json["id"],
            title = request.json["title"],
            description= request.json["description"],
            status= request.json["status"]
        )

        tasks.append(new_task.task_to_dict())
        write_tasks(tasks)
        return new_task.task_to_dict(),200
    
    except ValueError as ex:
        return jsonify(message=str(ex)),400
    
    except Exception as ex:
        return jsonify(message=str(ex)),500



@app.route("/delete_task/<int:task_id>", methods= ["DELETE"])
def delete_task(task_id):

    tasks_list = read_tasks()
    for t in tasks_list:

        if t["id"] == task_id:
            tasks_list.remove(t)
            write_tasks(tasks_list)

            return jsonify(message = "Task deleted successfully"),200
    return jsonify(message = "Task not Found"),400


@app.route("/edit_task/<int:task_id>",methods = ["PATCH"])
def edit_task(task_id):
    tasks = read_tasks()
    for t in tasks:
        
        if t["id"] == task_id:

            if "title" in request.json:
                t["title"] = request.json["title"]
            
            if "description" in request.json:
                t["description"] = request.json["description"]

            if "status" in request.json:
                t["status"] = request.json["status"]

            write_tasks(tasks)
            return jsonify(message = "Task edited successfully" ),200
        
    return jsonify(message = "Task not Found"),400
            

            




if __name__ =="__main__":
    app.run(host = "localhost", debug=True)


