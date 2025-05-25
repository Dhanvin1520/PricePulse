document.getElementById('track-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const url = document.getElementById('url').value;
    const email = document.getElementById('email').value;
    const target_price = document.getElementById('target_price').value;

    const response = await fetch('/track', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `url=${encodeURIComponent(url)}&email=${email}&target_price=${target_price}`
    });

    const data = await response.json();
    if (response.ok) {
        displayProduct(data);
        fetchProductData(data.product_id);
        if (email && target_price) {
            alert('Alert scheduled!');
        }
    } else {
        alert(data.error);
    }
});

async function fetchProductData(productId) {
    const response = await fetch(`/product/${productId}`);
    const data = await response.json();
    displayChart(data.prices);
}

function displayProduct(data) {
    const preview = document.getElementById('product-preview');
    preview.innerHTML = `
        <h2>${data.name}</h2>
        <img src="${data.image_url}" alt="${data.name}" width="100">
        <p>Current Price: ₹${data.current_price}</p>
    `;
}

function displayChart(prices) {
    const ctx = document.getElementById('price-chart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: prices.map(p => new Date(p.timestamp).toLocaleString()),
            datasets: [{
                label: 'Price (₹)',
                data: prices.map(p => p.price),
                borderColor: '#007bff',
                fill: false
            }]
        },
        options: {
            scales: {
                x: { title: { display: true, text: 'Time' } },
                y: { title: { display: true, text: 'Price (₹)' } }
            }
        }
    });
}