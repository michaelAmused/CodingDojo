function makeItBig(x){
  for(i=0;i<x.length;i++){
    if(x[i]>0){
      x[i]="big";
    }
  }
  return x;
}

console.log(makeItBig([-1,3,5,-5,0]));