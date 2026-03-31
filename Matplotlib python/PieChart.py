import matplotlib.pyplot as plt
categories = ["A","B","C","D","E"]
sales= [10,20,30,40,50]

plt.pie(sales, labels=categories, autopct='%1.1f%%', startangle=45)
plt.title("My Pie Chart")
plt.show()