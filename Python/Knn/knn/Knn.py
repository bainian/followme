from datetime import datetime
from os import listdir

from click._compat import raw_input
from numpy import array, zeros, shape, tile
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', "B", 'B']
    return group, labels


def file2matrix(filename):
    '''
    输入已笴样本数据
    :param filename:
    :return:
    '''
    fn = open(filename)
    content = fn.readlines()
    numLines = len(content)
    mat = zeros((numLines, 3))  # 值为0的N行3列的数组
    classLabelVector = []
    index = 0
    for line in content:
        line = line.strip()
        listFromLine = line.split('\t')
        mat[index, :] = listFromLine[0:3]  # 矩阵相当于二维数组
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return mat, classLabelVector


def autoNorm(dataSet):
    minVals = dataSet.min(0)  # 每一列最小值
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals  # 此处是三维，这两个值是最大值与最小值，范围
    m = dataSet.shape[0]  # 求 数组的 行数,求 数组的列数shape[1]
    normDataSet = dataSet - tile(minVals, (
        m, 1))  # tile 是将数组A重复n次，构成一个新的数组,这里产生一个m行，min列的新数组，可以理解为所有点与最小点的差，标准数据集,这里想当于一种 转换原点的做法。
    normDataSet = normDataSet / tile(ranges, (m, 1))  # 把原始数据集转换为一种百分比数据集
    return normDataSet, ranges, minVals


def classify0(inX, dataSet, labels, k):
    '''
    分类器
    :param inX: 用于被分类的单个输入测试向量，
    :param dataSet: 训练样本集
    :param labels: 训练样本集已知标签向量
    :param k: 邻近值
    :return:
    '''
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)  # axis=1表示按行相加 , axis=0表示按列相加
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()  # argsort函数返回的是数组值从小到大的索引值的排序
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]  # 距离排最小的点 对应 的label
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)  # 按出现的频度从大到小排列
    return sortedClassCount[0][0]  # 返回判断出的label, sortedClassCount为list

    pass


def datingClassTest():
    '''
    找到测试数据与样本数据的每个特征的最小距离（最小距离公式），找到前k个最小距离中标签出现频率最多的一项作为其分类标签，
    思考：如果不断以此标准来找出分类，会不会前期的训练对后期的影响太大了，导致后面越来越不准确？
    :return:
    '''
    hoRatio = 0.50  # 样本分界线
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')  # 得到数据值与标签值集合
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]  # 行数
    numTestVecs = int(m * hoRatio)  # 取测试集 500
    errorCount = 0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print('the classifier came back with: %d, the real answer is :%d' % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print('the total error rate is %f' % (errorCount / float(numTestVecs)))
    print('errorCount', errorCount)
    # 测试输入值
    resultList = ['not at all', 'insmall doses', 'in large doses']
    percenTats = float(raw_input("percentage of time spent playing video games?"))
    ffMiles = float(raw_input("frequent filter miles earned per year?"))
    iceCream = float(raw_input("liters of ice cream consumed per year?"))
    inArr = array([percenTats, ffMiles, iceCream])
    classifierResult = classify0((inArr - minVals) / ranges, normMat, datingLabels, 3)
    print('you will probably like this person', resultList[classifierResult - 1])


def img2vector(filename):
    '''
    把32 x 32变为 1 x 1024的一维
    :param filename:
    :return:
    '''
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        linestr = fr.readline().strip()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(linestr[j])
    return returnVect


# datingClassTest()

def handwritingClassTest():
    '''
    NumPy数组的维数称为秩（rank），一维数组的秩为1，二维数组的秩为2，以此类推。在NumPy中，每一个线性的数组称为是一个轴（axes），
    秩其实是描述轴的数量。比如说，二维数组相当于是一个一维数组，而这个一维数组中每个元素又是一个一维数组。所以这个一维数组就是NumPy中的轴（axes），
    而轴的数量——秩，就是数组的维数。

    k临近算法并不是最有效的算法，因为每个测试向量都要做1934次距离计算 ，而每次的距离计算包含1024个维度的浮点运算，还要为测试向量准备2M的在在存储空间，k决算树就是k近邻算法的优化版。
    另一个缺陷就是无法出任何数据的基础諅，无法知晓平均实例样本和典型实例样本的特征。
    :return:
    '''
    start = datetime.now().timestamp()
    hwLabels = []
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        filename = trainingFileList[i]
        classNumStr = int(filename.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('trainingDigits/%s' % filename)
    testFileList = listdir('testDigits')
    errorCount = 0
    mTest = len(testFileList)
    for i in range(mTest):
        filename = testFileList[i]
        numLabel = int(filename.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % filename)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 5)
        print('this classifier come back with %s, the real answer is %s' % (classifierResult, numLabel))
        if (classifierResult != numLabel): errorCount += 1
        print('the total number of errors is %d' % errorCount)
        print('the total error rate is :%s' % (errorCount / float(mTest)))
    print('Cost time %f' % (datetime.now().timestamp() - start))


handwritingClassTest()
