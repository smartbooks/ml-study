
# Solr
```
#命令
solrctl

#生成实体配置文件
solrctl instancedir --generate /data/bigwork/wangya/solr/kmarket

#创建实体并上传
solrctl instancedir --create kmarket /data/bigwork/wangya/solr/kmarket

#更新实体配置
solrctl instancedir --update kmarket /data/bigwork/wangya/solr/kmarket

#删除实体
solrctl instancedir --delete kmarket

#查看已上传的实体
solrctl instancedir --list

#创建集合-s表示设置Shard数为1,-r表示设置的replica数为1
solrctl collection --create kmarket -s 2 -r 1

#删除集合
solrctl collection --delete kmarket

#重新加载
solrctl collection --reload kmarket

solrctl collection --list
```


# 参考链接
- http://blog.csdn.net/kissmelove01/article/details/45043955
- https://www.cnblogs.com/arli/p/6248819.html
