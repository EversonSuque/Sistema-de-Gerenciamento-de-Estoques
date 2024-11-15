from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Inicializa o banco de dados
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL, quantity INTEGER)''')
    conn.commit()
    conn.close()

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para adicionar um produto
@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data['name']
    price = data['price']
    quantity = data['quantity']
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)', (name, price, quantity))
    conn.commit()
    conn.close()
    return jsonify({"status": "success", "message": "Produto adicionado com sucesso!"})

# Rota para buscar todos os produtos
@app.route('/get_products', methods=['GET'])
def get_products():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return jsonify(products)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
