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
>docker port           #查看端口映射情况
>docker logs -f 291b5e1743ca    #查看容器日志
>docker start 291b5e1743ca      #启动容器
>docker stop 291b5e1743ca       #停止容器
>docker rm 291b5e1743ca         #删除容器
>docker rmi e40405f80704        #删除镜像
>docker top 291b5e1743ca        #查看容器内进程
>docker inspect 291b5e1743ca    #查看Docker底层信息
>docker search centos           #搜索镜像

>docker pull centos    #安装镜像
>docker images         #查看本机已安装的镜像
>docker ps -a          #查看运行的容器
>docker tag <镜像ID> smartbooks/work:<tag>
>docker commit -m="update" -a="smartbooks" <容器ID> smartbooks/work:<tag>    #镜像打标签
>docker push smartbooks/work:<tag>    #推送镜像到仓库

#运行镜像实例
>docker run --help                               #查看命令帮助选项
>docker run -t -i centos                         #进入shell交互模式,exit退出
>docker run centos /bin/echo "hello World"       #容器内执行echo命令并退出
>docker run -d centos /bin/echo "hello world"    #进入后台模式运行命令
>docker attach d48b21a7e439                      #进入正在运行的docker实例
>docker exec -it 2b05be77efe4 /bin/bash

#docker run 命令选项
-d    #后台运行
-P    #容器内部随机端口映射到主机
-p port:port    #手工指定端口映射

```

## Build Dockerfile

```bash

#编译镜像,确保目录下存在Dockerfile文件
cd $projectRoot
docker build -t abtest-server .

```

## Dockerfile Example

```dockerfile
#继承自父级镜像
FROM centos

#作者信息
MAINTAINER smartbooks

#容器内部环境变量
ENV APP_ROOT /data/service/app
ENV APP_JAR docker-sample.jar

#容器内部安装的依赖
RUN mkdir -p ${APP_ROOT}
RUN yum -y install java-1.8.0-openjdk-1.8.0.191.b12-1.el7_6.x86_64

#容器内部运行的身份
#USER work

#容器内部开启的端口
EXPOSE 9999

#容器内部的挂载目录
VOLUME ${APP_ROOT}/config

#容器内部的工作目录
WORKDIR ${APP_ROOT}

#将本地文件复制到容器内部
ADD core-site.yaml ${APP_ROOT}
ADD ./target/${APP_JAR} ${APP_ROOT}
ADD ./target/lib ${APP_ROOT}/lib

#容器启动时执行的命令,存在多个CMD,以最后一条为准,可以替换
CMD java -jar ${APP_ROOT}/${APP_JAR}

#容器启动时执行的命令,只能有1条,不可替换
ENTRYPOINT java -jar ${APP_ROOT}/${APP_JAR}

```