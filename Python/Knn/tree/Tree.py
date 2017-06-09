import operator
from math import log


def calcShannonEnt(dataSet):
    '''
    计算熵值，熵表示一集合中物质的混乱程度，这里用到的公式 h = -E p(x) log(2^p(x))
    所有标签参与运算得出一个值
    :param dataSet:
    :return:
    '''
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    print('\t计算%s中的标签熵值%s' % (dataSet, shannonEnt))
    return shannonEnt


def createDataSet():
    dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no'], [0, 1, 'no'], [1, 1, 'yes']]
    labels = ['no sufacing', 'flippers']
    return dataSet, labels


def splitDataSet(dataSet, axis, value):
    '''
    第一个特征，值为value的求出一个sub集合，然后还会再分这个集合
    :param dataSet:
    :param axis:
    :param value:
    :return:
    '''
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    bestEntropy = calcShannonEnt(dataSet)
    print('dataSet标签熵值：', bestEntropy)
    bestInfoGain = 0.0
    bestFeature = -1
    print('dataSet共有特征%d个' % numFeatures)
    for i in range(numFeatures):
        featList = [e[i] for e in dataSet]
        print("\t第%d个特征值列表为：%s" % (i, featList))
        uniqueVals = set(featList)
        print('\t精减重复特征值后为：', uniqueVals)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            print('\t\t按照第%s个特征的特征值%s提取子集：%s' % (i, value, subDataSet))
            prob = len(subDataSet) / float(len(dataSet))
            print('\t\t子集数目%s占总数%s比率：%s' % (len(subDataSet), len(dataSet), prob))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = bestEntropy - newEntropy
        print('\t第%s特征熵增为本特征标签熵与全局标签熵之差：%s' % (i, infoGain))
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    print('选取的最好的熵增为：', bestFeature)
    return bestFeature


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    print('各个值出现的次数从大到小排列：', sortedClassCount)
    return sortedClassCount


def createTree(dataSet, labels):
    '''
    这里的dataset都 是一个list
    ID3算法
    :param dataSet:
    :param labels:
    :return:
    '''
    classList = [e[-1] for e in dataSet]
    if classList.count(classList[0]) == len(classList):
        print('所有值都是相同的，返回值：', classList[0])
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    featValues = [e[bestFeat] for e in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        data_set = splitDataSet(dataSet, bestFeat, value)
        myTree[bestFeatLabel][value] = createTree(data_set, subLabels)
    print('myTree:', myTree)
    return myTree


myDat, myLabel = createDataSet()
# aa = [[0, 1, 'no'], [0, 1, 'no']]
# bb = [[1, 'maybe'], [1, 'yes'], [0, 'no']]
# print('bb clac:', calcShannonEnt(bb))
# print('aa clac:', calcShannonEnt(aa))
# print(myDat)
# print(calcShannonEnt(myDat))
# myDat[0][-1] = 'maybe'
# print(myDat)
# print(calcShannonEnt(myDat))
# print('splitdataset：', splitDataSet(myDat, 0, 1))
# print('chooseBestSplit:', chooseBestFeatureToSplit(myDat))

createTree(myDat, myLabel)
