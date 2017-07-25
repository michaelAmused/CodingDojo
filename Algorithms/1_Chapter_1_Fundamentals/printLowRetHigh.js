function printHighRetLow(x){
  var low = x[0];
  var high = x[0];
  for(i=1;i<x.length-1;i++){
    if(x[i+1]<low){
      low = x[i+1];
    }
    if(x[i+1]>high){
      high = x[i+1];
    }
  }
  console.log(low);
  return high;
}
array = [8,3,10,48,0,-5,9,-45,1,25]
console.log(printHighRetLow(array));

