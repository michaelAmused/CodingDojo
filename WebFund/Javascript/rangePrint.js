function printRange(start,end,skip){
    for(var i=start; i<=end; i+=skip){
        if(i<end){
            console.log(i);
        }
    }
}

printRange(2, 10, 2)
