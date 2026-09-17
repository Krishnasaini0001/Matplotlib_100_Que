import matplotlib.pyplot as plt

products = ["Laptop", "Mobile", "Tablet", "Watch", "Headphone"]
sales = [85, 150, 70, 110, 130]

plt.barh(products, sales)

plt.title("Product Sales")
plt.xlabel("Units Sold")
plt.ylabel("Products")
plt.show()