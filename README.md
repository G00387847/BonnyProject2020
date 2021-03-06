# Fisher's Iris data set [3]

## Programming and Scripting

## Summary About Fisher's Iris Dataset

Ronald fisher is a British statistician biologist. He published fisher's Iris data set which also known as Anderson iris data set in 1936.The data set consist of 50 samples from 3 different types of irises(setosa, versicolour, virginica)Four faetures were measured from each sample:the length and the width of the sepal and petals in centimeters.

Based on the combination of these four features,fisher developed a linear discrimination of these four features, fisher developed a linear discrimination model to distinguish the species from each other.

Based on Fisher's linear discriminant model, this data set became a typical test case for many statistical classification techniques in machine learning such as support vector machines.[5]

The use of this data set in cluster analysis however is not common, since the data set only contains two clusters with rather obvious separation. One of the clusters contains Iris setosa, while the other cluster contains both Iris virginica and Iris versicolor and is not separable without the species information Fisher used. This makes the data set a good example to explain the difference between supervised and unsupervised techniques in data mining: Fisher's linear discriminant model can only be obtained when the object species are known: class labels and clusters are not necessarily the same.[6]

Nevertheless, all three species of Iris are separable in the projection on the nonlinear and branching principal component.[7] The data set is approximated by the closest tree with some penalty for the excessive number of nodes, bending and stretching. Then the so-called "metro map" is constructed.[4] The data points are projected into the closest node. For each node the pie diagram of the projected points is prepared. The area of the pie is proportional to the number of the projected points. It is clear from the diagram (left) that the absolute majority of the samples of the different Iris species belong to the different nodes. Only a small fraction of Iris-virginica is mixed with Iris-versicolor (the mixed blue-green nodes in the diagram). Therefore, the three species of Iris (Iris setosa, Iris virginica and Iris versicolor) are separable by the unsupervising procedures of nonlinear principal component analysis. To discriminate them, it is sufficient just to select the corresponding nodes on the principal tree.
There are 5 attribute and 150

![Capture1.PNG](https://github.com/G00387847/BonnyProject2020/blob/master/Images/Capture1.PNG)
![Capture2.PNG](https://github.com/G00387847/BonnyProject2020/blob/master/Images/Capture2.PNG)
![Capture3.PNG](https://github.com/G00387847/BonnyProject2020/blob/master/Images/Capture3.PNG)

## Python code
 This python program call Analysis.py
 output a summary of each variable to a single text file and
 Save a histogram of each variable to png files and
 Output a scatter plot of each pair of variables
 I also import pandas as pd to read csv file and matplotlib to plot graph

## import libraries
import pandas as pd
import matplotlib.pyplot as plt

## Reading file from url
df = pd.read_csv("https://raw.githubusercontent.com/gchoi/Dataset/master/OldFaithful.csv")

## Scatter plot output
plt.plot(df["TimeEruption"],df["TimeWaiting"],'b.')
plt.title("scatter plot")
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
plt.clf()

## Save Histogram TimeEruption plot to png file
plt.hist(df["TimeEruption"])
plt.title("Histogram TimeEruption")
plt.show()
plt.savefig("TimeEruption")
plt.clf()

## Save Histogram TimeWaiting plot to png file
plt.hist(df["TimeWaiting"])
plt.title("Histogram TimeWaiting")
plt.show()
plt.savefig("TimeWaiting")



Reference - https://en.wikipedia.org/wiki/Iris_flower_data_set
                     
Reference - https://github.com/richardfeeney7/FisherIrisDataSetProject
                  
Reference - https://github.com/RitRa/Project2018-iris
           


        
        


         

