//Toma una lista de temperaturas en grados celsius
//  y conviertala a farenheit utilizando la función map

const temperaturesCelsius = [22, 25, 30, 18, 15, 28, 35, 10, 0, -5, 20, 33];
const temperaturesFahrenheit = temperaturesCelsius.map((element)=>{
    return element * 9/5 + 32;
});

console.log(temperaturesFahrenheit);