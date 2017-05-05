function countPositives(x){
  count = 0;
  for(i=0;i<x.length;i++){
    if(x[i]>=0){
      count++
    }
  }
  x[x.length-1]=count;
  return x;
}

x = [-1,1,1,1];
console.log(countPositives(x));