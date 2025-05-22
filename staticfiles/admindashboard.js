let a= document.querySelector(".sales-details")
  
let Reja_sum =document.querySelectorAll(".Reja_sum"),
  Qarizdor=document.querySelectorAll(".qariz"),
Qarizdorlik=[],
 Reja_sums=[];

   function setvalue(getelement,setvalue){
      for (let i = 0; i < getelement.length; i++) {
      const element = getelement[i]
      setvalue.push(element.textContent)
    }
    }
    setvalue(Qarizdor,Qarizdorlik)
    setvalue(Reja_sum,Reja_sums)
    let ctx = document.getElementById('lineChart').getContext('2d');
    let myChart = new Chart(ctx, {
      type: 'line',
      data: {
          labels: [1 ,2,3,4,5,6,7,8,9,10,11,12],
          datasets: [{
              label: Rejalashtrilgan to'luvlar summasi( 000 ga qisqartrilgan),
              data: Reja_sums,

              backgroundColor: [
                  'blue'
              ],
              borderColor: 'blue',
              borderWidth: 1
          },
          {
              label: Qarizdorliklar ( 000 ga qisqartrilgan),
              data: Qarizdorlik ,

              backgroundColor: [
                  'red'
              ],
              borderColor: 'red',
              borderWidth: 3
          }
        ]
      },
      options: {
          responsive: true
      }
  });