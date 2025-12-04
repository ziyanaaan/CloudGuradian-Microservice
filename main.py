from fastapi import FastAPI
from models import Product

app= FastAPI()

@app.get("/products")
def products():
	return products 
	

products=[
	Product(id=1,name="phone",quantity=20,price =5000),
	Product(id=2,name="laptop",quantity=40,price=6000)
]


@app.get("/products/{id}")
def getproducts(id: int):
	for Product in products:
		if Product.id==id:
			return Product
	return "Not found in Base"
		
	
@app.get("/")
def greet():
	return "hello this is server"

@app.post("/products")
def postproducts(product: Product):
	products.append(product)
	return product
