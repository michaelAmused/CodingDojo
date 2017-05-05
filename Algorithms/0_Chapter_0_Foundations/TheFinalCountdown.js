function finalCountdown(param1,param2,param3,param4){

    for(param3-=param3%param1;param3>=param2;param3-=param1){
        if(param3==param4){
            continue;
        }
        else {
            console.log(param3);
        }

    }
}

finalCountdown(3,5,17,9);
