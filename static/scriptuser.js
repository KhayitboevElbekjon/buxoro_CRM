const navlink=document.querySelectorAll(".nav_link"),
time = document.querySelector(".time"),
time_month= document.querySelector(".time_month"),
time_day= document.querySelector(".time_day"),
time_hour= document.querySelector(".time_hour"),
time_min= document.querySelector(".time_min"),
video_btn = document.querySelector(".video_btn")
video_close =document.querySelector(".close")
video =document.querySelector(".video") 
time_second= document.querySelector(".time_second");


// function active link
function linkColor(){
    
    navlink.forEach(link=>{
        link.classList.remove("active_link")
        this.classList.add('active_link')
    })
}

navlink.forEach(link=>{
    link.addEventListener('click',linkColor)
})


//open video section
video_btn.addEventListener("click", ()=>{
   video.classList.remove("none")
})
video_close.addEventListener("click",()=>{

  video.classList.add("none")
})

// Time
setInterval(()=>{
  

  const mydate = new Date()
  function addthero(val) {
      if(val/10 >=1){
        return val
      }else{
        return val=`0${val}`
      }
      addthero()
    }

                       
    time_second.textContent=addthero(mydate.getSeconds());
    time_min.textContent= addthero(mydate.getMinutes());
    time_hour.textContent= addthero(mydate.getHours());
    time_day.textContent=addthero(Date.getDay());
    time_month.textContent= addthero(mydate.getMonth());
},1000)






// SwiperJS
var swiper = new Swiper(".mySwiper", {
  slidesPerView: 1,
  grabCursor: true,
  loop: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});


