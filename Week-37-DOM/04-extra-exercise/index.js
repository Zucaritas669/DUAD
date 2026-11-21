const text = document.getElementById("text");
const changeBtn = document.getElementById("change_btn");

const color = ["red", "blue", "green", "orange", "purple"];

changeBtn.addEventListener("click",function() {
    
    const index = Math.floor(Math.random() * color.length);
    text.style.color = color[index]
});


