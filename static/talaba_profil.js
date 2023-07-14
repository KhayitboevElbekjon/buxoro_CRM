{
  let alo=document.querySelector(".alo").textContent,
   yomon=document.querySelector(".yomon").textContent,
   past=document.querySelector(".past").textContent,
   yaxshi=document.querySelector(".yaxshi").textContent;

  
  var ctx2 = document.getElementById('doughnut').getContext('2d');
var myChart2 = new Chart(ctx2, {
    type: 'doughnut',
    data: {
        labels: [`A'lo`, `Yaxshi`, 'Past',"Yomon",],
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
}