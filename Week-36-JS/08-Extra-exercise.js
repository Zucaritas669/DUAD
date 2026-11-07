//Cree una función que cuente cuántas 
// veces aparece cada palabra en un string
//Ignore mayúsculas/minúsculas y 
//signos de puntuación

const countWords =(text)=>{
    const words = text.toLowerCase().replaceAll(".", "").split(" ");
    const result = {};
    for(const word of words){
        if(result[word]){
            result[word]+=1;
        }else{
            result[word]=1
        }
    };
    return result;
};
console.log(countWords("This is a test. This test is simple."));