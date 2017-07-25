function thisLngthThatVal(num1, num2){
  var array = [];
  if(num1===num2){
      return "Jinx!"
  }
  else {
    for(i=0; i<num1; i++){  
      array.push(num2);
    }
    return array;
  }
}

console.log(thisLngthThatVal(1,2));
console.log(thisLngthThatVal(4,0));
console.log(thisLngthThatVal(6,2));
console.log(thisLngthThatVal(0,2));
console.log(thisLngthThatVal(10,10));