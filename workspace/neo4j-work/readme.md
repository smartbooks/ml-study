
# neo4j

## 安装

```
#https://neo4j.com/docs/operations-manual/current/installation/linux/rpm/#linux-yum
#https://neo4j.com/docs/operations-manual/current/installation/linux/

rpm --import https://debian.neo4j.org/neotechnology.gpg.key

#配置YUM源
vim /etc/yum.repos.d/neo4j.repo
[neo4j]
name=Neo4j RPM Repository
baseurl=https://yum.neo4j.org/stable
enabled=1
gpgcheck=1

#安装neo4j
yum install -y neo4j-3.5.12
yum install -y neo4j-enterprise-3.5.12

#卸载neo4j
yum remove neo4j-3.5.12
yum remove neo4j-enterprise-3.5.12

wget http://yum.neo4j.org/stable/neo4j-enterprise-3.5.12-1.noarch.rpm
wget http://yum.neo4j.org/stable/neo4j-3.5.12-1.noarch.rpm

rpm -i neo4j-enterprise-3.5.12-1.noarch.rpm
rpm -i neo4j-3.5.12-1.noarch.rpm

```

## 常用命令

```
#匹配所有数据
match (n) return n limit 10

#删除全部数据
match (n) delete n

#创建节点
CREATE (u:User{cf1_REG_NUMUSERID:'289215'}) return n

#合并操作,节点存在就覆盖,不存在就创建
MERGE(gp2:GoogleProfile2{ Id: 201402,Name:"Nokia"})

#创建关系289215->2780446
MATCH (a:User{cf1_REG_NUMUSERID:'289215'}),(b:User{cf1_REG_NUMUSERID:'2780446'}) CREATE (a)-[:init]->(b)

#查询289215认识的人
match (n:User{cf1_REG_NUMUSERID:"289215"})-[:init]-(b) return n,b

#查询全部关系
match (n)-[:USED]-(b) return n,b
match (n)-[:UNUSED]-(b) return n,b
match (n)-[:NEWREG]-(b) return n,b
match (n)-[]-(b) return n,b

#统计数据总数
match (n) return count(n)

#非重复IP地址数据
match (n) return count(distinct(n.cf1_IP))

#非重复IP地址,不包含NULL值
match (n) WHERE n.cf1_IP IS NOT NULL return count(distinct(n.cf1_IP))

#IP地址排序示例&别名
match (n) WHERE n.cf1_IP IS NOT NULL return n.cf1_IP as ip order by ip desc

#删除节点属性
MATCH (book{id:122}) REMOVE book.price RETURN book

#添加属性
MATCH (dc:DebitCard) SET dc.atm_pin=3456 RETURN dc

#SKIP查询
MATCH (emp:Employee) RETURN emp SKIP 2

#IN查询
MATCH (e:Employee) WHERE e.id IN [123,124] RETURN e.id,e.name,e.sal,e.deptno

#UNION查询
MATCH (cc:CreditCard) RETURN cc.id,cc.number
UNION
MATCH (dc:DebitCard) RETURN dc.id,dc.number
```

# 参考资料
- http://blog.csdn.net/starcrm/article/details/52576381
- https://www.w3cschool.cn/neo4j/properties.html
- https://neo4j.com/download/other-releases/#releases
- http://mvnrepository.com/artifact/org.neo4j.driver/neo4j-java-driver
- http://yum.neo4j.org/stable/
