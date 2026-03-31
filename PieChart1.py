import matplotlib.pyplot as plt
# Data
activities = ['Python','SQL','Excel','Power BI']
slices = [40,25,20,15]
colors = ['gold','yellowgreen','lightcoral','lightskyblue']

# Plotting
plt.pie(slices, labels=activities, colors=colors, startangle=140, autopct='%1.1f%%')
plt.title("My Learning Focus")
plt.show()