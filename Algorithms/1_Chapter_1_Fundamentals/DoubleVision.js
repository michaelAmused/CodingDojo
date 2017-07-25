function dblVis(x){
  y = [];
  for(i=0;i<x.length;i++){
    y[i]=x[i]*2;
  }
  return y;
}
x = [1,2,3];
console.log(dblVis(x));
console.log(x);