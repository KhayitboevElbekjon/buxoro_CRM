{

    group_diagramm_boxs =document.querySelectorAll(".group_diagramm_box")
    
    // console.log(group_diagramm_boxs); 
     
    let ctx = document.getElementById('lineChart').getContext('2d');
    let chiqim =document.querySelectorAll(".chiqim"),
    kirim =document.querySelectorAll(".kirim")
    console.log(kirim[1].textContent , chiqim);
    let  arr_chiqim =[] ,arr_kirim= []; 
    function setvalue(getelement,setvalue){
      for (let i = 0; i < getelement.length; i++) {
      const element = getelement[i]
      setvalue.push(element.textContent)
    }
    }
  
  setvalue(chiqim,arr_chiqim)
  setvalue(kirim ,arr_kirim )
  console.log(arr_chiqim ,arr_kirim);
  

  let myChart = new Chart(ctx, {
      type: 'line',
      data: {
          labels: [1 ,2,3,4,5,6,7,8,9,10,11,12],
          datasets: [{
              label: 'Chiqim ',
              data: arr_chiqim,
             
              backgroundColor: [
                  'red'
              ],
              borderColor: 'red',
              borderWidth: 4    
          },
          {
              label: `Kirim`,
              data: arr_kirim,
             
              backgroundColor: [
                  'blue'
              ],
              borderColor: 'blue',
              borderWidth: 4
          }
        ]
      },
      options: {
          responsive: true
      }
  });
   


  
  var ctx2 = document.getElementById('doughnut').getContext('2d');
  oylik_all=document.querySelector(".oylik_all").textContent,
      soliq_all=document.querySelector(".soliq_all").textContent,
      reklama_all=document.querySelector(".reklama_all").textContent,
      kamunal_all=document.querySelector(".kamunal_all").textContent;
      ragbatlantirish_all=document.querySelector(".ragbatlantirish_all").textContent;
      boshqalar_all=document.querySelector(".boshqalar_all").textContent;
      
  var myChart2 = new Chart(ctx2, {
    
      type: 'doughnut',
      data: {
          labels: [`Oylik`, `Soliq`, 'Reklama',"Kamunal", "Rag'batlantrish", "Boshqalar"],
          datasets: [{
              label: 'Employees',
              data:[oylik_all,soliq_all,reklama_all,kamunal_all, ragbatlantirish_all , boshqalar_all],
              backgroundColor: [
                  'rgba(41, 155, 99, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(120, 46, 139,1)',
                  'rgba(120, 46, 19,1)',
                  'rgba(30, 200, 109,05)'
              ],
              borderColor: [
                  'rgba(41, 155, 99, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(120, 46, 139,1)',
                  'rgba(120, 46, 19,1)',
                  'rgba(30, 200, 109,05)'
              ],
              borderWidth: 1
          }]
      },
      options: {
          responsive: true
      }
  });
  
  
  function createGroupDiagram(){
    group_diagramm_boxs.forEach(element => {
      let oylik=element.querySelector(".oylik").textContent;
      soliq=element.querySelector(".soliq").textContent;
      reklama=element.querySelector(".reklama").textContent;
      kamunal=element.querySelector(".kamunal").textContent;
      ragbatlantirish=element.querySelector(".ragbatlantirish").textContent;
      boshqalar=element.querySelector(".boshqalar").textContent;
      var ctxElement = element.querySelector(".doughnutBox").getContext('2d');
    
  
      var myChartElement = new Chart(ctxElement, {
      type: 'doughnut',
      data: {
          labels: ["Oylik","Soliq","Reklama","Kamunal","Ragbatlantirish","Boshqalar"],
          datasets: [{
              label: 'Employees',
              data: [oylik,soliq,reklama,kamunal,ragbatlantirish,boshqalar],
              backgroundColor: [
                'rgba(41, 155, 99, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(120, 46, 139,1)',
                'rgba(120, 46, 19,1)',
                'rgba(30, 200, 109,05)'
            ],
            borderColor: [
                'rgba(41, 155, 99, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(120, 46, 139,1)',
                'rgba(120, 46, 19,1)',
                'rgba(30, 200, 109,05)'
            ],  
              borderWidth: 1
          }]
      },
      options: {
          responsive: true
      }
  });
  
  
   });
  }
  createGroupDiagram()
    }