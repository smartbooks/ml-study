# ml-study
关于机器学些的快速示例

# 知识体系
- 日志采集:[flume](http://flume.apache.org),[logstash](https://www.elastic.co/cn/products/logstash)
- 消息队列:[kafka](http://kafka.apache.org),[ActiveMQ](http://activemq.apache.org)
- 爬虫采集:[Scrapy](https://scrapy.org)
- 数据清洗:[Kettle](https://community.hds.com/docs/DOC-1009855),[DataX](https://github.com/alibaba/DataX),[Spark](http://spark.apache.org)
- 任务调度:[Oozie](http://oozie.apache.org/)
- 分布式内存文件系统:[tachyon](https://www.alluxio.org)
- 倒排索引:[Lucene](https://lucene.apache.org/),[Elasticsearch](https://www.elastic.co/cn/products/elasticsearch)
- 中文分词:[Jcseg](https://github.com/lionsoul2014/jcseg)
- 高速缓存:[redis](https://redis.io),[memcached](https://www.memcached.org),[twemproxy](https://github.com/twitter/twemproxy),[HBase](https://hbase.apache.org)
- 负载均衡:[nginx](http://nginx.org),[LVS](http://www.linuxvirtualserver.org),[haproxy](http://www.haproxy.org)
- 水平扩展:[dubbo](https://github.com/alibaba/dubbo)
- 数据仓库:[presto](https://github.com/prestodb/presto),[kylin](http://kylin.apache.org),[hive](http://hive.apache.org)
- 数据分析:[zeppelin](https://zeppelin.apache.org),[hue](http://gethue.com)
- 机器学习:[numpy](http://www.numpy.org),[scikit-learn](http://scikit-learn.org),[RStudio](https://www.rstudio.com),[sprkml](https://spark.apache.org)
- 深度学习:[tensorflow](https://github.com/tensorflow),[caffe2](https://caffe2.ai),[PyTorch](http://pytorch.org/),[CUDA](https://developer.nvidia.com/cuda-downloads)
- 运营报表:[Bootstrap](http://getbootstrap.com),[ECharts](http://echarts.baidu.com/),[jetty](http://www.eclipse.org/jetty),[Tomcat](http://tomcat.apache.org)
- 统一授权:[OpenLDAP](http://www.openldap.org)
- 图数据库:[neo4j](https://neo4j.com)
- 邮件系统:[james](http://james.apache.org)
- 监控系统:[zabbix](https://www.zabbix.com)

# 谷歌十大信条
0. 一切以用户为中心，其他一切纷至沓来. Focus on the user and all else will follow.
0. 把一件事做到极致. It's best to do one thing really, really well.
0. 快比慢好. Fast is better than slow.
0. 网络社会需要民主. Democracy on the web works.
0. 您不一定要在桌子前找答案. You don't need to be at your desk to need an answer.
0. 不做坏事也能赚钱. You can make money without doing evil.
0. 未知的信息总是存在的. There's always more information out there.
0. 对信息的需求无所不在. The need for information crosses all borders.
0. 不穿西装也可以严肃认真. You can be serious without a suit.
0. 仅有优秀是远远不够的. Great just isn't good enough.

# 标准算法
- 推荐必读1:http://www.apachecn.org/map/179.html
- 推荐必读2:http://www.apachecn.org/map/145.html
- 机器学习:https://en.wikipedia.org/wiki/Portal:Machine_learning
- 梯度推进:https://en.wikipedia.org/wiki/Gradient_boosting
- PR算法:https://en.wikipedia.org/wiki/PageRank
- Word2vec:https://en.wikipedia.org/wiki/Word2vec
- tf–idf:https://en.wikipedia.org/wiki/Tf%E2%80%93idf
- k-means:https://en.wikipedia.org/wiki/K-means_clustering
- 随机森林:https://en.wikipedia.org/wiki/Random_forest
- 决策树:https://en.wikipedia.org/wiki/Decision_tree_learning
- 支持向量机:https://en.wikipedia.org/wiki/Support_vector_machine
- 贝叶斯分类:https://en.wikipedia.org/wiki/Naive_Bayes_classifier
- K最近邻:https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
- AdaBoost:https://en.wikipedia.org/wiki/AdaBoost

# 推荐系统
```
0、推荐候选集
1、决策树二次筛选,决策树IF-THEN规则
2、点击率预估排序
3、推荐结果展示
4、推荐结果反馈
平台组成:
离线处理:偏好矩阵计算、推荐候选集、内容特征(物)，偏好特征(人)，环境特征(地)
混合系统:召回策略、倒排索引、混合策略、点击预估、置顶加权
实验平台:流量分桶、桶分组、实验时间、实验组、特殊条件、实验数据对比/置信度/评估
反馈系统:实验对比、特征拟合
```

# 算法选择
![ml_estimator_map](img/ml_map.png)

# git commit
```shell
git config --global user.name smartbooks
git config --global user.email smartbooks@qq.com
git remote set-url origin https://smartbooks@github.com/smartbooks/ml-study.git
git push
```
