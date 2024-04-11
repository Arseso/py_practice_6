import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

trees = pd.read_csv("./data/trees.csv", index_col = "ID")
fig, axs = plt.subplots(2)
axs[0].sb.Plot(trees, x="species").add(so.Bar(), so.Hist())
axs[1].plot(x, -y)


plt.barplot
