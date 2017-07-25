function fahrenheitToCelsius(fDegrees){
  cDegrees = Math.round((fDegrees - 32)*5/9);
  return cDegrees
}

console.log(fahrenheitToCelsius(75));
console.log(fahrenheitToCelsius(100));
console.log(fahrenheitToCelsius(19));
console.log(fahrenheitToCelsius(69));
console.log(fahrenheitToCelsius(32));