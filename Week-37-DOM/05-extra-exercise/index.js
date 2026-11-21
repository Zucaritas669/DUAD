const number = document.getElementById("number")
const addBtn = document.getElementById("add")
const removeBtn = document.getElementById("remove")
const message = document.getElementById("message")

const incrementNum = () => {
    number.textContent = Number(number.textContent) + 1;
    message.textContent = "";
};

const decrementNum = () =>{
    const current = Number(number.textContent)
    if (current > 0){
        number.textContent = current - 1
        
    } else {
        message.textContent = "Invalid action";
    };
};

addBtn.addEventListener("click", incrementNum);
removeBtn.addEventListener("click", decrementNum)

