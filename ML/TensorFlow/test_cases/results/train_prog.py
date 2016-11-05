import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

data = pd.read_csv("../models/xor_nn_2.csv");
print(data);

grp = data[data.epoch < 200];
#data[data.epoch > 130].plot(x="epoch", y="cost")
#data[data.epoch > 130].plot(x="epoch", y="accuracy")



fig, ax = plt.subplots()
ax = grp.plot(ax=ax, kind='line', x='epoch', y='cost')
ax = grp.plot(ax=ax, kind='line', x='epoch', y='accuracy')
lines, _ = ax.get_legend_handles_labels()



plt.show()