function rmvWhtSp(string) {
    var l = string.length-1;
    var newString = '';
    for (var i=0; i <= l; i++){
        if (string[i]!=" " && string[i]!= '\t'){
            newString += string[i];
        }
    }
    return newString;
}

console.log(rmvWhtSp("pl ayThat fu nk ymus ic"));
