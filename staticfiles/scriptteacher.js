{
    group_diagramm_boxs =document.querySelectorAll(".group_diagramm_box")
    
    // console.log(group_diagramm_boxs);
     
    let ctx = document.getElementById('lineChart').getContext('2d');
    let oylik =document.querySelectorAll(".oylik"),
    talabaSoni =document.querySelectorAll(".talabaSoni")
    console.log(talabaSoni[1].textContent , oylik);
    let  arr_oylik =[] ,arr_talabaSoni= []; 
    function setvalue(getelement,setvalue){
      for (let i = 0; i < getelement.length; i++) {
      const element = getelement[i]
      setvalue.push(element.textContent)
    }
    }
  
  setvalue(oylik,arr_oylik)
  setvalue(talabaSoni ,arr_talabaSoni )
  console.log(arr_oylik ,arr_talabaSoni);
  
  
  let myChart = new Chart(ctx, {
      type: 'line',
      data: {
          labels: [1 ,2,3,4,5,6,7,8,9,10,11,12],
          datasets: [{
              label: 'Oylik daromadi (000 ga qisqartirilgan)',
              data: arr_oylik,
             
              backgroundColor: [
                  'rgba(85,85,85, 1)'
              ],
              borderColor: 'rgb(41, 155, 99)',
              borderWidth: 1
          },
          {
              label: `O'quvchi soni`,
              data: arr_talabaSoni,
             
              backgroundColor: [
                  'rgba(85,85,85, 1)'
              ],
              borderColor: 'rgb(41, 155, 99)',
              borderWidth: 1
          }
        ]
      },
      options: {
          responsive: true
      }
  });
  
  var ctx2 = document.getElementById('doughnut').getContext('2d');
  alo_all=document.querySelector(".alo_all").textContent,
      yaxshi_all=document.querySelector(".yaxshi_all").textContent,
      past_all=document.querySelector(".past_all").textContent,
      yomon_all=document.querySelector(".yomon_all").textContent;
      
  var myChart2 = new Chart(ctx2, {
    
      type: 'doughnut',
      data: {
          labels: [`A'lo`, `Yaxshi`, 'Past',"Yomon",],
          datasets: [{
              label: 'Employees',
              data:[alo_all,yaxshi_all,past_all,yomon_all],
              backgroundColor: [
                  'rgba(41, 155, 99, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(120, 46, 139,1)',
                  'rgba(120, 46, 19,1)'
              ],
              borderColor: [
                  'rgba(41, 155, 99, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(120, 46, 139,1)',
                  'rgba(120, 46, 19,1)'
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
      let alo=element.querySelector(".alo").textContent;
      yaxshi=element.querySelector(".yaxshi").textContent;
      past=element.querySelector(".past").textContent;
      yomon=element.querySelector(".yomon").textContent;
      var ctxElement = element.querySelector(".doughnutBox").getContext('2d');
    
  
      var myChartElement = new Chart(ctxElement, {
      type: 'doughnut',
      data: {
          labels: [`A'lo`, `Yaxshi`, 'Past',"yomon",],
          datasets: [{
              label: 'Employees',
              data: [alo,yaxshi,past,yomon],
              backgroundColor: [
                  'rgba(41, 155, 99, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(120, 46, 139,1)',
                  'rgba(120, 46, 19,1)'
              ],
              borderColor: [
                  'rgba(41, 155, 99, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(120, 46, 139,1)',
                  'rgba(120, 46, 19,1)'
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