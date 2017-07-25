function randomChance(qIn){
    for(qIn; qIn > 0; qIn--){
        if(Math.trunc(Math.random()*100)%100==0){
            return(qIn + Math.trunc(Math.random() * 50)+51);
        }
    }
    return(0);
}

console.log(randomChance(1001));
