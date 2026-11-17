const addBtn = document.getElementById("add_button")
const text = document.getElementById("text")
const addNewText = document.getElementById("new_text")

addBtn.addEventListener("click", function () {
  if (text.value.trim() === "") {
    return;
  }
  addNewText.textContent = text.value;
  text.value = "";
});
