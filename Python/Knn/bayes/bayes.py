import re
from numpy import *


def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 人工标注1为侮辱性语言
    return postingList, classVec


def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet.union(document)  # 并集，按位或
    return list(vocabSet)


def setOfWord2Vec(vocabList, inputSet):  # 词汇表 文档表
    '''
    转换为词向量
    :param vocabList: 训练集的词汇表
    :param inputSet: 输入的语句词组
    :return: 语句对应的向量列表
    '''
    returnVec = [0] * len(vocabList)  # 初始化一个值为0长度为词汇表长度的list
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1  # 当输入词句词在词汇表中出现了，把list对应的位置 标为1,成为特征向量
        else:
            print('the word %s is not in my Vocabulary!' % word)
    return returnVec


def bagOfWords2VecMN(vocabList, inputSet):
    '''
    词袋模型 bag of words model,考虑每个词出现的次数
    :param vocabList:
    :param inputSet:
    :return:
    '''
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec


def trainNBO(trainMatrix, trainCategory):
    '''
    训练方法：词集模型，以每个词是否出现 为一个特征，set of  words  model
    :param trainMatrix: 词汇表长度的词向量列表list
    :param trainCategory: 每段文档 的真实01标签
    :return:
    '''
    numTrainDocs = len(trainMatrix)  # 有多少行
    numWords = len(trainMatrix[0])  # 每行词汇向量的长度
    pAbusive = sum(trainCategory) / float(numTrainDocs)  # 侮辱语句/总语句 = 3/6 = 0.5
    p0Num = ones(numWords)  # 将所有值初始化为1,分子
    p1Num = ones(numWords)
    p0Denom = 2.0  # 将所有值初始化为2,分母，这样计算出的概率对结果 没有影响 但是却可以规避分子为0时的影响，
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num / p1Denom)  # 由于 有极小值的影响，这里将取自然对数，其与一般的函数有相同 的极大极大值极小值趋势，不影响 最终结果
    p0Vect = log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    '''
    核心思想 就是测试语句词出现在两伙向量中的次数（概率），取概率大的那个
    :param vec2Classify: 要测试的数字词向量
    :param p0Vec: 训练集返回的非侮辱词本概率集合
    :param p1Vec: 侮辱词的概率集合
    :param pClass1: 训练集中出现侮辱词的概率
    :return: 哪个概率大，判断为哪 种
    '''
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)  # 对数概率
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def testingNB():
    '''
    bayes分类的原理，这里是以每个词是否出现为依据，
    :return:
    '''
    listOPosts, listClasses = loadDataSet()  # 返回list表示的语句列表和相应的标签值，此为训练数据
    myVocabList = createVocabList(listOPosts)  # 创建所有语句的单词表set
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWord2Vec(myVocabList, postinDoc))  # list中装各个语句的词汇表长度的词向量列表
    p0v, p1v, pAb = trainNBO(array(trainMat), array(listClasses))

    print('p0v:%s\np1v:%s\npAb:%s' % (p0v, p1v, pAb))
    testEntry = ['love', 'my', 'dog', 'dalmation', 'big']
    thisDoc = array(setOfWord2Vec(myVocabList, testEntry))
    print('test array ', thisDoc)
    print(testEntry, 'classified as:', classifyNB(thisDoc, p0v, p1v, pAb))

    testEntry = ['stupid', 'garbags']
    thisdoc = array(setOfWord2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as:', classifyNB(thisdoc, p0v, p1v, pAb))


# listOPosts, listClasses = loadDataSet()
# myVocabList = createVocabList(listOPosts)
# print(myVocabList)
# vec = setOfWord2Vec(myVocabList, listOPosts[0])
# print(vec)

# testingNB()

def textParse(bigString):
    listOfToken = re.split('\W+', bigString)
    return [k.lower() for k in listOfToken if len(k) > 2]


def spamTest():
    docList = []
    classList = []
    fullText = []
    for i in range(1, 26):
        wordList = textParse(open('email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)

        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    trainingSet = list(range(50))
    testSet = []
    for i in range(10):
        uniform = random.uniform(0, len(trainingSet))
        randIndex = int(uniform)
        testSet.append(trainingSet[randIndex])
        del trainingSet[randIndex]
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0v, p1v, pSpam = trainNBO(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0v, p1v, pSpam) != classList[docIndex]:
            errorCount += 1
            # print('classification error', docList[docIndex])
    return float(errorCount) / len(testSet)


rateCount = 0
for i in range(10):
    rate = spamTest()
    print(rate, end=' ')
    rateCount += rate
print('\nthe 10 times rate val is :', rateCount / 10)
