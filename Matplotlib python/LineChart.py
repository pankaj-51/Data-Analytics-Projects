import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,20,30,40,50]
plt.figure(figsize=[8,4])
plt.plot(x,y, marker='o', color='green', linestyle='--', linewidth='2', markersize='15')
plt.title("My first graph")
plt.xlabel("X-Axis (Numbers)")
plt.ylabel("Y-Axis (Values)")
plt.grid(True)
plt.show()


