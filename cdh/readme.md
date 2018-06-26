
# CDH快速入门指南
```
下载地址:https://www.cloudera.com/downloads/manager/5-11-0.html
SPARK2要求:https://www.cloudera.com/documentation/spark2/latest/topics/spark2_packaging.html
操作系统:centos-6.8 x86-64
```

# 注意事项
* 同一集群要求运行同一版本操作系统、cloudera-manager-server、cloudera-manager-agent、cdh.
* 推荐使用操作系统centos-6.8 x86-64.
* 内网信任模式运行,建议关闭外网访问,关闭每台主机防火墙.
* 每台主机的tmp目录不可删除,也不可以随便删除文件个数据,否则重新安装集群.

# 下载parcel离线文件
```shell
#下载cdh离线parcels压缩包
wget http://archive.cloudera.com/cdh5/parcels/latest/CDH-5.11.0-1.cdh5.11.0.p0.34-el6.parcel
wget http://archive.cloudera.com/cdh5/parcels/latest/CDH-5.11.0-1.cdh5.11.0.p0.34-el6.parcel.sha1
mv ./CDH-5.11.0-1.cdh5.11.0.p0.34-el6.parcel.sha1 ./CDH-5.11.0-1.cdh5.11.0.p0.34-el6.parcel.sha
```

# 制作YUM本地离线安装源

## 制作本地源
```shell
cd /opt/
wget http://archive.cloudera.com/cm5/repo-as-tarball/5.11.0/cm5.11.0-centos6.tar.gz
yum -y install httpd
chkconfig httpd on
service httpd start
tar xvfz ./cm5.11.0-centos6.tar.gz
mv cm /var/www/html
chmod -R ugo+rX /var/www/html/cm
```

## 分发repo文件到全部服务器中

- 文件名称:cloudera-manager.repo
- 存储路径:/etc/yum.repos.d/cloudera-manager.repo

```
[cloudera-manager]
name = Cloudera Manager, Version 5.11.0
baseurl = http://192.168.1.17/cm/5
enabled = 1
gpgcheck = 0
```

# 服务器环境初始化(每台)
```shell

#检查操作系统版本
cat /etc/system-release

yum -y install wget

echo "下载阿里云YUM源配置"
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo
wget -O /etc/yum.repos.d/cloudera-cm5.repo http://192.168.1.17/cm/cloudera-cm5.repo
wget -O /etc/hosts http://192.168.1.17/cm/hosts
wget -O /opt/jdk-8u121-linux-x64.rpm http://192.168.1.17/tool/jdk-8u121-linux-x64.rpm
rpm -ivh /opt/jdk-8u121-linux-x64.rpm

echo "更新YUM缓存"
yum clean all
yum list update
yum makecache
yum repolist

echo "安装ntpd"
yum -y install ntp
chkconfig ntpd on
service ntpd start

echo "安装scp"
yum -y install openssh-clients

echo "同步HOST"

echo "修改HOSTNAME"
cat /etc/sysconfig/network
vi /etc/sysconfig/network
hostname jx-1-

echo "关闭防火墙"
service iptables stop
service iptables start
chkconfig iptables off

#防火墙配置
vi /etc/sysconfig/iptables

*filter
:INPUT ACCEPT [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]
-A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
-A INPUT -p icmp -j ACCEPT
-A INPUT -i lo -j ACCEPT
-A INPUT -i eth0 -j REJECT #拒绝外网网卡
-A INPUT -m state --state NEW -m tcp -p tcp --dport 22 -j ACCEPT
COMMIT

#重启防火墙
service iptables restart

#开机自启动
chkconfig iptables on

*********************************************************************
#防火墙操作
http://blog.csdn.net/u011846257/article/details/54707864
-A INPUT -i eth0 -j REJECT

#查看打开的端口
/etc/init.d/iptables status

#开启端口
iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
*********************************************************************

echo "系统参数调整"
vi /etc/sysctl.conf
vm.swappiness=10

sysctl vm.swappiness=10

vi /etc/rc.local
echo never > /sys/kernel/mm/transparent_hugepage/defrag
echo never > /sys/kernel/mm/transparent_hugepage/enabled

```

# HOST配置参考
```
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
192.168.1.11 jx-1-11
192.168.1.16 jx-1-16
192.168.1.19 jx-1-19
192.168.1.30 jx-1-30
192.168.1.35 jx-1-35
192.168.1.7  jx-1-7
192.168.1.14 jx-1-14
192.168.1.3  jx-1-3
192.168.1.9  jx-1-9
```

# 安装cloudera-manager-service
```shell
wget -O /opt/cloudera-manager-installer.bin http://archive.cloudera.com/cm5/installer/latest/cloudera-manager-installer.bin
chmod u+x /opt/cloudera-manager-installer.bin
#使用本地yum源
/opt/cloudera-manager-installer.bin --skip_repo_package=1
#安装完成后,浏览器打开链接:http://localhost:7180/
#注意:
#1.先不要运行安装向导,否则网速慢的环境装起来很痛苦.
#2.CM默认使用postgrap数据库,生产环境要切换为mysql数据库,阅读《更改CM监控数据库》
```

# 安装cloudera-manager-agent(每台)
```
#1.要求每台机器配置使用本地YUM源
#2.先安装作为集群监控的某台机器的cloudera-manager-agent
#3.登录CM:http://localhost:7180 安装cloudera-manager-service
#4.安装cloudera-manager-agent到剩余的全部机器
#5.参考一下步骤,逐台安装和配置并启动服务
#6.登录CM:http://localhost:7180 查看全部主机,检查是否所有主机的监控状态全部刷新
#7.在CM首页中点击添加新集群,选择"当前已受CM管理的主机",选择下一步,之后停止安装操作(防止自动联网下载parcel安装包)
#8.复制[*.parcel和*.parcel.sha]离线包到CM主机目录:/opt/cloudera/parcel-repo/
#9.在主机菜单中,单机检查parcel,选择parcel->Cluster1->CDH5,单击分配parcel按钮,即可使用本地离线安装包
#10.在CM主机列表中看到每台主机监控状态刷新到CDH版本信息,即可开始为集群中每台机器分配HADOOP角色啦
#11.分配完毕角色之后,全部机器重新启动一遍,观察集群是否可以自动正常工作

#安装cloudera-manager-agent
yum -y install cloudera-manager-agent
chkconfig cloudera-scm-agent on
wget -O /etc/cloudera-scm-agent/config.ini http://192.168.1.17/cm/config.ini
service cloudera-scm-agent restart
service cloudera-scm-agent start
service cloudera-scm-agent status

#修改cloudera-manager-agent监控地址指向cloudera-manager-server
vi /etc/cloudera-scm-agent/config.ini
#server_host=<cm-server>

#启动cloudera-manager-agent服务
service cloudera-scm-agent start
#或
/etc/init.d/cloudera-scm-agent start

chkconfig cloudera-scm-agent on

#查看cloudera-manager-agent服务运行状态
service cloudera-scm-agent status
```

# 更改CM监控数据库
```
yum install -y mysql-server mysql mysql-deve
chkconfig mysqld on
service mysqld start
/usr/bin/mysqladmin -u root password 'root'
mysql -u root

GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY 'root' WITH GRANT OPTION;
flush privileges;
create database scm DEFAULT CHARSET utf8 COLLATE utf8_general_ci;

#在CM主机执行
/usr/share/cmf/schema/scm_prepare_database.sh mysql --scm-host jx-1-11 scm root root

#重启CM
service cloudera-scm-server restart
```


# 其他参考

- 卸载CM:https://www.cloudera.com/documentation/enterprise/latest/topics/cm_ig_uninstall_cm.html
- 下载离线CM源:https://www.cloudera.com/documentation/enterprise/latest/topics/cm_ig_create_local_package_repo.html#cmig_topic_21_3_1
- 创建本地CM源:https://www.cloudera.com/documentation/enterprise/latest/topics/cm_ig_create_local_package_repo.html

# 读者建议
问：如果安装失败了怎么办？
答：建议重新安装操作系统.
