function fitFrstVal(x){
  if(x[0]>x.length){
    return "Too big!"
  }
  else if(x[0]<x.length){
    return "Too small!"
  }
  else {
    return "Just right!"
  }
}

console.log(fitFrstVal([1,2,3,4,5]));
console.log(fitFrstVal([7,2,3,4,5]));
console.log(fitFrstVal([5,2,3,4,1]));