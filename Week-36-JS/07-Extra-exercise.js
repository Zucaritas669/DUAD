//Cree una función que reciba una lista de números y devuelva una nueva lista 
//sin números repetidos, manteniendo el orden original

const duplicates = (numbers)=>{
    const result = [];
    for(const elements of numbers){
        if(!result.includes(elements)){
            result.push(elements)
        };
    };
    return result;
};
console.log(duplicates([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]));