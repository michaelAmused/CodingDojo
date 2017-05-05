function flexCountdown(lowNum,highNum,mult){

    for(highNum-=highNum%mult;highNum>=lowNum;highNum-=mult){
        console.log(highNum);
    }
}

flexCountdown(2,10,3);
