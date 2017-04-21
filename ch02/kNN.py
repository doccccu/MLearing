import numpy as np
import operator
import matplotlib
import matplotlib.pyplot as plt


def createDataSet():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def draw():
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    print datingDataMat
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
    plt.show()


def file2matrix(filename):
    fr = open(filename)
    arrayOfLines = fr.readlines()
    numberOflines = len(arrayOfLines)
    returnMat = np.zeros((numberOflines, 3))
    classLabelVector = []
    index = 0
    name_dict = {'largeDoses': 3, 'smallDoses': 2, 'didntLike': 1}
    for line in arrayOfLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0: 3]
        classLabelVector.append(int(name_dict[listFromLine[-1]]))
        index += 1
    return returnMat, classLabelVector


if __name__ == '__main__':
    draw()
