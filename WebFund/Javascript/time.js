function time(hour,minute,period){
    if(minute > 30 && minute < 60) {
        if(period==="AM"){
            console.log("it's almost",hour+1,"in the morning");
        }
        else if(period==="PM"){
            console.log("it's almost",hour+1,"in the evening");
        }
    }
    else if(minute < 30 && minute > 0){
        if(period==="AM"){
            console.log("it's just after",hour,"in the morning");
        }
        else if(period==="PM"){
            console.log("it's just after",hour,"in the evening");
        }
    }
    else if(minute == 30){
        if(period==="AM"){
            console.log("it's half past",hour,"in the morning");
        }
        else if(period==="PM"){
            console.log("it's half past",hour,"in the evening");
        }
    }
}

time(6,29,"PM")
