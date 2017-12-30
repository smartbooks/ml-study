
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

# RServe相关
```
#安装包
install.packages("Rserve")

#加载包
library(Rserve)

#启动服务1
Rserve()

#启动服务2
D:\tool\R-3.4.3\library\Rserve\libs\x64>R CMD Rserve --help·
R CMD Rserve --RS-enable-remote

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

# 参考资料
- Rserve实现java与R的互通,https://www.cnblogs.com/mutougezi/p/6140329.html