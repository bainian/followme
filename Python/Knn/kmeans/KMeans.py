from numpy import *
import matplotlib.pyplot as plt


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
    '''
    算法步骤：
    生成随机质心cent
    如果有点的簇分配变化changed则死循环：
        遍历每个点（80 x 2）:
            遍历每个cent(4 x 2):
            求每个cent质心与此点间距 ，选择最小间距记录进cluster(80 x 2)
            如果此点的质心变化，则 changed为true
            记录此点的 质心索引与间距平方值
        遍历每个cent(4 x 2):
        找出每个质心下面的对应原数据
        发列为准求平均值生成对应索引的新的质心点并更新质心集合cent
    如果有点的簇分配变化changed则再循环。

    误差平方和SSE最小的是最好的划分手段

    :param dataSet:  原数据
    :param k:  分为的簇数
    :param distMeans:  求距离
    :param createCent:  根据原数据随机生成质心（最小值加范围间距的随机值）
    :return: 质心坐标，每个点的质心分布情况
    '''
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m, 2)))  # 簇分配结果矩阵，第一列索引，第二列误差（当前点到质心的距离）
    centroids = createCent(dataSet, k)  # 分配 一个原始的质点
    print('centroids = ', centroids)
    plt_dots(centroids)
    clusterChanged = True  # 数据簇分配结果变化与否
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
                clusterChanged = True  # 只要有一次的变化 就改变为true了，不变的不会来此处改变
            clusterAssment[i, :] = minIndex, minDist ** 2
        print('centroids = ', centroids)
        for cent in range(k):
            a_cent = clusterAssment[:, 0].A == cent  # .A 把这一列转为ndarray
            iterable = nonzero(a_cent)  # 生成行索引与列索引
            ptsInClust = dataSet[iterable[0]]  # 取行索引得到 真实
            centroids[cent, :] = mean(ptsInClust, axis=0)
    return centroids, clusterAssment


def biKmeans(dataSet, k, distMeans=distEclud):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m, 2)))
    centroid0 = mean(dataSet, axis=0).tolist()[0]
    centList = [centroid0]
    for j in range(m):
        clusterAssment[j, 1] = distMeans(mat(centroid0), dataSet[j, :]) ** 2
    while (len(centList) < k):
        lowestSSE = inf
        for i in range(len(centList)):
            ptsInCurrCluster = dataSet[nonzero(clusterAssment[:, 0].A == i)[0], :]
            centroidMat, splitClustAss = kMeans(ptsInCurrCluster, 2, distMeans)
            sseSplit = sum(splitClustAss[:, 1])
            sseNotSplit = sum(clusterAssment[nonzero(clusterAssment[:, 0].A != i)[0], 1])
            print('sseSplit, and NotSplit: ', sseSplit, sseNotSplit)
            if sseSplit + sseNotSplit < lowestSSE:
                bestCentToSplit = i
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowestSSE = sseSplit + sseNotSplit
        bestClustAss[nonzero(bestClustAss[:, 0].A == 1)[0], 0] = len(centList)
        bestClustAss[nonzero(bestClustAss[:, 0].A == 0)[0], 0] = bestCentToSplit
        print('the bestCenToSplit is :', bestCentToSplit)
        print('the len of bestClustAss is : ', len(bestClustAss))
        centList[bestCentToSplit] = bestNewCents[0, :].tolist()[0]
        centList.append(bestNewCents[1, :].tolist()[0])
        clusterAssment[nonzero(clusterAssment[:, 0].A == bestCentToSplit)[0], :] = bestClustAss
    return mat(centList), clusterAssment


def plt_dots(dots):
    if isinstance(dots, matrix):
        dots = dots.A
    x = dots[:, 0]
    y = dots[:, 1]
    T = arctan2(x, y)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)  # 3行1 列，第一位置（左到右，上到下数）， 各个add_subplot独立
    plt.scatter(x, y, c=T, s=25, alpha=0.4, marker='o')
    # T:散点的颜色
    # s：散点的大小
    # alpha:是透明程度
    plt.title('k-means dot plt')
    plt.grid('on')
    plt.show()


data_set = loadDataSet('testSet.txt')
dataMat = mat(data_set)
print(min(dataMat[:, 0]))
re = randCent(dataMat, 2)
print(re)
dist = distEclud(dataMat[0], dataMat[1])
print(dist)
myCentroids, culstAssing = kMeans(dataMat, 4)
print(myCentroids, culstAssing)

plt_dots(dataMat)
