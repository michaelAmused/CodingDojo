var arr = ["James", "Jill", "Jane", "Jack"]

function fancyArray(arg){
    for(var i = 0; i < arg.length; i++){
        console.log(i, "->", arg[i]);
    }
}

fancyArray(arr)
