function celsiusToFahrenheit(cDegrees){
  fDegrees = Math.round(cDegrees*9/5+32);
  return fDegrees
}

console.log(celsiusToFahrenheit(25));
console.log(celsiusToFahrenheit(32));
console.log(celsiusToFahrenheit(17));
console.log(celsiusToFahrenheit(-25));
console.log(celsiusToFahrenheit(0));