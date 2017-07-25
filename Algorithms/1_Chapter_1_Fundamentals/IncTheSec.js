function incTheSec(x){
  console.log(x);
  for(i=1;i<x.length;i+=2){
    x[i]+=1;
  }
  for(i=0;i<x.length;i++){
    console.log(x[i]);
  }
  return x;
}
arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14];
console.log(incTheSec(arr));