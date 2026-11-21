const taskInput = document.getElementById("task");
const addBtn = document.getElementById("addbtn");
const list = document.getElementById("list");

const showInput = () =>{
    taskInput.hidden = false
};
addBtn.addEventListener("click", showInput);

const createDeleteBtn = (li) => {
    const deleteBtn = document.createElement("button")
    deleteBtn.type = "button"
    deleteBtn.textContent = "Delete"
    deleteBtn.addEventListener("click", () => li.remove())
    return deleteBtn
};

const addToList = () =>{
    if(taskInput.value.trim()===""){
        return;
    }
    const li = document.createElement("li")
    li.textContent = taskInput.value;
    li.appendChild(createDeleteBtn(li));
    list.appendChild(li);
    taskInput.value = "";
};

const handleAdd = () => {
    if (taskInput.hidden) {
        showInput()
    } else {
        addToList()
    }
};

addBtn.addEventListener("click", handleAdd);