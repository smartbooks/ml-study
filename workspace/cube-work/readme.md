
# 参考资料

## Facebook贡献的开源MPP OLAP引擎
- https://prestodb.io/
- http://prestodb-china.com/
- http://lxw1234.com/archives/2017/07/867.htm
- http://kylin.apache.org/

## 版本库定位
```
#查看本地所有TAG
git tag

#切换到指定TAG
git checkout 0.196

#基于0.196标签创建0.196-lzkj开发标签
git checkout -b 0.196-lzkj 0.196

#还原本地更改
git reset

#查看当前分支
git branch
```

## 编译过程
```shell
yum -y install git

wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo
yum -y install apache-maven

mvn -N io.takari:maven:wrapper -Dmaven=3.5.2
mvnw clean compile
```


## 参考资料
- https://www.cnblogs.com/bchen/p/7492929.html
- http://blog.csdn.net/xtqve/article/details/51670116
- http://itgrocery.cn/2017/05/01/Presto-Oracle-%E6%8F%92%E4%BB%B6%E7%BC%96%E5%86%99%E6%95%99%E7%A8%8B/
