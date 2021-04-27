# 广告平台

## 名词解释

- 广告商:买卖方撮合
- 广告主:投放广告&买量增长
- 流量主:广告位流量变现

## 核心工程

- 广告展示组件[广告商]:
    - 积分墙广告:
    - 交叉推广广告:
    - 视频广告:
    - 开屏广告:
- 灰度测试系统[广告商]:主要关注大规模灰度实验
- 策略服务系统[广告商]:主要关注算法版本迭代、升级、回滚、部署、评估；以及分层、池子召回、排序策略融合；
- 策略评估系统:
    - 广告商:AB实验、模型算法
    - 流量主:cpm、ltv、arpu、广告渗透率、人均广告曝光量、广告ARPU、拉取量、曝光量、曝光率、点击量、点击率、ecpm、收入
    - 广告主:花费、曝光次数、点击次数、点击率、转化目标量、转化目标成本、目标转化率
- 数据管理系统:
    - 广告商:主要关注人群/曝光/点击/归因，面向OLAP分析型GP数据仓库
    - 广告主:号码包
- 内容管理系统:
    - 流量主:广告位管理
    - 广告主:广告/物料/创意
- 结算评估系统:
    - 流量主:广告位概况、收益、结算
    - 广告主:充值、预算、消耗、计费、成本
- 用户画像系统[广告商]:主要关注人群概况
- 流量反作弊系统[广告商]:

## 参考资料

- [Group Input Format](https://github.com/dmlc/xgboost/blob/master/doc/tutorials/input_format.rst#group-input-format)
- [XGBoost rank demo](https://github.com/dmlc/xgboost/tree/master/demo/rank)
- [Introduction to Learning to Rank](https://everdark.github.io/k9/notebooks/ml/learning_to_rank/learning_to_rank.html)
- [《LambdaMART Demystified》](https://staff.fnwi.uva.nl/e.kanoulas/wp-content/uploads/Lecture-8-1-LambdaMart-Demystified.pdf)
- [《Unbiased LambdaMART: An Unbiased PairwiseLearning-to-Rank Algorithm》](https://arxiv.org/pdf/1809.05818.pdf)
- [LambdaMART](https://www.microsoft.com/en-us/research/uploads/prod/2016/02/MSR-TR-2010-82.pdf)
- [MLUtils.saveAsLibSVMFile](http://spark.apache.org/docs/2.2.2/api/java/org/apache/spark/mllib/util/MLUtils.html#saveAsLibSVMFile-org.apache.spark.rdd.RDD-java.lang.String-)
- [XGBoost 网格搜索调参](https://www.jianshu.com/p/392b6ef4656b)
- [XGBoost pairwise评分转概率](https://blog.csdn.net/weixin_42001089/article/details/84146238)
- [XGBoost在携程搜索排序中的应用](https://zhuanlan.zhihu.com/p/97126793)
- [XGBoost Parameters](https://github.com/dmlc/xgboost/blob/master/doc/parameter.rst)
- [XGBoost Python API](https://xgboost.readthedocs.io/en/latest/python/python_api.html)
- [《Overlapping Experiment Infrastructure More, Better, Faster Experimentation》](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/36500.pdf)
- ISBN:9787115497482《计算广告 互联网商业变现的市场与技术 第2版》
- [DMP数据管理平台](https://de.qq.com/featuresportal/data-access/summary)
- [热温冷数据集成方案](https://blog.cloudera.com/transparent-hierarchical-storage-management-with-apache-kudu-and-impala/)
- https://item.jd.com/12429306.html
- https://item.jd.com/47612225922.html
- https://item.jd.com/12085226.html
- https://item.jd.com/26670953699.html
- https://github.com/dmlc/xgboost
- https://xgboost.ai/
- https://tensorflow.google.cn/
- https://github.com/Microsoft/LightGBM
- https://scikit-learn.org/
- https://keras.io/zh/
- http://pytorch.org/
- [广告归因](https://www.facebook.com/business/help/458681590974355?id=768381033531365)
- [wx.navigateToMiniProgram](https://developers.weixin.qq.com/minigame/dev/api/open-api/miniprogram-navigate/wx.navigateToMiniProgram.html)
- [巨量:监测链接发送服务](https://ad.oceanengine.com/openapi/doc/index.html?id=1299)
- [广点通:获取点击数据](https://developers.e.qq.com/docs/guide/user_actions/new_click_data)
- [史上最详细的XGBoost实战](https://zhuanlan.zhihu.com/p/31182879)
- [数据类别不平衡](https://www.ai1994.com/2018/10/25/Imbalanced-Datasets/)
- [A Beginner’s Guide to Word Embedding with Gensim Word2Vec Model](https://towardsdatascience.com/a-beginners-guide-to-word-embedding-with-gensim-word2vec-model-5970fa56cc92)
- [广告系统的平台架构与交互流程](http://neoremind.com/2020/01/ad_system_architecture/)
- [cloriSearch](https://github.com/shpilu/cloriSearch)
- [阿里技术嘉年华 2013 Slide PPT PDF](https://github.com/alswl/adc2013)
- [Nginx流量镜像使用技巧](https://cloud.tencent.com/developer/article/1495449)
- [Bytedeco makes](http://bytedeco.org/)
- [美团广告实时索引的设计与实现](https://tech.meituan.com/2018/05/11/adp-rtidx-ls.html)
- [美团点评效果广告实验配置平台的设计与实现](https://mp.weixin.qq.com/s/R7vsxiXLXcjJDOBigrlYKg)
- [美团DSP广告策略实践](https://mp.weixin.qq.com/s/5mrOX1puY6WvoRP3X2wTZw)
- [美团点评联盟广告的场景化定向排序机制](https://mp.weixin.qq.com/s/xigME-griWFwEvvPNqWuvg)
- [AdNetwork和AdExchange区别](https://blog.csdn.net/chenglian1987/article/details/76229051)
- [处理海量数据：列式存储综述](https://zhuanlan.zhihu.com/p/35622907)
- [流失预警模型](https://zhuanlan.zhihu.com/p/93059773)
- [流失挽留](https://zhuanlan.zhihu.com/p/93559578)
- [流失分析方法5_流失前最后一次游戏行为法](https://zhuanlan.zhihu.com/p/89375647)
- [流失分析方法4_流失和留存用户对比分析法](https://zhuanlan.zhihu.com/p/88420788)

## 接口文档

### 拉取广告

- 正式环境:http://xxxxxxxxxxxxxx/feed/item
- 开发环境:http://localhost:8080/feed/item
- 请求方式:GET
- 请求参数:
    - reg_uid:[必须,2选1]注册用户UID;优先传递reg_uid,未注册用户传递device_id,两者传递其中一个即可
    - device_id:[必须,2选1]游客设备ID,优先传递reg_uid,未注册用户传递device_id,两者传递其中一个即可
    - page_size:[非必须]默认返回20条
- 返回结果:

```json
{
    "msg": "success",                      //状态消息
    "code": "100",                         //错误代码100:正常|101:参数错误|102:未知错误|103:请求过于频繁
    "data": {
        "item_list_size": 10,              //实际返回结果数
        "item_list": [                     //接口返回结果
            {
                "deviceId": "",                                     //[需要采集]请求用户设备号
                "userId": 1069722,                                  //[需要采集]请求用户UID,游客时为0
                "rqtime": 1536819292870,                            //[需要采集]本次请求的时间戳
                "rquuid": "4ddd8205-5f50-49fe-b30e-3e2d141bf343",   //[需要采集]本次请求的唯一标识
                "abTest": null,                                     //AB测试策略,当前保留未使用,后续版本会加入
                "uuid" : "3f3d8811-18aa-495d-813a-659a4e028a31",    //[需要采集]本次请求结果的唯一ID标识
                "id": "white_418078",               //索引唯一标识
                "ignore": false,                    //忽略结果标识,召回系统内部排重使用
                "itemCreateTime": 1535096889000,    //作品发布时间
                "itemId": 418078,                   //[需要采集]作品唯一ID
                "itemScore": 0.18924959,            //算法评分,召回系统内部排序使用
                "itemUserId": 807562,               //作品所属作者用户UID
                "poolName": "WhiteListPool",        //召回结果池名称
                "modelName": "home-cnxh",           //数据适配的模块名称
                "ranking": 1,                       //推荐结果排名位置,从1开始计数
                "summary": {                        //推荐原因
                    "event": "love",                //触发事件
                    "sourceType": 0,                //触发事件原因类型|-1:无|0:用户|1:系统
                    "sourceValue": "1069722",       //触发事件对象
                    "targetType": 1,                //被触发目标类型|-1:无|0:用户|1:作品
                    "targetValue": "230174",        //被触发目标对象
                    "time": 1536289421000           //触发事件事件
                }
            }
            //...
        ],
        "req_pam": {
            "reg_uid": 1069722,         //客户端请求参数:注册用户UID
            "page_size": 10,            //客户端请求参数:结果条数,召回接口根据情况实际返回条数不一定等于page_size
            "device_id": ""             //客户端请求参数:设备唯一标识
        }
    },
    "use_time": 999,                    //推荐接口响应时间
    "end_time": 1536310970326,          //推荐接口接受请求时间戳
    "measure_status": "healthy",        //推荐接口性能度量状态:大于1秒warning|小于1秒healthy
    "begin_time": 1536310871449,        //推荐接口完整请求时间戳
    "version": 1,                       //接口协议版本
    "status": 0                         //状态:0成功|1异常
}
```
