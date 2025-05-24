document.getElementById("urlForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const urlInput = document.getElementById("urlInput").value;

  const response = await fetch("/submit-url", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: `url=${encodeURIComponent(urlInput)}`
  });

  const data = await response.json(); 
  document.getElementById("productPreview").innerHTML = `
    <img src="${data.image}" alt="Product Image" style="width:150px;">
    <h3>${data.title}</h3>
    <p>Price: ${data.price}</p>
  `;

  loadPriceChart();
});

let chart; 

async function loadPriceChart() {
  const res = await fetch("/history");
  const data = await res.json();

  const labels = data.map(entry => new Date(entry.timestamp)); // Convert to Date
  const prices = data.map(entry => parseFloat(entry.price.replace(/[₹,]/g, '')) || 0);

  const ctx = document.getElementById("priceChart").getContext("2d");

  if (chart) chart.destroy();

  chart = new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [{
        label: "Price History",
        data: prices,
        borderColor: "#3498db",
        fill: false,
        tension: 0.1
      }]
    },
    options: {
      responsive: true,
      scales: {
        x: {
          type: 'time',
          time: {
            tooltipFormat: 'MMM d, yyyy HH:mm',
            unit: 'hour',
            displayFormats: {
              hour: 'MMM d, hA'
            }
          },
          title: {
            display: true,
            text: 'Timestamp'
          }
        },
        y: {
          title: {
            display: true,
            text: 'Price (INR)'
          },
          ticks: {
            callback: function(value) {
              return '₹' + value.toLocaleString(); // Format y-axis values
            }
          }
        }
      },
      plugins: {
        title: {
          display: true,
          text: 'Product Price Over Time'
        }
      }
    }
  });
}