from flask import render_template
from Saleapp import app, untils

@app.route("/")
def index():

    categories = untils.read_data()

    return render_template("index.html",
                           categories=categories)

@app.route('/products')
def product_list():
    products = untils.read_data(path="data/products.json")
    return render_template("product.html",
                           products=products)
@app.route('/products/<int:products_id>')
def product_details(product_id):
    product = untils.get_product_byid(product_id=product_id)
    return render_template('product-details.html',
            product=product)
if __name__ == "__main__":
    app.run(debug=True)