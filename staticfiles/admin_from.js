{
    const form = document.querySelector("form"),
        nextBtn = form.querySelector(".nextBtn"),
        fa_plus=document.querySelector(".fa-plus"),
        select_student=document.querySelector(".select_student"),
        select_student_close= select_student.querySelector("i")
        TR =document.querySelectorAll("tbody tr"),
        beack = document.querySelector(".beack"),
        container = document.querySelector(".container"),
        backBtn = form.querySelector(".backBtn"),
        allInput = form.querySelectorAll(".first input");
        
    


fa_plus.addEventListener("click",()=>{
    select_student.classList.remove("hidden")
})
select_student_close.addEventListener("click",()=>{
    select_student.classList.add("hidden")
})
beack.addEventListener("click",()=>{
    container.classList.add("hidden")
})



TR.forEach(talabgor=>{
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
        fan=document.querySelector(".status")
        input_fan =document.querySelector(".input_fan")

          input_ism.value=ism.textContent;
          input_fam.value = fam.textContent;
          input_tel.value =tel.textContent;
          input_fan.value =fan.textContent
        //   input_yili.value =yili.textContent;
   
    })
})




}