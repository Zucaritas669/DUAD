const positive = document.getElementById("positive");
const negative = document.getElementById("negative");
const company = document.getElementById("company");

positive.addEventListener("change", function(){
    company.hidden = false;
    company.required = true;
});
negative.addEventListener("change", function(){
    company.hidden = true;
    company.required = false;
    company.value = "";
});

