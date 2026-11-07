//Realiza un programa que recorra una lista de números 
// y almacene todos los pares en otra lista
//Para este ejercicio intenta hacer una solución con un for 
// y otra utilizando la función filter

const numbersExample = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
const newArray = numbersExample.filter((elements)=>{
    return elements %2 === 0
});
console.log(newArray)


const numbersExampleTwo = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
const evenNumbers = []
for(const i of numbersExampleTwo){
    if(i %2 ===0){
        evenNumbers.push(i)
    };
};
console.log(evenNumbers)


