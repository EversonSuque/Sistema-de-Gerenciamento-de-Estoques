// Função para carregar produtos
async function loadProducts() {
    const response = await fetch('/get_products');
    const products = await response.json();
    const productList = document.getElementById('productList');
    productList.innerHTML = '';
    products.forEach(product => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${product[0]}</td>
            <td>${product[1]}</td>
            <td>${product[2]}</td>
            <td>${product[3]}</td>
        `;
        productList.appendChild(row);
    });
}

// Função para adicionar produto
document.getElementById('productForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const name = document.getElementById('productName').value;
    const price = parseFloat(document.getElementById('productPrice').value);
    const quantity = parseInt(document.getElementById('productQuantity').value);

    const response = await fetch('/add_product', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, price, quantity })
    });
    
    const result = await response.json();
    alert(result.message);
    loadProducts();
    this.reset();
});

// Carregar produtos ao iniciar
window.onload = loadProducts;
