//Toma un string y conviertelo en una lista de palabras, 
// separandolas por espacios en blanco. 
// No puedes usar la función split.

const example = "This is a string!";
const result = [];
let actualWord = "";

for(const element of example){
    if (element === " "){
        result.push(actualWord);
        actualWord = "";
    } else {
        actualWord += element;
    }
}
result.push(actualWord);

console.log(result); 
