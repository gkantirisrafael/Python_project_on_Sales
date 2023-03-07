import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Modified_Table.csv')

df1 = df.plot(x='zip_code' , y=['bottles_sold'],linestyle=":",marker='o')
plt.xlabel('Zip Code')
plt.ylabel('Bottles Sold')
plt.title('Bottles Sold per Zip Code')
plt.show()