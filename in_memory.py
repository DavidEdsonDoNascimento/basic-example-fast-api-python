from product import Product

def get_products():
  products = []
  
  for x in [1,2,3]:
    product = Product(name = f"Product {x + 1}", price = 4.9 * x, status = x % 2 == 0)
    products.append(product)
  
  return products