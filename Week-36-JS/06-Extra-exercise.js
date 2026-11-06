//Cree una función que reciba un string y devuelva el string al
//  revés sin usar split(), reverse(), ni join()

//Deberá recorrerlo con un for


function reverseString(text){
    let backwards = "";
    for(const element of text){
        backwards = element + backwards
    };
    return backwards
};
console.log(reverseString("This is the text"));