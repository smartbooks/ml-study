
# 机器学习项目
- 管道：http://spark.apache.org/docs/latest/ml-pipeline.html
- 特征：http://spark.apache.org/docs/latest/ml-features.html
- 分类和回归：http://spark.apache.org/docs/latest/ml-classification-regression.html
- 聚类：http://spark.apache.org/docs/latest/ml-clustering.html
- 协同过滤：http://spark.apache.org/docs/latest/ml-collaborative-filtering.html
- 频繁模式挖掘：http://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html
- 模型参数选择和训练：http://spark.apache.org/docs/latest/ml-tuning.html
- 高级主题：http://spark.apache.org/docs/latest/ml-advanced.html

## ML-特征提取/转换/选择
```
Feature Extractors/特征提取
  TF-IDF
  Word2Vec
  CountVectorizer
Feature Transformers/特征转换
  Tokenizer|RegexTokenizer/文本句子转单词序列
  StopWordsRemover/移除停用词
  nn-gram/N元模型,评估两个字符串之间的差异程度,评估一个句子是否合理
  Binarizer/二值化
  PCA/主成分分析，降维
  PolynomialExpansion/多项式展开
  Discrete Cosine Transform (DCT)/离散余弦变换
  StringIndexer/编码字符串标签到数字标签
  IndexToString/解码数字标签到字符串标签
  OneHotEncoder/独热码,对分类型的特征进行独热码编码
  VectorIndexer
  Interaction/多列转1列向量,乘积
  Normalizer/正规化行特征
  StandardScaler/标准缩放
  MinMaxScaler/最大最小归一化
  MaxAbsScaler/绝对值归一化
  Bucketizer
  ElementwiseProduct
  SQLTransformer
  VectorAssembler/多列值转向量
  QuantileDiscretizer
  Imputer
Feature Selectors
  VectorSlicer
  RFormula
  ChiSqSelector
Locality Sensitive Hashing
  LSH Operations
    Feature Transformation
    Approximate Similarity Join
    Approximate Nearest Neighbor Search
  LSH Algorithms
    Bucketed Random Projection for Euclidean Distance
    MinHash for Jaccard Distance
```

## ML-分类和回归
```
Classification/分类
  Logistic regression/逻辑回归
    Binomial logistic regression/二分类逻辑回归
    Multinomial logistic regression/多分类逻辑回归
  Decision tree classifier/决策树分类
  Random forest classifier/随机森林分类
  Gradient-boosted tree classifier/梯度提升决策树分类
  Multilayer perceptron classifier/多层感知神经网络分类
  Linear Support Vector Machine/线性支持向量机分类
  One-vs-Rest classifier (a.k.a. One-vs-All)/一对多法分类
  Naive Bayes/朴素贝叶斯分类
Regression/回归
  Linear regression/线性回归
  Generalized linear regression/广义线性回归
    Available families
  Decision tree regression/决策树回归
  Random forest regression/随机森林回归
  Gradient-boosted tree regression/梯度提升决策树回归
  Survival regression/生存回归
  Isotonic regression/保序回归
  Linear methods/线性方法
  Decision trees/决策树
    Inputs and Outputs/输入和输出
      Input Columns/输入列
      Output Columns/输出列
  Tree Ensembles/树整合
    Random Forests/随机森林
      Inputs and Outputs/输入和输出
        Input Columns/输入列
        Output Columns (Predictions)/预测输出列
    Gradient-Boosted Trees (GBTs)/梯度提升树
      Inputs and Outputs/输入和输出
        Input Columns/输入列
        Output Columns (Predictions)/预测输出列
```

## ML-聚类
```
K-means
  Input Columns
  Output Columns
Latent Dirichlet allocation (LDA)
Bisecting k-means
Gaussian Mixture Model (GMM)
  Input Columns
  Output Columns
```

## ML-协同过滤
```
Collaborative filtering
  Explicit vs. implicit feedback
  Scaling of the regularization parameter
  Cold-start strategy
```

## ML-频繁模式挖掘
```
FP-Growth
```

## 基础概念
```
稠密矩阵/稀疏矩阵/向量/方差/标准差/均值/损失函数/
```

## 推荐系统
```
特征处理
偏好训练
排序函数
```

## HADOOP快速入门
```
Hadoop快速入门:
1.集群搭建和维护(CDH)
2.数据分析/挖掘(SparkSQL/RDD)
3.机器学习(SparkML)
4.实时计算(SparkStreaming)
5.图计算(SparkGraphx)

CDH提供的虚拟机镜像,可以快速上手使用：
https://www.cloudera.com/downloads/quickstart_vms/5-12.html

CDH标准集群安装程序，实际动手操练一下，把每个组件都安装一下（对机器性能要求很高）：
https://www.cloudera.com/downloads/manager/5-13-1.html

Spark官方的快速入门指南，一共8个主题介绍，是Spark的精髓，涵盖了当前所有的应用场景（要求倒背如流）：
http://spark.apache.org/docs/latest/quick-start.html
```

# 参考资料
- http://dblab.xmu.edu.cn/blog/spark/
