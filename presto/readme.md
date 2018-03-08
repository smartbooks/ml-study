
# 快速参考
- 官网:https://prestodb.io
- 中文:http://prestodb.org.cn
- 源码:https://github.com/prestodb/presto

## 编译源码(只支持LINUX)
```shell
yum -y install git
wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo
yum -y install apache-maven

git clone https://github.com/prestodb/presto
git checkout -b 0.196-lzkj 0.196
git branck

mvn -N io.takari:maven:wrapper -Dmaven=3.5.2
./mvnw clean install
```

## presto-server-config
```shell
export PRESTO_HOME=/media/data1/tool/presto-server-0.196

#创建配置文件目录
mkdir $PRESTO_HOME/etc

#创建节点数据目录,建议选择一个较大存储空间的分区
mkdir $PRESTO_HOME/data

#节点标识配置
cat $PRESTO_HOME/etc/node.properties
node.environment=production
node.id=0000000000
node.data-dir=/media/data1/tool/presto-server-0.196/data

#服务配置(单节点)
cat $PRESTO_HOME/etc/config.properties
coordinator=true
node-scheduler.include-coordinator=true
http-server.http.port=8080
query.max-memory=50GB
query.max-memory-per-node=1GB
discovery-server.enabled=true
discovery.uri=http://0.0.0.0:8080

#JVM配置
$PRESTO_HOME/etc/jvm.config
-server
-Xmx16G
-XX:+UseG1GC
-XX:G1HeapRegionSize=32M
-XX:+UseGCOverheadLimit
-XX:+ExplicitGCInvokesConcurrent
-XX:+HeapDumpOnOutOfMemoryError
-XX:+ExitOnOutOfMemoryError

#日志配置
cat $PRESTO_HOME/etc/log.properties
com.facebook.presto=INFO

#数据库配置(要求读写权限)
#支持连接器:https://prestodb.io/docs/current/connector.html
$PRESTO_HOME/etc/catalog/mongodb.properties
connector.name=mongodb
mongodb.seeds=0.0.0.0:27017
mongodb.credentials=username:password@db
mongodb.schema-collection=_schema

```

## presto-server
```shell
#HOME环境变量配置
export PRESTO_HOME=/media/data1/tool/presto-server-0.196

#单个进程运行
$PRESTO_HOME/bin/launcher run

#守护进程运行
$PRESTO_HOME/bin/launcher start

#更多命令详情
$PRESTO_HOME/bin/launcher --help
回显:
Usage: launcher [options] command

Commands: run, start, stop, restart, kill, status

Options:
  -h, --help            show this help message and exit
  -v, --verbose         Run verbosely
  --etc-dir=DIR         Defaults to INSTALL_PATH/etc
  --launcher-config=FILE
                        Defaults to INSTALL_PATH/bin/launcher.properties
  --node-config=FILE    Defaults to ETC_DIR/node.properties
  --jvm-config=FILE     Defaults to ETC_DIR/jvm.config
  --config=FILE         Defaults to ETC_DIR/config.properties
  --log-levels-file=FILE
                        Defaults to ETC_DIR/log.properties
  --data-dir=DIR        Defaults to INSTALL_PATH
  --pid-file=FILE       Defaults to DATA_DIR/var/run/launcher.pid
  --launcher-log-file=FILE
                        Defaults to DATA_DIR/var/log/launcher.log (only in
                        daemon mode)
  --server-log-file=FILE
                        Defaults to DATA_DIR/var/log/server.log (only in
                        daemon mode)
  -D NAME=VALUE         Set a Java system property
```


## presto-jdbc
```shell

#参考官网:https://prestodb.io/docs/current/installation/jdbc.html

wget https://repo1.maven.org/maven2/com/facebook/presto/presto-jdbc/0.196/presto-jdbc-0.196.jar

OR

<dependency>
    <groupId>com.facebook.presto</groupId>
    <artifactId>presto-jdbc</artifactId>
    <version>0.196</version>
</dependency>

```

## Cli
```shell

#下载命令行包
wget https://repo1.maven.org/maven2/com/facebook/presto/presto-cli/0.196/presto-cli-0.196-executable.jar
chmod +x ./presto-cli-0.196-executable.jar
mv ./presto-cli-0.196-executable.jar ./presto.jar

#进入SHELL
./presto --server 0.0.0.0:8080 --catalog mongodb --schema _schema

#切换SCHEMA
use mongodb._schema

#查询示例
#SELECT * FROM [db].[collection]
select * from lzkj.userinfo limit 100;

#查看表结构(q键退出)
DESC lzkj.userinfo;

#帮助命令
help;
回显:
Supported commands:
QUIT
EXPLAIN [ ( option [, ...] ) ] <query>
    options: FORMAT { TEXT | GRAPHVIZ }
             TYPE { LOGICAL | DISTRIBUTED }
DESCRIBE <table>
SHOW COLUMNS FROM <table>
SHOW FUNCTIONS
SHOW CATALOGS [LIKE <pattern>]
SHOW SCHEMAS [FROM <catalog>] [LIKE <pattern>]
SHOW TABLES [FROM <schema>] [LIKE <pattern>]
SHOW PARTITIONS FROM <table> [WHERE ...] [ORDER BY ...] [LIMIT n]
USE [<catalog>.]<schema>

#退出
exit
```

