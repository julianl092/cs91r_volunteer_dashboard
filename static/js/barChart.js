new Chart(document.getElementById("myBarChart"), {
  type: "bar",
  data: {
    labels: ["-18", "18-24", "25-35", "36-45", "45+"],
    datasets: [
      {
        label: "Volunteers",
        backgroundColor: [
          "#3e95cd",
          "#8e5ea2",
          "#3cba9f",
          "#e8c3b9",
          "#c45850"
        ],
        data: [2478, 5267, 734, 784, 433]
      }
    ]
  },
  options: {
    legend: { display: false },
    title: {
      display: true,
      text: "Volunteers"
    }
  }
});
