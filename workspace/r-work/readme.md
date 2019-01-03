
# R环境快速入门
- RStudio,https://www.rstudio.com/products/rstudio/download/
- R基础库,https://cloud.r-project.org/bin/windows/base/R-3.4.3-win.exe
- Rserve Java跨平台调用,http://www.rforge.net/Rserve/files/

# 测试脚本
```r
#如果你能看到一个二维点图,那么恭喜你
x=rnorm(10)
y=rnorm(10)
plot(x,y)
```

# R模型保存/加载步骤
```r
#定义一个面积函数
area <- function(r){pi*r^2}

#面积计算结果
x <- area(10)

#保存内存镜像,save(x,path)x是一个对象,很抽象的那种,比如变量/模型/图像/矩阵/向量等等
save(x, file="mj.rdata")

#加载内存镜像
load("mj.rdata")

#输出对象X的值
print(x)

```

# R KMeans简单示例
```r
pig       <- read.csv('ha.pig.price.train.csv')
pig_vect  <- pig[c("year","week","pig_price","bean_pulp_price","chance","yumi","xiaomaifu","yufen","siliao","zhurou")]
pig_scala <- scale(pig_vect)
pig_km    <- kmeans(pig_scala,centers = 10)
pig_km$cluster
pig_km$centers
plot(pig_scala,col=pig_km$cluster)
save(pig_km,file = "simple_kmeans.rdata")
#预测模型该怎么做?就是输入一组变量,预测一下属于哪个聚类?

Pred.R <- function(x1,x2,x3){
    data  <- cbind(x1,x2,x3)
    score <- predict(modelname, data, type = 'prob')
    return(list(score))
}


```

# R一元线性回归
```r
x <- c(seq(0.10,0.18,by = 0.01),0.20,0.21,0.23)
y <- c(42.0,43.5,45.0,45.5,45.0,47.5,49.0,53.0,50.0,55.0,55.0,60.0)
plot(x,y)
lm.sol  <- lm(y~1+x)
summary(lm.sol)
new     <- data.frame(x = 0.16)
lm.pred <- predict(lm.sol,new,interval = "prediction",level = 0.95)
lm.pred
lm.pred[1]
lm.pred[2]
lm.pred[3]
```

# RServe相关
```

Usage: R CMD Rserve [<options>]

Options: --help  this help screen
 --version  prints Rserve version (also passed to R)
 --RS-port <port>  listen on the specified TCP port
 --RS-socket <socket>  use specified local (unix) socket instead of TCP/IP.
 --RS-workdir <path>  use specified working directory root for connections.
 --RS-encoding <enc>  set default server string encoding to <enc>.
 --RS-conf <file>  load additional config file.
 --RS-settings  dumps current settings of the Rserve
 --RS-source <file>  source the specified file on startup.
 --RS-enable-control  enable control commands
 --RS-enable-remote  enable remote connections

All other options are passed to the R engine.

===============================================================================

#安装包
install.packages("Rserve")

#加载包
library(Rserve)

#启动服务1
Rserve()

#启动服务2
D:\tool\R-3.4.3\library\Rserve\libs\x64>R CMD Rserve --help·
R CMD Rserve --RS-enable-remote --RS-conf E:/work/github/ml-study/r-work/Rserv.cfg

#查看Rserve配置
R CMD Rserve --RS-settings

Rserve v1.7-3
config file: Rserv.cfg
working root: /tmp/Rserv
port: 6311
local socket: [none, TCP/IP used]
authorization required: no
plain text password: not allowed
passwords file: [none]
allow I/O: yes
allow remote access: no
control commands: no
interactive: yes
max.input buffer size: 262144 kB
```

# OpenBLAS加速R计算
```
#参考链接：http://blog.csdn.net/a358463121/article/details/42713307
#依赖库[mingw64_dll.zip]：https://sourceforge.net/projects/openblas/files/v0.2.14/
#OpenBLAS加速库：https://jaist.dl.sourceforge.net/project/openblas/v0.2.14/OpenBLAS-v0.2.14-Win64-int64.zip

#R测试代码
x<-matrix(1:(6000*6000),6000,6000)  
system.time(tmp<-x%*%x)

#R自带库
  用户   系统   流逝 
157.80   0.36 158.65

#OpenBLAS库
 用户  系统  流逝 
26.88  0.81  7.33

#结论:只能告诉你是瞬间完成的！
```

# 参考资料
- Rserve实现java与R的互通,https://www.cnblogs.com/mutougezi/p/6140329.html
- R中的线性回归分析,https://www.cnblogs.com/malt927/p/6074185.html
- 数据挖掘模型如何进行线上部署,https://www.zhihu.com/question/49775870/answer/118149542