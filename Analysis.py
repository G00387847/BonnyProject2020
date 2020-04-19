# Bonny Chimezie Nwosu
# Writing python program call Analysis.py
# That output a summary of each variable to a single text file
# Save a histogram of each variable to png files
# Output a scatter plot of each pair of variables

# import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Reading file from url
df = pd.read_csv("https://raw.githubusercontent.com/gchoi/Dataset/master/OldFaithful.csv")

# Scatter plot output
plt.plot(df["TimeEruption"],df["TimeWaiting"],'b.')
plt.title("scatter plot")
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
plt.clf()

# Save Histogram TimeEruption plot to png file
plt.hist(df["TimeEruption"])
plt.title("Histogram TimeEruption")
plt.show()
plt.savefig("TimeEruption")
plt.clf()

# Save Histogram TimeWaiting plot to png file
plt.hist(df["TimeWaiting"])
plt.title("Histogram TimeWaiting")
plt.show()
plt.savefig("TimeWaiting")




