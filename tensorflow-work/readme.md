
# tensorflow机器学些快速环境配置-windows

## 必备软件
- python-3.6.4-amd64,https://www.python.org/ftp/python/3.6.4/python-3.6.4-amd64.exe
- IDEA PyCharm,https://download.jetbrains.8686c.com/python/pycharm-professional-2017.3.1.exe
- https://github.com/tensorflow/tensorflow
- https://developer.nvidia.com/cuda-90-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal
- http://www.tensorfly.cn/tfdoc/get_started/introduction.html
- http://developer2.download.nvidia.com/compute/machine-learning/cudnn/secure/v7.0.5/prod/9.0_20171129/cudnn-9.0-windows10-x64-v7.zip?0PErSgeB3sJpMttjxrHjV1_tKf1yBw7Li9Hve6jBJ8DV-DuwTHTzzkMVqDasU0PIKVaqp6jDST9PDr9yZIFPWQjY8jtswGDd-nFziNNv18z7HbOkCn9v7EgJyCYWmq-G3rixvEHpTz1SDbs88d6VjMhYkSXLU89MxnyVbdJmZyZfBvwmGjerny_plBcHA67qqyK7nWLG2n8AEViS
- Download cuDNN v7.0.5 (Dec 5, 2017), for CUDA 9.0
- cuDNN v7.0.5 Library for Windows 10
- https://pypi.python.org/pypi?%3Aaction=search&term=tensorflow&submit=search

## 特殊说明
```
tensorflow-gpu==1.5.0 需要 CUDA Toolkit 9.0
```

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
pip install tensorflow-gpu==1.5.0

# CPU版本,只能二选一
pip install tensorflow==1.5.0
pip uninstall tensorflow==1.5.0

# 代数库
pip install numpy

# 图形库
pip install matplotlib

# OpenCV支持
pip install opencv-python
```

## 环境测试
```shell
python ./main.py
```

## 常见错误
```
#futures requires Python '>=2.6, <3' but the running Python is 3.5.3
#https://github.com/tensorflow/tensorflow/issues/16478
pip install futures==3.1.1
pip install tensorflow-gpu==1.5.0
pip uninstall tensorflow-gpu==1.5.0
```
