async function loadProducts() {

    try {

        const response = await fetch(
            "http://YOUR_LOADBALANCER_IP/products"
        );

        const products = await response.json();

        let html = "";

        products.forEach(product => {

            html += `
                <div class="card">
                    <h3>${product.name}</h3>
                    <p>Category: ${product.category}</p>
                    <p>Price: ₹${product.price}</p>
                </div>
            `;
        });

        document.getElementById("products").innerHTML = html;

    } catch (error) {

        document.getElementById("products").innerHTML =
            "<p>Unable to load products.</p>";
    }
}

async function loadRecommendations() {

    try {

        const response = await fetch(
            "http://YOUR_LOADBALANCER_IP/recommend/Mobile"
        );

        const data = await response.json();

        let html = "<ul>";

        data.recommendations.forEach(item => {
            html += `<li>${item}</li>`;
        });

        html += "</ul>";

        document.getElementById("recommendations").innerHTML = html;

    } catch (error) {

        document.getElementById("recommendations").innerHTML =
            "<p>Unable to load recommendations.</p>";
    }
}