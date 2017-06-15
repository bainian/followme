import random

from numpy import *


def loadDataset(filename):
    dataMat = []
    labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat, labelMat


def selectJrand(i, m):
    j = i
    while (j == i):
        j = int(random.uniform(0, m))
    return j


def clipAlpha(aj, H, L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj


def smoSimple(dataMatIn, classLabels, C, toler, maxIter): #五个输入函数，数据集 类别标签 常数C 容错率 取消前迭代次数
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    b = 0
    m, n = shape(dataMatrix) #得到常数项n m
    alphas = mat(zeros((m, 1))) #构建alpha列矩阵，矩阵中元素都初始化为0，并建立一个iter变量
    iter = 0
    while (iter < maxIter): #如果alpha可以更改 进入优化过程  当变量iter达到输入值maxItem时，函数结束运行并退出
        alphaPairsChanged = 0
        for i in range(m):
            fXi = float(multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[i, :].T)) + b
            Ei = fXi - float(labelMat[i])
            if ((labelMat[i] * Ei < -toler) and (alphas[i] < C)) or ((labelMat[i] * Ei > toler) and (alphas[i] > 0)):
                j = selectJrand(i, m)
                fXj = float(multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[j, :].T)) + b
                Ej = fXj - float(labelMat[j])
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
                if (labelMat[i] != labelMat[j]):
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0,alphas[j] + alphas[i] -C)
                    H = min(C, alphas[j] + alphas[i])
                if L == H:
                    print('L == H')
                    continue


dataArr, labelArr = loadDataset('testSet.txt')
print(dataArr)
print('-' * 30)
print(labelArr)
