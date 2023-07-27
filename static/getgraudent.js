
let tr = document.querySelectorAll("tbody tr") 

 tr.forEach(buqiymat=>{
let  qiymat= buqiymat.querySelector(".qiymat"),
    setqiymat = buqiymat.querySelector(".status");
    
    if (qiymat.textContent>=86) {
       setqiymat.classList.add("alo")  
       setqiymat.textContent = "ALo"    
    }
     else if ( qiymat.textContent>=70  &&  qiymat.textContent<86) {
        setqiymat.classList.add("yaxshi")  
        setqiymat.textContent = "Yaxshi"  
     } 
     else if ( qiymat.textContent>=60  &&  qiymat.textContent<70) {
        setqiymat.classList.add("yomon")    
        setqiymat.textContent = "yomon"
     } 
     else{
        setqiymat.classList.add("past")    
        setqiymat.textContent = "Past!"
     }
 }) 