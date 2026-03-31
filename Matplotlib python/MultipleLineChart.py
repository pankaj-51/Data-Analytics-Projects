import matplotlib.pyplot as plt
x= [1,2,3,4,5]
y1 = [20,30,60,90,120]
y2= [30,40,60,80,100]

plt.plot(x, y1, label="Sales 2024", marker="o", color="green", linestyle=":")
plt.plot(x, y2, label="Sales 2025", marker="P", color="Blue", linestyle="--")

plt.title("Year on Year Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)

plt.legend()
plt.show()