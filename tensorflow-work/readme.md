
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
- https://opencv.org/releases.html
- https://zhuanlan.zhihu.com/p/26514493
- https://www.cnblogs.com/chaosimple/p/4153167.html
- http://scikit-learn.org/stable
- https://github.com/scikit-learn/scikit-learn
- http://www.apachecn.org/
- https://github.com/apachecn/MachineLearning
- https://github.com/apachecn/scikit-learn-doc-zh
- CUDA:GPU并行计算平台
- cuDNN:CUDA平台下面向深度学习库,用于训练模型
- TensorRT:推理引擎,即加载深度学习模型到GPU,并对新数据做出预测
- DeepStream SDK:视频分析,包括图像分类、目标检测、识别和跟踪等
- cuBLAS:一个基于GPU的BLAS(向量和矩阵计算)库
- cuSPARSE:稀疏矩阵和向量计算库
- NCCL:可以理解为GPU集群模式协调管理库
- 关于超算:http://www.nvidia.cn/object/cuda-ecosystem-cn.html

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

# 机器学习库可以进行归一化处理
pip install sklearn

pip install scipy
pip install scikit-learn

# 编译scikit-learn库
pip install Cython
python setup.py install
```

## 环境测试
```shell
python ./main.py
```

## jupyter
```shell
#详细使用手册:http://datascience-enthusiast.com

yum -y install python-devel
pip install --upgrade pip
pip install jupyter

#生成配置文件
jupyter notebook --generate-config

#编辑配置文件
vim /home/guest/.jupyter/jupyter_notebook_config.py
c.NotebookApp.ip = '172.17.10.100'
c.NotebookApp.notebook_dir = u'/data/bigwork/jupyter-notebook/notebook-dir'
c.NotebookApp.open_browser = False
c.NotebookApp.password_required = True
c.NotebookApp.port = 8888

#设置密码
jupyter notebook password

#启动服务
jupyter notebook
```

## 常见错误
```
#futures requires Python '>=2.6, <3' but the running Python is 3.5.3
#https://github.com/tensorflow/tensorflow/issues/16478
pip install futures==3.1.1
pip install tensorflow-gpu==1.5.0
pip uninstall tensorflow-gpu==1.5.0
```

## 扩展阅读
- 机器学习资源大全:http://tensorfly.cn/tfdoc/mltools.html
- https://www.anaconda.com
- https://www.jianshu.com/p/2ea7a0632239
- https://mirror.tuna.tsinghua.edu.cn/help/anaconda/
- 参数服务器Petuum/Bosen:https://github.com/sailing-pmls/bosen
- 参数服务器:https://github.com/cnkuangshi/LightCTR
- 参数服务器:https://github.com/dmlc/ps-lite
- 持续构建:https://travis-ci.org
- https://github.com/dmlc
- https://github.com/PipelineAI/pipeline
