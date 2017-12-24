
# tensorflow机器学些快速环境配置-windows

## 必备软件
- python-3.6.4-amd64,https://www.python.org/ftp/python/3.6.4/python-3.6.4-amd64.exe
- IDEA PyCharm,https://download.jetbrains.8686c.com/python/pycharm-professional-2017.3.1.exe

## PIP阿里云镜像配置
```shell
cd %APPDATA%
mkdir %APPDATA%/pip
vim %APPDATA%/pip/pip.ini

#内容如下
[global]
index-url=https://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com
```

## PIP安装依赖库
```shell

#PIP依赖包默认安装位置(我的机器)
D:\tool\Python36\Lib\site-packages

# GPU版本,只能二选一
pip install tensorflow-gpu

# CPU版本,只能二选一
pip install tensorflow

# 代数库
pip install numpy

# 图形库
pip install matplotlib
```

## 环境测试
```shell
python ./main.py
```