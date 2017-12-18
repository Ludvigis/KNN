import math
import matplotlib.pyplot as plt

def euclidian_distance(a,b):
    return math.sqrt((a[0] - b[0])**2 + (a[1]-b[1])**2)

def knn(k):
    dataset = getDataSet("C:\\Users\\Ludvig\\Desktop\\iris.data.txt")
    #split data into training data and test data...
    x = dataset.sepal_length
    y = dataset.sepal_width
    colors = []
    for c in dataset.iris_type:
        if(c == "Iris-setosa"):
            colors.append('green')
        if(c == "Iris-versicolor"):
            colors.append('red')
        if(c == "Iris-virginica"):
            colors.append('blue')
    
    plt.scatter(x,y,10,colors)
    plt.ylabel('sepal width')
    plt.xlabel('sepal length')
    plt.show()

def getDataSet(fileName):
    f = open(fileName,"r")
    lines = f.read().split('\n')
    dataset = dataSet()
    for line in lines:
        cat = line.split(',')
        if(line!=""):
            dataset.sepal_length.append(cat[0])
            dataset.sepal_width.append(cat[1])
            dataset.petal_length.append(cat[2])
            dataset.petal_width.append(cat[3])
            dataset.iris_type.append(cat[4])
    return dataset
    
class dataSet:  #in cm
    sepal_length = []  
    sepal_width = []
    petal_length = []
    petal_width = []
    iris_type = []
plt.rcParams['toolbar'] = 'None'    
knn(3)


