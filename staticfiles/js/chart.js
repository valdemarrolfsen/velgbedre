$(function(){
  $("#doughnutChart").drawDoughnutChart([
    { title: "Tokyo",         value : 70,  color: "#2C3E50" },
    { title: "Berlin",        value : 30,   color: "#FFF" }
  ]);
});

$(function(){
  $("#doughnutChart2").drawDoughnutChart([
    { title: "Tokyo",         value : 50,  color: "#2C3E50" },
    { title: "Berlin",        value : 50,   color: "#FFF" }
  ]);
});