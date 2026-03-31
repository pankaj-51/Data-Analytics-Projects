import matplotlib.pyplot as plt
import pandas as pd

data={'Month' : ['Jan','Feb','Mar','Apr'],
      'Sales' : [12000, 14000, 18000, 25000] 
     }

df=pd.DataFrame(data)
print(df)

plt.bar(df['Month'], df['Sales'])
plt.title("Matplotlib With Pandas")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.savefig(r"Monthly_Sales_From_df.jpg")  # for save the file or chart
plt.show()
