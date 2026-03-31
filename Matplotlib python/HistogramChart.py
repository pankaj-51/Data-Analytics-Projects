import matplotlib.pyplot as plt
import random
data= [random.randint(1,50) for _ in range(100)]

plt.hist(data, bins=20)
plt.title("Histagram Example")
plt.show()