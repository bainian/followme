from numpy import *


def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curline = line.strip().split('\t')
        fltLine = list(map(float, curline))
        dataMat.append(fltLine)
    print('load dataMat shape:', shape(dataMat))
    return dataMat


def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))


def randCent(dataSet, k):
    '''
    shape为(k, n)的值为0的mat，把每个特征列的最小值加一个范围内的随机数赋给这个mat
    :param dataSet:
    :param k:
    :return:
    '''
    n = shape(dataSet)[1]
    centroids = mat(zeros((k, n)))
    for j in range(n):
        minj = min(dataSet[:, j])
        rangeJ = float(max(dataSet[:, j]) - minj)
        centroids[:, j] = mat(minj + rangeJ * random.rand(k, 1))
    return centroids


def kMeans(dataSet, k, distMeans=distEclud, createCent=randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m, 2))) # 簇分配结果矩阵，第一列索引，第二列误差（当前点到质心的距离）
    centroids = createCent(dataSet, k) # 分配 一个原始的质点
    clusterChanged = True # 数据簇分配结果变化与否
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf
            minIndex = -1
            for j in range(k):
                distJI = distMeans(centroids[j, :], dataSet[i, :])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist ** 2
        print('centroids = ', centroids)
        for cent in range(k):
            ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]
            centroids[cent, :] = mean(ptsInClust, axis=0)
    return centroids, clusterAssment


data_set = loadDataSet('testSet.txt')
dataMat = mat(data_set)
print(min(dataMat[:, 0]))
re = randCent(dataMat, 2)
print(re)
dist = distEclud(dataMat[0], dataMat[1])
print(dist)
myCentroids, culstAssing = kMeans(dataMat, 4)
print(myCentroids, culstAssing)
