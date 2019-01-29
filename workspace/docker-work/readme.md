# docker

## install

```bash

#download dmg
wget https://download.docker.com/mac/stable/Docker.dmg

#show version
>docker --version
Docker version 18.09.1, build 4c52b90

#show info
>docker info
>docker stats
>docker pull centos    #安装镜像
>docker images         #查看本机已安装的镜像
>docker ps             #查看运行的容器
>docker port           #查看端口映射情况
>docker logs -f 291b5e1743ca    #查看容器日志
>docker start 291b5e1743ca      #启动容器
>docker stop 291b5e1743ca       #停止容器
>docker rm 291b5e1743ca         #删除容器
>docker rmi e40405f80704        #删除镜像
>docker top 291b5e1743ca        #查看容器内进程
>docker inspect 291b5e1743ca    #查看Docker底层信息
>docker search centos           #搜索镜像
>docker commit -m="has update" -a="author" e218edb10161 centos

#运行镜像实例
>docker run --help                               #查看命令帮助选项
>docker run -t -i centos                         #进入shell交互模式,exit退出
>docker run centos /bin/echo "hello World"       #容器内执行echo命令并退出
>docker run -d centos /bin/echo "hello world"    #进入后台模式运行命令

#docker run 命令选项
-d    #后台运行
-P    #容器内部随机端口映射到主机
-p port:port    #手工指定端口映射

```