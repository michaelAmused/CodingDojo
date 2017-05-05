function PrintNreturn(arr){
    if(arr.length==2){
        console.log(arr[0]);
        return arr[1];
    }
    else{
        console.log("worng input");
    }
}

console.log(PrintNreturn([86,99]))
