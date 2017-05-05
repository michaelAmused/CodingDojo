function printOneRetAnother(x){
  firstOdd = x[0];
  console.log(x[x.length-2]);
  for(i=0;i<x.length;i++){
    if(x[i]%2==1){
      firstOdd = x[i];
      break
    }
  }
  console.log(firstOdd);
}

array = [46, 68, 34, 2, 3, 19, 45, 8, 0];
printOneRetAnother(array);