var array = [1,3,5,7,9,13];
function valGrThSec(x){
  var count = 0;
  for(i=0; i<array.length; i++){
    if(array[i] > array[1]){
      count += 1;
      console.log(array[i]);

    }
    else {
      continue;
    }
  }
  return count;
}

console.log(valGrThSec(array));