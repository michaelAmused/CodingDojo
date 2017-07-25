function evenNodds(x){
  s1 = "That's odd!"
  s2 = "Even more so!"
  for(i=0;i<x.length-2;i++){
    if(x[i]%2==1 && x[i+1]%2==1 && x[i+2]%2==1){
      console.log(s1);
    }
    if(x[i]%2==0 && x[i+1]%2==0 && x[i+2]%2==0){
      console.log(s2);
    }
  }
}

x = [2,4,5,3,7,3,2,4,6,4,6,6,3,4,5,6,8,2,0,1,7,9];
console.log(x.length);
evenNodds(x);