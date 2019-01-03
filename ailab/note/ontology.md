
# 用户画像

## HBase用户画像表存储结构
```
存储需求(支持10W+属性):
用户属性:Map<String,Object>
用户标签:Map<Long,String>

用户属性对数据:
RowKey:Guid ColumnFamily:f1 Column:属性=值

用户标签集数据:
RowKey:Guid ColumnFamily:f2 Column:标签1=在学车,标签2=炒股...标签N=描述M

```

## 用户画像元数据架构
- 数据库名:UserProfileMetaStore

### 用户属性元数据表
- 数据库表名:user_property

|序号|字段名称|字段类型|字段长度|字段说明|
|:---:|:----|:---|:---:|:---|
|1|id|int|8|自增主键|
|2|name_space|string|255|HBASE表空间|
|3|table_name|string|255|HBASE表名|
|4|column_family|string|255|HBASE表列族|
|5|property_name|string|255|属性名称|
|6|property_doc|string|255|属性描述|
|7|property_type|string|255|属性值类型|
|8|property_default_value|string|255|属性默认值|

### 用户标签元数据表
- 数据库表名:user_tag

|序号|字段名称|字段类型|字段长度|字段说明|
|:---:|:----|:---|:---:|:---|
|1|id|long|16|自增主键,标签ID|
|2|name_space|string|255|HBASE表空间|
|3|table_name|string|255|HBASE表名|
|4|column_family|string|255|HBASE表列族|
|5|tag_text|string|255|标签文本|
|6|tag_filter|string|255|标签数据过滤条件,示例:age>20 AND age<30|
|7|group_id|int|8|所属标签组|

### 标签组元数据表
- 数据库表名:user_tag_group

|序号|字段名称|字段类型|字段长度|字段说明|
|:---:|:----|:---|:---:|:---|
|1|id|int|8|自增主键,标签组ID|
|2|group_name|string|255|标签组名称|
|3|parent_group_id|int|8|父级组标签组ID,根节点0|

## 用户画像数据查询
- 按rowkey主键uid查询
- 按属性条件查询(配合二级索引实现)

### 查询结果示例
```
#标签描述
tag_100:炒股
tag_101:戏迷
tag_102:街舞
tag_103:影迷
tag_104:养生
tag_105:驴友

#查询结果
#uid,age,gender,work_city,tag_100,tag_101,tag_104,tag_105
100,55,男,北京,炒股,戏迷,养生,驴友

#特征工程
#uid,age,gender,work_city,tag_100,tag_101,tag_102,tag_103,tag_104,tag_105
100,55,1,110000,1,1,0,0,1,1
```
