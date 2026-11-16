const positive = document.getElementById("positive");
const negative = document.getElementById("negative");
const company = document.getElementById("company");

const sendBtn = document.getElementById("send_button");

positive.addEventListener("change", function(){
    company.hidden = false;
    company.required = true;
});
negative.addEventListener("change", function(){
    company.hidden = true;
    company.required = false;
});

