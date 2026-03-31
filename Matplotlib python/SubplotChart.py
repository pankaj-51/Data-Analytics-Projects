import matplotlib.pyplot as plt
# Data-1 : Bar Chart
categories = ["Mon","Tue","Wed","Thu","Fri"]
sales= [10,20,30,40,50]

#Data-2 : Scatter Chart
y1=[10,20,25,35,45]
y2=[20,30,35,45,55]

plt.figure(figsize=(10,4))

#first plot: Bar Chart
plt.subplot(1,2,1) # (Row, Column, Position)
plt.bar(categories, sales)
plt.title("Weekly Sales")
plt.xlabel("Week Days")
plt.ylabel("Sales")

#first plot: scatter Chart
plt.subplot(1,2,2) # (Row, Column, Position)
plt.scatter(y1, y2)
plt.title("User Examples")
plt.xlabel("User1")
plt.ylabel("User2")

plt.show()

