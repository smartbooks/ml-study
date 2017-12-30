
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

# 参考资料
- Rserve实现java与R的互通,https://www.cnblogs.com/mutougezi/p/6140329.html