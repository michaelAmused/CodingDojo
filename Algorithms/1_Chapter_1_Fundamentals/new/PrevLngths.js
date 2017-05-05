arr = ["this Was", "just a","complete", "waste", "of time."]
function prevLngths(x){
  var count = [];
  for(i=0;i<x.length;i++){
    count[i] = x[i].length;

  }
  return count;
}

console.log(prevLngths(arr));