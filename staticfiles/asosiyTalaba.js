
{
    const form = document.querySelector("form"),
        nextBtn = form.querySelector(".nextBtn"),
        TR =document.querySelectorAll("tbody tr"),
        beack = document.querySelector(".beack"),
        container = document.querySelector(".container"),
        backBtn = form.querySelector(".backBtn"),
        allInput = form.querySelectorAll(".first input");
        
    
beack.addEventListener("click",()=>{
    container.classList.add("hidden")
})


TR.forEach(talabgor=>{
    let  fan=talabgor.querySelector(".status");
    let hissob_tb =document.querySelector("#hissob_tb");

     talabgor.addEventListener("click",()=>{
        container.classList.remove("hidden")
        let  ism  =talabgor.querySelector(".name"),
        input_ism =document.querySelector(".input_ism"),
        fam=talabgor.querySelector(".fam"),
        input_fam=document.querySelector(".input_fam"),
        yili=talabgor.querySelector(".yili"),
        input_yili=document.querySelector(".input_yili"),
        tel=talabgor.querySelector(".tel"),
        input_tel=document.querySelector(".input_tel");
       
        input_fan =document.querySelector(".input_fan")
 
        // input_ism.value=ism.textContent;
        // input_fam.value = fam.textContent;
        // input_tel.value =tel.textContent;
        //   input_fan.value =fan.textContent
        //   input_yili.value =yili.textContent;
   
    })
    if(  (!(talabgor.querySelector(".status")))  || (!(document.querySelector(".container ").hasAttributes(".hidden"))) ){
    //   talabgor.classList.add("hidden")
      hissob_tb.classList.add("hidden")
    }  
    if((document.querySelector(".container ").hasAttributes(".hidden"))){
        hissob_tb.classList.remove("hidden")
    }


    console.log( (!(talabgor.querySelector(".status")))  ); 
    console.log( (!(document.querySelector(".container ").hasAttributes(".hidden"))) );
   
}
)


}