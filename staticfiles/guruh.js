{
    {
        let dots_event= document.querySelector(".dots_event")
          const accordionItemHeaders = document.querySelectorAll(".accordion-item-header");
      console.log(dots_event);
      accordionItemHeaders.forEach(accordionItemHeader => {
        accordionItemHeader.addEventListener("click", event => {
          accordionItemHeader.classList.toggle("active");
          const accordionItemBody = accordionItemHeader.nextElementSibling;
          if(accordionItemHeader.classList.contains("active")) {
            accordionItemBody.style.maxHeight = accordionItemBody.scrollHeight + "px";
          }
          else {
            accordionItemBody.style.maxHeight = 0;
          }
          
        });
      });
       } 
}