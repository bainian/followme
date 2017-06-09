from  numpy import *
import matplotlib.pyplot as plt


def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat


def sigmoid(inX):
    '''
    sigmoid函数,
    :param inX: 输入值，
    :return: 0-1之间的数
    '''
    return 1.0 / (1 + exp(-inX))


def gradAscent(dataMatIn, classLabels):
    '''
    梯度上升算法求每个特征的回归系数值，,一次全部处理，批处理
    :param dataMatIn:
    :param classLabels:
    :return:
    '''
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    m, n = dataMatrix.shape
    alpha = 0.001
    maxCycles = 500
    weights = ones((n, 1))
    for k in range(maxCycles):
        matrix_weights = dataMatrix * weights  # 两个 ndarray有时候 相告乖会报错，这时候 用matrix主为矩阵相乖就好了，或者使用dot，但是一个matrix与一个ndarray就不会出错
        h = sigmoid(matrix_weights)
        error = (labelMat - h)
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights


def plotBestFit(weights):
    dataMat, labelMat = loadDataSet()
    dataArr = array(dataMat)
    n = dataArr.shape[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)  # 子图，投射方式 ，1，1，1为极坐标方式
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')  # s 绽放，c 颜色 ，market速记标识 ，默认0
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = mat(arange(-3.0, 3.0, 0.1))  # 等 差数列，起始值，终值，公差
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


def stocGradAscent0(dataMatrix, classLabels):
    m, n = shape(dataMatrix)
    alpha = float64(0.01)
    weights = ones(n)
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i] * weights))
        error = (classLabels[i] - h)
        weights = weights + alpha * error * float64(dataMatrix[i])
    return weights


def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    m, n = shape(dataMatrix)
    weights = ones(n)
    for j in range(numIter):
        dataIndex = list(range(m))
        for i in range(m):
            alpha = 4 / (1.0 + j + i) + 0.0001
            randIndex = int(random.uniform(0, len(dataIndex)))
            h = sigmoid(sum(dataMatrix[randIndex] * weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * float64(dataMatrix[randIndex])
            del (dataIndex[randIndex])
    return weights


ascent = gradAscent(*loadDataSet())
ascent0 = stocGradAscent0(*loadDataSet())
ascent1 = stocGradAscent1(*loadDataSet())
print('weight = ', ascent)
print('weight0 = ', ascent0)
print('weight1 = ', ascent1)
plotBestFit(ascent)
plotBestFit(ascent0)
plotBestFit(ascent1)
